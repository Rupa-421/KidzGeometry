# Generated by Django 3.2.5 on 2021-07-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('des', models.TextField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
    ]
