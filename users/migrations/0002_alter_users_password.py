# Generated by Django 5.0.6 on 2024-06-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="password",
            field=models.CharField(max_length=250),
        ),
    ]