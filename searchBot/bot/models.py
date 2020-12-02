from django.db import models

# Create your models here.

class SaveSearch(models.Model):
    """
    To save searches by users
    """
    author = models.CharField()
    keyword = models.CharField()
    created_at = models.DateTimeField(auto_now=True)