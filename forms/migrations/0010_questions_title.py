# Generated by Django 2.2 on 2021-02-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_auto_20210220_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='title',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
