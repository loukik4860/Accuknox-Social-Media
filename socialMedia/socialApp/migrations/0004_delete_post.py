# Generated by Django 5.0.6 on 2024-06-27 05:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("socialApp", "0003_friendrequest"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Post",
        ),
    ]