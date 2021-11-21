# Generated by Django 3.1.4 on 2021-07-04 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210704_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupofwords',
            options={'verbose_name_plural': 'groups of words'},
        ),
        migrations.AddField(
            model_name='idiom',
            name='example_text',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='dictation',
            name='lesson',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dictation_set', to='app.lesson'),
        ),
        migrations.AlterField(
            model_name='themeword',
            name='text',
            field=models.CharField(max_length=120),
        ),
    ]
