# Generated by Django 3.0.7 on 2020-07-03 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField()),
                ('product_description', models.TextField()),
                ('product_price', models.TextField()),
            ],
        ),
    ]