# Generated by Django 4.2.3 on 2023-07-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_remove_ticket_interests_ticket_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='interest',
        ),
        migrations.AddField(
            model_name='ticket',
            name='interests',
            field=models.TextField(blank=True, null=True),
        ),
    ]
