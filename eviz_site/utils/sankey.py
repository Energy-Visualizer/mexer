import json
from utils.translator import Translator
from utils.data import query_database, DatabaseTarget
from eviz_site.settings import SANKEY_COLORS_PATH
from eviz.logging import LOGGER

INDUSTRY_COLOR = "midnightblue"

with open(SANKEY_COLORS_PATH) as f:
    SANKEY_COLORS: dict[str, str] = json.loads(f.read())

def _get_sankey_color(node_name: str) -> str:
    carrier_name = -1

    for carrier_category in SANKEY_COLORS:
        if carrier_category in node_name.lower():
            carrier_name = carrier_category
            break

    return SANKEY_COLORS.get(carrier_name) or LOGGER.error("Couldn't find sankey color for " + node_name)

def _get_sankey_node_info(
        label_num: int, label_col: int,
        node_list: list[list], idx_dict: dict, label_info_dict: dict,
        translator: Translator,
        carrier: bool
):
    name = translator.index_translate(label_num)
    # try to get saved information about the label
    label_info = label_info_dict.get(label_num, -1)
    if label_info == -1:
        # add it if it is a new label and get new node_idx
        node_list[label_col].append(dict(label=name,color=_get_sankey_color(name) or "red" if carrier else INDUSTRY_COLOR))
        
        label_info = (idx_dict[label_col], label_col)
        idx_dict[label_col] += 1

        # remember which index and column the label is in so future nodes can find this one
        label_info_dict[label_num] = label_info
        node_idx = label_info[0]

    else:
        # if node is not new, just get the recorded col and idx
        label_col = label_info[1]
        node_idx = label_info[0]
    

    return node_idx, label_col

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

    translator = Translator(target[0])
    
    # have the query get a full RUVY
    query.update({"matname__in": [
            translator.matname_translate("R"),
            translator.matname_translate("U"),
            translator.matname_translate("V"),
            translator.matname_translate("Y")
        ]})

    # get all four matrices to make the full RUVY matrix
    data = query_database(target, query, ["matname", "i", "j", "x"])

    # if no cooresponding data, return as such
    if not data:
        return (None, None, None)

    # get rid of any duplicate i,j,x combinations (many exist)
    data = set(data)

    # 5 lists, one for each column in the plot
    nodes = [list(), list(), list(), list(), list()]
    links = list()
    options = dict(
        plot_background_color = '#f4edf7',
        default_links_opacity = 0.8,
        default_gradient_links_opacity = 0.8,
        show_column_lines = False,
        show_column_names = False,
        linear_gradient_links = False
    )

    # track which label is which index in the column lists
    label2info = dict()

    # keep track of the index a new label is added to
    # this prevents having to repeatedly calculate the length of the
    # column lists
    # keys = column lists by index in nodes list above
    # values = index at which a new label will be added to a column list
    idx = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

    # what columns we think the node should go in
    # filled in below

    for matname, i, j, magnitude in data:
        from_node_col = to_node_col = -1
        carrier_row = False
        carrier_col = False
        # figure out which column the info should go in
        match(translator.matname_translate(matname)):
            case("R"):
                from_node_col = 0
                to_node_col = 1
                carrier_col = True

            case("U"):
                from_node_col = 1
                to_node_col = 2
                carrier_row = True

            case("V"):
                from_node_col = 2
                to_node_col = 3
                carrier_col = True

            case("Y"):
                from_node_col = 3
                to_node_col = 4
                carrier_row = True

        # if the column values were not filled in above
        if from_node_col < 0 or to_node_col < 0:
            raise ValueError("Unknown matrix name processed")

        # get the index and column the node truely belongs in
        from_node_idx, from_node_col = _get_sankey_node_info(i, from_node_col, nodes, idx, label2info, translator, carrier_row)
        to_node_idx, to_node_col = _get_sankey_node_info(j, to_node_col, nodes, idx, label2info, translator, carrier_col)

        # set up the flow from the two labels above
        links.append({"from": dict(column=from_node_col, node = from_node_idx),
                      "to": dict(column=to_node_col, node = to_node_idx),
                      "value": magnitude,
                      "color": _get_sankey_color(translator.index_translate(i if carrier_row else j))})

    # convert everything to json to send it to the javascript renderer
    return json.dumps(nodes), json.dumps(links), json.dumps(options)