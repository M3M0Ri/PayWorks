# Generated by Django 4.2 on 2023-04-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_jobpost_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='data',
            new_name='date',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='expiry',
            field=models.DateField(null=True),
        ),
    ]