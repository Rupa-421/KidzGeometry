# Generated by Django 3.2.5 on 2021-08-01 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
