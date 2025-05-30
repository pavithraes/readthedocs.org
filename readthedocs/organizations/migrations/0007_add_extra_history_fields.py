# Generated by Django 2.2.24 on 2021-09-29 19:27
from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("organizations", "0006_add_assets_cleaned"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalorganization",
            name="extra_history_browser",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Browser user-agent"
            ),
        ),
        migrations.AddField(
            model_name="historicalorganization",
            name="extra_history_ip",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="IP address"
            ),
        ),
        migrations.AddField(
            model_name="historicalteam",
            name="extra_history_browser",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="Browser user-agent"
            ),
        ),
        migrations.AddField(
            model_name="historicalteam",
            name="extra_history_ip",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="IP address"
            ),
        ),
    ]
