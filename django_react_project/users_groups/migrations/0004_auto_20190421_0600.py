# Generated by Django 2.2 on 2019-04-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_groups', '0003_users_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]