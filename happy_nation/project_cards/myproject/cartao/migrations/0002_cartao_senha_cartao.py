# Generated by Django 5.1.7 on 2025-03-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartao',
            name='senha_cartao',
            field=models.CharField(default='senha_padrao', max_length=100),
        ),
    ]
