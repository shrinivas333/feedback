# Generated by Django 2.2 on 2021-02-20 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0015_forms_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='question',
        ),
        migrations.RemoveField(
            model_name='forms',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='forms',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='choices',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
        migrations.DeleteModel(
            name='Forms',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]