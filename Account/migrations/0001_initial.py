# Generated by Django 4.2.6 on 2023-11-11 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=255)),
                ('month', models.CharField(max_length=3)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
