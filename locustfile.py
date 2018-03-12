from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        pass

    @task(2)
    def index(self):
        self.client.get("/")
    
    @task(1)
    def advanced(self):
        self.client.get("/advanced?advanced=1&terms-0-operator=AND&terms-0-term=&terms-0-field=title&classification-physics_archives=all&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&size=25")
    
    @task(1)
    def simple(self):
        self.client.get("/?query=microprocessor&searchtype=all")
    
    @task(1)
    def author(self):
        self.client.get("/?query=ginsparg&searchtype=author")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 15000