####################################################################
# xy_plot.py contains the functions to create... xy plots
#
# Given the query and some plotting information, it will put 
# together a plotly Figure object, which can then be turned 
# into HTML or further modified.
#
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu 
#####################
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from utils.data import get_translated_dataframe, DatabaseTarget

def get_xy(efficiency_metric: str, target: DatabaseTarget, query: dict,
           color_by: str, line_by: str, facet_col_by: str = None, facet_row_by: str = None, energy_type: str = None) -> go.Figure:
    """ Generate a line plot based on the given efficiency metric and query parameters.

    Inputs:
        efficiency_metric: The efficiency metric to plot on the y-axis.
        query: A dictionary containing filter parameters for the database query.
        color_by: The field to use for coloring the lines.
        line_by: The field to use for line dash styles.
        facet_col_by: The field to use for faceting columns.
        facet_row_by: The field to use for faceting rows.
        energy_type: The type of energy (Energy, Exergy, or both) for y-axis label.

    Outputs:
        go.Figure: A Plotly figure object containing the generated plot.
    """

    # Create a list of fields to select, always including 'Year' and the efficiency metric
    fields_to_select = ["Year", efficiency_metric]

    # Map the names to the actual database field names
    field_mapping = {
        'country': 'Country',
        'energy_type': 'EnergyType'
    }
    
    # Add color_by, line_by, facet_col_by, and facet_row_by fields to the selection list
    for field in {color_by, line_by, facet_col_by, facet_row_by}:
        if field in field_mapping:
            fields_to_select.append(field_mapping[field])

    # get the respective data from the database
    df = get_translated_dataframe(target, query, fields_to_select)
        
    
    if df.empty: return None # if no data, return as such

    # convert year column to datetime if present
    # and sort on that so that the xy plots come out right
    df["Year"] = pd.to_datetime(df["Year"], format="%Y")
    df = df.sort_values(by="Year")
    
    try:
        # Create the line plot using Plotly Express
        fig = px.line(
            df, x="Year", y=efficiency_metric, 
            color=field_mapping.get(color_by),
            line_dash=field_mapping.get(line_by),
            facet_col=field_mapping.get(facet_col_by),
            facet_row=field_mapping.get(facet_row_by),
            facet_col_spacing=0.05,
            category_orders={"EnergyType": ["Energy", "Exergy"]},
        )
        
        # Set the y-axis title based on the energy type
        if 'Energy' in energy_type and 'Exergy' in energy_type:
            y_title = f"EX<sub>{efficiency_metric[-1]}</sub> [TJ]"
        elif energy_type == 'Exergy':
            y_title = f"X<sub>{efficiency_metric[-1]}</sub> [TJ]"
        elif energy_type == 'Energy':
            y_title = f"E<sub>{efficiency_metric[-1]}</sub> [TJ]"
        else:
            y_title = efficiency_metric

        # Update layout with axis lines
        fig.update_xaxes(
            showgrid=False,
            zeroline=False,
            ticklen=10,
            ticks="inside",
            title=None,
            linecolor='black',
            linewidth=1,
            mirror=False
        )
        fig.update_yaxes(
            showgrid=False,
            zeroline=False,
            ticklen=10,
            ticks="inside",
            title=y_title,
            linecolor='black',
            linewidth=1,
            mirror=False,
            showticklabels=True
        )

        # Force x-axis to bottom and y-axis to left for all subplots (used because of faceting)
        fig.update_xaxes(position=0)
        fig.update_yaxes(position=0)

        # Update overall layout
        fig.update_layout(
            plot_bgcolor="white",
            showlegend=True,
            margin=dict(l=50, r=50, t=50, b=50),
        )
        
        # Remove y-axis titles for all but the first column when using facet columns
        if facet_col_by:
            for i in range(2, len(fig.data) + 1):
                fig.update_yaxes(title_text="", col=i)

        return fig
    
    except Exception as e:
        # Return a message if plot fails.
        return go.Figure().add_annotation(text=f"Error creating plot: {str(e)}", showarrow=False)