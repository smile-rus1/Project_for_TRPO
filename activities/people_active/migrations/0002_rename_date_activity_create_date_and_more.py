# Generated by Django 4.1.2 on 2023-01-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people_active', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='date',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='activity',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]