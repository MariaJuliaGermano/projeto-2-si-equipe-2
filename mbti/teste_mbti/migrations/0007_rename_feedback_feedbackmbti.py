# Generated by Django 5.1.2 on 2024-11-25 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_mbti', '0002_cadastro_curso'),
        ('teste_mbti', '0006_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='feedback',
            new_name='feedbackmbti',
        ),
    ]
