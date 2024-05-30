from locust import HttpUser, task, between

class EvizUser(HttpUser):
    wait_time = between(1, 5)
    def load_main_page(self):
        self.client.get("/")