# Generated by Django 3.2.9 on 2021-11-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0003_data_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='_id',
            field=models.CharField(default='NA', max_length=500),
            preserve_default=False,
        ),
    ]