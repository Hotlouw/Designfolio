# Generated by Django 5.0.1 on 2024-01-27 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle', '0008_otherlibrary_other'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherlibrary',
            name='category',
        ),
    ]
