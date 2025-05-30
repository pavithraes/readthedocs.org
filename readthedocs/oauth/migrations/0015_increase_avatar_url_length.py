# Generated by Django 2.2.24 on 2021-09-07 13:30
from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("oauth", "0014_remove_remoterepository_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remoteorganization",
            name="avatar_url",
            field=models.URLField(
                blank=True, max_length=255, null=True, verbose_name="Avatar image URL"
            ),
        ),
        migrations.AlterField(
            model_name="remoterepository",
            name="avatar_url",
            field=models.URLField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Owner avatar image URL",
            ),
        ),
    ]
