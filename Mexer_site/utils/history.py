####################################################################
# history.py includes all functions related to user history
# 
# A user's plotting history is represented as a queue of dictionaries
# The dictionaries are previous queries
# The queue (really a list, but treated like a queue) stores
# MAX_HISTORY number of previous queries in it
#
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu 
#####################
import pickle
import json

# Maximum number of items to keep in the user's history
# Can't be too big because too many in history
# Will overflow the cookie size limit
MAX_HISTORY = 5

def get_user_history(request) -> list:
    """Retrieve the user's plot history from cookies.

    Inputs:
        request: The HTTP request object containing cookies.

    Outputs:
        list: The user's plot history, or an empty list if no history exists.
    """
    # Get the serialized user history from cookies
    serialized_data = request.COOKIES.get('user_history')

    if serialized_data:
        user_history = pickle.loads(bytes.fromhex(serialized_data)) # Deserialize the data if it exists
    else:
        user_history = list() # Return an empty list if no history exists

    return user_history

def update_user_history(request, plot_type, query):
    """Update the user's plot history with a new plot query.

    Inputs:
        request: The HTTP request object.
        plot_type (str): The type of plot being added to the history.
        query (dict): The query parameters for the plot.

    Outputs:
        bytes: Serialized updated user history.
    """
    # Get the current user history
    user_history = get_user_history(request)

    # Create a dictionary with the new history data
    history_data = {
        'plot_type': plot_type,
        **query
    }

    # Check if user_history is not empty
    if user_history:

        # if query is already in history, remove it to move it to the top
        try:
            user_history.remove(history_data)
        except ValueError: pass # don't care if not in, trying to remove anyways

        user_history.insert(0, history_data) # finally, add the new query to the top of the history

        # if the queue (list) is full, take the end off
        if len(user_history) > MAX_HISTORY: user_history.pop()

    else:
        # If user_history is empty, append the new history_data
        user_history.append(history_data)

    # Serialize the updated user history
    serialized_data = pickle.dumps(user_history)
    return serialized_data

from django.urls import reverse
def get_history_html(user_history: list[dict]) -> str:
    history_html = ''
    
    if user_history:
        # Iterate through each history item and create HTML buttons
        for index, history_item in enumerate(user_history):
            # Create HTML for each history item, including plot and delete buttons
            history_html += f'''
            <div class="history-item">
                <button type="button" 
                    hx-vals='{json.dumps(history_item)}' 
                    hx-indicator="#plot-spinner" 
                    hx-post="/plot" 
                    hx-target="#plot-section" 
                    hx-swap="innerHTML" 
                    onclick='document.getElementById("plot-section").scrollIntoView();' 
                    class="history-button">
                    Plot Type: {history_item["plot_type"].capitalize()}<br>
                    Dataset: {history_item["dataset"]}<br>
                    Country: {history_item["country"]}
                </button>
                <button class="delete-history" 
                    hx-post="{reverse('delete_history_item')}" 
                    hx-vals='{{"index": {index}}}' 
                    hx-target="#history-list" 
                    hx-swap="innerHTML">
                    <i class="fas fa-trash-alt"></i>
                </button>
            </div><br>
            '''
    else:
        # If no history is available, display a message
        history_html = '<p>No history available.</p>'

    return history_html