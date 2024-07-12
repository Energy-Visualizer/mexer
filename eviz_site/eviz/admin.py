from django.contrib.admin import action as admin_action, site as admin_site
from django.contrib.auth.models import User, Permission
from django.contrib.auth.admin import UserAdmin
from django.contrib.messages import success as success_message

# fill this in later so that the database is not being accessed during the app's initialization
GET_IEA_PERMISSION = None

@admin_action(description="Give access to IEA data")
def allow_iea(modeladmin, request, queryset):
    global GET_IEA_PERMISSION # tell the function to use the globally defined variable instead of a local one
    if GET_IEA_PERMISSION is None: GET_IEA_PERMISSION = Permission.objects.get(codename="get_iea")

    for u in queryset:
        u.user_permissions.add(GET_IEA_PERMISSION)

    success_message(request, "User(s) access to IEA data successfully added")

@admin_action(description="Remove access to IEA data")
def remove_iea(modeladmin, request, queryset):
    global GET_IEA_PERMISSION # tell the function to use the globally defined variable instead of a local one
    if GET_IEA_PERMISSION is None: GET_IEA_PERMISSION = Permission.objects.get(codename="get_iea")

    for u in queryset:
        u.user_permissions.remove(GET_IEA_PERMISSION)

    success_message(request, "User(s) access to IEA data successfully removed")

class IEAAdmin(UserAdmin):
    actions = [allow_iea, remove_iea] # this needs to be a list or there will be an error when Django looks for allow_iea()

# Change User model manager that with the IEA changing action
admin_site.unregister(User)
admin_site.register(User, IEAAdmin)