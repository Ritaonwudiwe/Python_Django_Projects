# Generated by Django 4.0.4 on 2022-06-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupant_name', models.CharField(max_length=10000)),
                ('occupant_email', models.EmailField(max_length=254)),
                ('occupant_occupation', models.CharField(max_length=10000)),
                ('room_number', models.IntegerField()),
                ('amount_paid', models.IntegerField()),
                ('number_of_rooms', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]