from django.db import models
from django.contrib.auth.models import User
from utils.time_helpers import utc_now

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def hours_to_now(self):
        #datetime.now needs add utc
        return(utc_now() - self.created_at).seconds  //3600

    def __str__(self):
        return f'{self.content} {self.user}:{self.content}'


# Create your models here.
