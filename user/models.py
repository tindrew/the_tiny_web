from django.db import models
from account.models import CustomUser
from django_summernote.fields import SummernoteTextField


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = SummernoteTextField()
    # content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    user = models.ForeignKey(CustomUser, max_length=10, on_delete=models.CASCADE, null=True)
