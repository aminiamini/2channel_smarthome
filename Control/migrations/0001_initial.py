# Generated by Django 5.1.3 on 2024-11-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LED_States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LED1', models.BooleanField()),
                ('LED2', models.BooleanField()),
            ],
        ),
    ]
