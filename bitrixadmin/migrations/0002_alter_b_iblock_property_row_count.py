# Generated by Django 3.2.4 on 2021-06-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitrixadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b_iblock_property',
            name='row_count',
            field=models.IntegerField(default=1),
        ),
    ]
