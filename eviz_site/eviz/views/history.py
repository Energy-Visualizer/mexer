####################################################################
# history.py includes all the views for managing a user's plot history
# 
# Includes views to
# Render a user's history cookie as HTML
# Delete a history entry
#
# For more history functionality, see utils/history.py
# 
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu 
#####################
from utils.history import get_user_history, get_history_html
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from eviz.views.error_pages import *
import pickle

def render_history(request):
    """
    Render the user's plot history as HTML.
    
    This function retrieves the user's plot history from cookies
    and formats it as HTML buttons with delete functionality for each item.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: An HTTP response containing the HTML representation of the user's plot history.
    """
    # Retrieve the user's plot history from cookies
    user_history = get_user_history(request)
    history_html = get_history_html(user_history)
    return HttpResponse(history_html)

@csrf_exempt
@require_POST
def delete_history_item(request):
    """
    Delete a specific item from the user's plot history.
    
    This function handles POST requests to delete a history item.
    It updates the user's history cookie after deletion.
    
    Inputs:
        request: The HTTP request object containing the index of the item to delete.
    
    Outputs:
        HttpResponse: A response containing the updated history HTML or an error message.
    """
    
    if request.method == "POST":
        # Get the index of the item to delete from the POST data
        index = int(request.POST.get('index', -1))
        
        if index < 0: return error_400(request, "Bad history index")
        
        # Retrieve the current user history
        user_history = get_user_history(request)
        
        # Check if the index is valid
        if 0 > index >= len(user_history): return error_400(request, "Bad history index for user history received")

        # Remove the item at the specified index
        del user_history[index]
        
        # Serialize the updated history
        serialized_data = pickle.dumps(user_history)
        
        if user_history:
            # If there are still items in the history, render them
            response = HttpResponse(get_history_html(user_history))
        else:
            # If the history is now empty, return a message
            response = HttpResponse('<p>No history available.</p>')
        
        # Update the user's history cookie
        response.set_cookie('user_history', serialized_data.hex(), max_age=30 * 24 * 60 * 60)
        
        return response
    
    # Return an error response if the request is invalid
    return error_400(request, "")