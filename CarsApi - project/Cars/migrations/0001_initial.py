# Generated by Django 3.1 on 2020-08-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model_name', models.CharField(max_length=20)),
                ('rates_counter', models.IntegerField(default=0)),
                ('total_rates', models.IntegerField(default=0)),
                ('average_rate', models.FloatField(default=0)),
            ],
        ),
    ]
