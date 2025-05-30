# Generated by Django 1.11.16 on 2018-11-06 23:12
from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("projects", "0031_add_modified_date_importedfile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webhook",
            name="url",
            field=models.URLField(
                blank=True, help_text="URL to send the webhook to", max_length=600
            ),
        ),
    ]
