# Generated by Django 3.2 on 2023-09-04 15:24

from django.db import migrations, models
import sms.models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sms',
            options={'verbose_name': 'SMS', 'verbose_name_plural': 'SMS'},
        ),
        migrations.AlterModelOptions(
            name='smssettings',
            options={'verbose_name': 'SMS Configuration', 'verbose_name_plural': 'SMS Configurations'},
        ),
        migrations.AddField(
            model_name='sms',
            name='response',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='sms',
            name='sent',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='sms',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[sms.models.format_phone_number]),
        ),
    ]
