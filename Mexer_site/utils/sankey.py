####################################################################
# sankey.py includes all the functions related to sankey diagrams
# 
# The main point is to get the data for rendering a sankey diagram
# Which is achieved through get_sankey()
#
# Which will return the data needed to pass to the JS library
# SanKEY.js (https://github.com/Krzysiekzd/SanKEY.js)
#
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu 
#####################
import json
from utils.translator import Translator
from utils.data import _query_database, DatabaseTarget
from Mexer_meta.settings import SANKEY_COLORS_PATH
from utils.logging import LOGGER
from collections import Counter
from django.db import connections
from Mexer.models import Index

INDUSTRY_COLOR = "midnightblue"
OVERRIDE_COL = 1 # where to put energy carrier nodes
OVERRIDE_COL_ON = False # only affects energy carrier columns

with open(SANKEY_COLORS_PATH) as f:
    SANKEY_COLORS: dict[str, str] = json.loads(f.read())

class NodeInfo:
    def __init__(self, column: int, index: int):
        self.column = column
        self.index = index

def _get_sankey_color(node_name: str) -> str:
    carrier_name = ""

    for carrier_category in SANKEY_COLORS:
        if carrier_category in node_name.lower():
            carrier_name = carrier_category
            break

    return SANKEY_COLORS.get(carrier_name) or (LOGGER.error("Couldn't find sankey color for " + node_name) or "") # return empty string if can't find

### shape of data to be returned
# nodes = [
#     [ <- column 0
#         {"label": "label1", "color": "color1"},
#         {"label": "label2", "color": "color2"},
#         ...
#     ],
#     ... repeated
# ]
###
def _create_new_node(name: str, node_info_by_name: dict, indexes_by_col: Counter, sankey_orders: dict) -> NodeInfo:
    ''' Creates a new node info for a given name '''
    node_column = sankey_orders.get(name, -1) # -1 represents an error state

    node_info = NodeInfo(node_column, indexes_by_col[node_column]) # store column and next index in column
    indexes_by_col[node_column] += 1 # update next index in column for next node

    node_info_by_name[name] = node_info # save node info
    return node_info

def _get_node_info(name: str, node_info_by_name: dict) -> NodeInfo:
    ''' Gets the node info for a given name. A little redundant, but it ensures proper exceptions are thrown '''
    # either get the node info or throw an error
    node_info = node_info_by_name.get(name)
    if not node_info:
        raise KeyError("Node info not found for " + name)
    return node_info

def get_sankey(target: DatabaseTarget, query: dict) -> tuple[str, str, str] | tuple[None, None, None]:
    ''' Gets a sankey diagram for a query

    Input:

        query, dict: a query ready to hit the database, i.e. translated as neccessary (see translate_query())

    Outputs:

        a plotly Figure with the sankey data

        or None if there is no cooresponding data for the query
    '''

    # we do a little shaping
    if "matname" in query.keys():
        del query["matname"]

    translator = Translator(target[0]) # get a translator for the correct database
    
    # have the query get a full RUVY
    query.update({"matname__in": [
            translator.matname_translate("R"),
            translator.matname_translate("U"),
            translator.matname_translate("V"),
            translator.matname_translate("Y")
        ]})

    # get all four matrices to make the full RUVY matrix
    data = _query_database(target, query, ["matname", "i", "j", "value"])

    # get foreign keys from the query results
    foreign_keys = set(row[1] for row in data).union(row[2] for row in data)

    # if no cooresponding data, return as such
    # TODO: would probably be better to raise an exception
    if not data:
        return (None, None, None)

    # get needed orderings from the db
    index_records = Index.objects.filter(IndexID__in=foreign_keys).values("Index", "SankeyColumn")
    sankey_orders = {record["Index"]: record["SankeyColumn"] for record in index_records}

    # normalize the values of sankey_orders to remove "empty" columns
    unique_columns = set(sorted(sankey_orders.values()))
    column_mapping = {old: new for new, old in enumerate(unique_columns)}
    sankey_orders = {key: column_mapping[value] for key, value in sankey_orders.items()}
    max_columns = max(column_mapping.values()) + 1 # get how many columns the plot will have

    # get rid of any duplicate i,j,x combinations (many exist)
    data = set(data)

    # these three variables are what ultimately get json dumped
    # and sent to the javascript renderer
    nodes = [list() for _ in range(max_columns)] # n columns for the sankey diagram, found from database values
    links = list()
    options = dict(
        plot_background_color = '#f4edf7',
        default_links_opacity = 0.8,
        default_gradient_links_opacity = 0.8,
        show_column_lines = False,
        show_column_names = False,
        linear_gradient_links = False
    )

    # track node information by node name
    node_info_by_name = dict()

    # keep track of the index a new label is added to
    # this prevents having to repeatedly calculate the length of the
    # column lists
    # keys = column lists by index in nodes list above
    # values = index at which a new label will be added to a column list
    indexes_by_column = Counter()

    for matname, i, j, magnitude in data:
        readable_matname = translator.matname_translate(matname)
        
        # if R or V matrix, then the destination node must be an energy carrier, while the source node must be an industry
        # j not being the carrier inherintly means i is the carrier
        j_is_carrier = readable_matname == "R" or readable_matname == "V"

        i_name = translator.index_translate(i)
        j_name = translator.index_translate(j)

        # get the column the i (from) and j (to) nodes should go in
        try:
            from_node_info = _get_node_info(i_name, node_info_by_name)
        except KeyError:
            # if we didn't already have it, make a new node and log it in the nodes dictionary
            from_node_info = _create_new_node(i_name, node_info_by_name, indexes_by_column, sankey_orders)
            nodes[from_node_info.column].append(dict(label=i_name,
                                                     color=_get_sankey_color(i_name) or "red" if not j_is_carrier else INDUSTRY_COLOR))
            
        try:
            to_node_info = _get_node_info(j_name, node_info_by_name)
        except KeyError:
            to_node_info = _create_new_node(j_name, node_info_by_name, indexes_by_column, sankey_orders)
            nodes[to_node_info.column].append(dict(label=j_name,
                                                   color=_get_sankey_color(j_name) or "red" if j_is_carrier else INDUSTRY_COLOR))
        
        # if the column values were not filled in above
        if from_node_info.column < 0 or to_node_info.column < 0:
            raise ValueError("Unknown node name processed")

        # set up the flow from the two labels above
        links.append({"from": dict(column=from_node_info.column, node = from_node_info.index),
                      "to": dict(column=to_node_info.column, node = to_node_info.index),
                      "value": magnitude,
                      "color": _get_sankey_color(translator.index_translate(j if j_is_carrier else i))})

    # convert everything to json to send it to the javascript renderer
    return json.dumps(nodes), json.dumps(links), json.dumps(options), max_columns
