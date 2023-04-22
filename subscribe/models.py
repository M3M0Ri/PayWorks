from django.db import models

NEWLETTER_OPTION = [
    ("W", "weekly"),
    ("M", "monthly")
]


class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    option = models.CharField(max_length=2, choices=NEWLETTER_OPTION)

    def __str__(self):
        return f"{self.first_name} ->  {self.email}"
