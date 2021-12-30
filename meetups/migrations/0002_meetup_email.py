# Generated by Django 4.0 on 2021-12-30 00:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]