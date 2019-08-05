# Generated by Django 2.2 on 2019-08-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=1000)),
                ('money', models.IntegerField()),
                ('buy_date', models.DateField()),
            ],
        ),
    ]
