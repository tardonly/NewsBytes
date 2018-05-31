from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    buddy = models.CharField(max_length=40,default="default_buddy")
    creator= models.CharField(max_length=40,default="admin")

    def __str__(self):
        return self.text