# Generated by Django 2.0.2 on 2018-02-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('hostname', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='hostname')),
                ('is_available', models.BooleanField(default=True, verbose_name='is_available')),
                ('locking_user', models.CharField(blank=True, max_length=256, verbose_name='locking_user')),
            ],
        ),
    ]