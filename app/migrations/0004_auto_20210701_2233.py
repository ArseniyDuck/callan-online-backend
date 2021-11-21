# Generated by Django 3.1.4 on 2021-07-01 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210629_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='group_of_words',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='words_set', to='app.groupofwords'),
        ),
        migrations.AlterField(
            model_name='word',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words_set', to='app.lesson'),
        ),
    ]