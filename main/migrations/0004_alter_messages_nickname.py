# Generated by Django 5.0.4 on 2024-04-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_messages_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='nickname',
            field=models.CharField(blank='True', default='Anonymous', max_length=10),
        ),
    ]