# Generated by Django 4.2.3 on 2023-07-13 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visiters', '0005_count_remove_visiter_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Count',
        ),
    ]
