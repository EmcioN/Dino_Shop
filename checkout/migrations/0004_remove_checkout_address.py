# Generated by Django 4.2.7 on 2023-12-02 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_checkout_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='address',
        ),
    ]
