# Generated by Django 5.1.3 on 2024-12-05 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_mbti', '0002_cadastro_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='arquivosExel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('arquivo', models.FileField(upload_to='documentos/')),
            ],
        ),
    ]
