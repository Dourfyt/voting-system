# Generated by Django 5.0.3 on 2024-03-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userd',
            name='mob_num',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
