from django.contrib.admin import action as admin_action, site as admin_site
from django.contrib.auth.models import User, Permission
from django.contrib.auth.admin import UserAdmin
from django.contrib.messages import success as success_message

# fill this in later so that the database is not being accessed during the app's initialization
# TODO: maybe this should not be global
GET_IEA_PERMISSION = None

@admin_action(description="Give access to IEA data")
def allow_iea(modeladmin, request, queryset):
    """Admin action to grant IEA data access permission to selected users.
    
    This funcition adds the 'get_iea' permission to all users in the queryset/
    
    Inputs:
        modeladmin: The ModelAdmin instance
        request: The current HttpRequest
        queryset: The QuerySet containing the selected User objects
    """
    global GET_IEA_PERMISSION # tell the function to use the globally defined variable instead of a local one
    # Fetch the persmission object if it hasn't been fetched yet
    if GET_IEA_PERMISSION == None: GET_IEA_PERMISSION = Permission.objects.get(codename="get_iea")

    # Add the permission to each user in the queryset
    for u in queryset:
        u.user_permissions.add(GET_IEA_PERMISSION)

    success_message(request, "User(s) access to IEA data successfully added")

@admin_action(description="Remove access to IEA data")
def remove_iea(modeladmin, request, queryset):
    """Admin action to remove IEA data access permission to selected users.
    
    This  function removes the 'get_iea' permissions from all users in the queryset.
    
    Inputs:
        modeladmin: The ModelAdmin instance
        request: The current HttpRequest
        queryset: The QuerySet containing the selected User objects
    """
    global GET_IEA_PERMISSION # tell the function to use the globally defined variable instead of a local one
    # Fetch the persmission object if it hasn't been fetched yet
    if GET_IEA_PERMISSION == None: GET_IEA_PERMISSION = Permission.objects.get(codename="get_iea")

    # Remove the permission to each selected user
    for u in queryset:
        u.user_permissions.remove(GET_IEA_PERMISSION)

    success_message(request, "User(s) access to IEA data successfully removed")

class IEAAdmin(UserAdmin):
    """ Custom UserAdmin class that includes actions for managing IEA data access."""
    actions = [allow_iea, remove_iea] # this needs to be a list or there will be an error when Django looks for allow_iea()

# Change User model manager that with the IEA changing action
admin_site.unregister(User)
admin_site.register(User, IEAAdmin)