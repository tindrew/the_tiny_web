from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin




from . models import CustomUser

admin.site.register(CustomUser,  MarkdownxModelAdmin)