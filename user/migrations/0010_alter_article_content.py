# Generated by Django 4.2.3 on 2024-06-05 21:23

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]