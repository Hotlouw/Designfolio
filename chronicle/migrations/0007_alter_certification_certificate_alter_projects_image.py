# Generated by Django 5.0.1 on 2024-01-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle', '0006_alter_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
