from django.db import models

# Create your models here.
class Post(models.Model):
    # designate title with a maximum character lenght
    title = models.CharField(max_length=200)

    # designate a date and time
    pub_date = models.DateTimeField()

    # post text
    text = models.TextField()