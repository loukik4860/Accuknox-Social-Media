# Generated by Django 5.0.6 on 2024-06-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("socialApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="body",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
