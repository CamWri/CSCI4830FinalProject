# Generated by Django 5.0.4 on 2024-04-07 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_coresubject_test_remove_ticket_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.course'),
        ),
    ]