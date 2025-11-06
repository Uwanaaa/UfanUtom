from locust import HttpUser, task, between


class MailUser(HttpUser):
    wait_time = between(1,5)

    @task
    def subscribe(self):
        self.client.post('/subscribe/',json={
            "name":"Testty",
            "mail":"test@mail.com"
            })