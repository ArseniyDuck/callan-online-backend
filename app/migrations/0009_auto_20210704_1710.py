# Generated by Django 3.1.4 on 2021-07-04 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210704_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictation',
            name='content_id',
        ),
        migrations.AlterField(
            model_name='idiom',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idioms_set', to='app.lesson'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules_set', to='app.lesson'),
        ),
    ]