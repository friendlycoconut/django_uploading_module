# Generated by Django 2.1.3 on 2019-12-02 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191202_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='url',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]