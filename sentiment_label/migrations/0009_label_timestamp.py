# Generated by Django 3.2.3 on 2021-06-11 09:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment_label', '0008_post_no_of_labels'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]