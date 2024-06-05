class DatabaseRouter:

    def db_for_read(self, model, **hints):

        # everything for user auth
        if model._meta.app_label in ["auth", "sessions"]:
            return "users"
        return None # None will go to default db


    def db_for_write(self, model, **hints):

        # everything for user auth
        if model._meta.app_label in ["auth", "sessions"]:
            return "users"
        return None # None will go to default db

    def allow_relations(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        
        return db != "default"
