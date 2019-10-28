# Generated by Django 2.2 on 2019-10-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_security_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField(default='')),
                ('label', models.CharField(max_length=10000)),
                ('uid', models.CharField(max_length=32, unique=True)),
            ],
        ),
    ]
