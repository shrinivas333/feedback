# Generated by Django 2.2 on 2021-02-13 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_answers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='question_id',
            new_name='question',
        ),
    ]
