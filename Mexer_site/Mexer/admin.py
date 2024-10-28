from django.contrib.admin import action as admin_action, site as admin_site
from Mexer.models import EvizUser
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin
from django.contrib.messages import success as success_message
from utils.logging import LOGGER

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
        LOGGER.info(f"User {u.username} granted IEA permissions")

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
        LOGGER.info(f"User {u.username} IEA permissions revoked")

    success_message(request, "User(s) access to IEA data successfully removed")

class IEAAdmin(UserAdmin):
    """ Custom UserAdmin class that includes actions for managing IEA data access."""
    actions = [allow_iea, remove_iea] # this needs to be a list or there will be an error when Django looks for allow_iea()
    list_display = (
        "username", "iea_approved", "email", "is_staff", "country", 
        "institution_name", "last_login")

    def iea_approved(self, obj: EvizUser) -> bool:
        """Determine if a user has IEA permissions."""
        return obj.has_perm("Mexer.get_iea")
    iea_approved.boolean = True # to show it as a checkmark / x symbol

# Register controls what shows up on the admin page
# so any user who has permissions related to the EvizUser model
# has IEAAdmin permissions, if they are also staff
admin_site.register(EvizUser, IEAAdmin)

from Mexer.models import EmailAuthCode, PassResetCode
admin_site.register((EmailAuthCode, PassResetCode))
