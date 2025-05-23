# Generated by Django 2.2.10 on 2020-05-26 14:34
from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("projects", "0050_migrate_external_builds"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="urlconf",
            field=models.CharField(
                default=None,
                help_text="Supports the following keys: $language, $version, $subproject, $filename. An example: `$language/$version/$filename`.",
                max_length=255,
                null=True,
                verbose_name="Documentation URL Configuration",
            ),
        ),
    ]
