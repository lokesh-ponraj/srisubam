# Generated by Django 3.2.12 on 2023-06-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0004_auto_20230606_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
