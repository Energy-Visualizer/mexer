class DatabaseRouter:
    """ A database router to control database operations on models
    
    This router directs database operations for authentication and 
    user-specific models to a specific database.
    """

    # Django's authorization/authentication apps
    AUTH_APPS = ["auth", "sessions", "contenttypes", "admin"]

    # Models to go to the Users DB
    USERS_DB_MODEL_NAMES = ["EvizUser", "EmailAuthCode", "PassResetCode"]

    # Contains every app name that should be routed to the Users db 
    ALL_USERS_APPS = AUTH_APPS + ["captcha"]

    # Contains every model that should be routed to the Users db 
    ALL_USERS_MODELS = USERS_DB_MODEL_NAMES

    def db_for_read(self, model, **hints):
        """ Database for read operations."""

        # everything for user auth
        if model._meta.app_label in self.ALL_USERS_APPS or model.__name__ in self.ALL_USERS_MODELS:
            return "users"
        return None # None will go to default db


    def db_for_write(self, model, **hints):

        # everything for user auth
        if model._meta.app_label in self.ALL_USERS_APPS or model.__name__ in self.ALL_USERS_MODELS:
            return "users"
        return None # None will go to default db

    def allow_relations(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db != "default"
