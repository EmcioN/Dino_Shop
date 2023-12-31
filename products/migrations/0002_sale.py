# Generated by Django 4.2.7 on 2023-11-29 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('dinosaur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.dinosaur')),
            ],
        ),
    ]
