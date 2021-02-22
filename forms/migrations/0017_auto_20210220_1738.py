# Generated by Django 2.2 on 2021-02-20 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forms', '0016_auto_20210220_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300, null=True)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('choice_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('qusetion_name', models.CharField(max_length=250)),
                ('question_type', models.SmallIntegerField(choices=[(0, 'yesorno'), (1, 'choiceType'), (2, 'rating'), (3, 'inputType')], default=3)),
                ('required', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('choices', models.ManyToManyField(blank=True, null=True, related_name='question', to='forms.Choices')),
            ],
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('template', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('answers', models.ManyToManyField(blank=True, default=None, null=True, to='forms.Answers')),
                ('questions', models.ManyToManyField(default=None, to='forms.Questions')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Questions'),
        ),
    ]
