# Generated by Django 2.1.4 on 2018-12-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
