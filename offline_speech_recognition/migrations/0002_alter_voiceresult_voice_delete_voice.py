# Generated by Django 4.2.4 on 2023-10-01 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voice_manager', '0001_initial'),
        ('offline_speech_recognition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiceresult',
            name='voice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voice_manager.voice'),
        ),
        migrations.DeleteModel(
            name='Voice',
        ),
    ]
