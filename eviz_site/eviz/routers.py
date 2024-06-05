class DatabaseRouter:

    def db_for_read(self, model, **hints):

        # specifically for user db
        if model.__name__ == "User":
            return "users"
        return None # None will go to default db


    def db_for_write(self, model, **hints):

        # specifically for user db
        if model.__name__ == "User":
            return "users"
        return None # None will go to default db

    def allow_relations(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        
        return db != "default"
