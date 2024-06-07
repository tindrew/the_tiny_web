from django.db import models
from django.urls import reverse
from django import forms
from account.models import CustomUser
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify




class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Create a property that returns the markdown 
    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def get_absolute_url(self):
        return reverse('user-articles', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
    
    user = models.ForeignKey(CustomUser, max_length=10, on_delete=models.CASCADE, null=True)


