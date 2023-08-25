# Generated by Django 3.2.19 on 2023-08-10 23:04

from django.db import migrations
from tasks.functions import fill_predictions_project

def forward(apps, schema_editor):
    fill_predictions_project()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('tasks', '0042_auto_20230810_2304'),
    ]

    operations = [
        migrations.RunPython(forward, backwards),
    ]
