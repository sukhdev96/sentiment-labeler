# Generated by Django 3.2.2 on 2021-05-29 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='content',
        ),
    ]
