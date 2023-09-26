# Re run "python manage.py makemigrations" for any new changes here to take effect 
# "python manage.py sqlmigrate blog 0001" for showing the sql
# "python manage.py migrate" actually let the changes happen in the database
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if the user is deleted, delete their posts also

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})