# Generated by Django 3.2.3 on 2021-07-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickFood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=0)),
            ],
        ),
    ]
