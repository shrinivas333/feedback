# Generated by Django 2.2 on 2021-02-16 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20210213_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='choices',
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]