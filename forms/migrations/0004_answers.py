# Generated by Django 2.2 on 2021-02-12 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0003_auto_20210210_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300, null=True)),
                ('question_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='forms.Questions')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]