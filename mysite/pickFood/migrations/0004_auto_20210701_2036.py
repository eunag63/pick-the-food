# Generated by Django 3.2.3 on 2021-07-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickFood', '0003_auto_20210701_2025'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Count',
        ),
        migrations.AddField(
            model_name='food',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]