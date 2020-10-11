from django.db import models
from django.utils import timezone

class Post(models.Model):
    title=models.CharField(max_length=150,db_index=True)
    username=models.SlugField(max_length=150,unique=True)
    post=models.TextField(db_index=True)
    date_pub=models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.date_pub=timezone.now()
        self.save()
    def __str__(self):
        return'{}'.format(self.title)
