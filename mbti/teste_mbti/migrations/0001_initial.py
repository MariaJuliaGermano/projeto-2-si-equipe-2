# Generated by Django 5.1.2 on 2024-11-04 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='respostas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pergunta_1', models.TextField()),
                ('pergunta_2', models.TextField()),
                ('pergunta_3', models.TextField()),
                ('pergunta_4', models.TextField()),
            ],
        ),
    ]
