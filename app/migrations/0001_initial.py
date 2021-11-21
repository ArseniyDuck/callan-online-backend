# Generated by Django 3.2.4 on 2021-06-29 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOfWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('columns_count', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeWorkTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=60)),
                ('text', models.CharField(max_length=240)),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Idiom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(unique=True)),
                ('idiom_text', models.CharField(max_length=120)),
                ('explaining_text', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('answer_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_text', models.CharField(max_length=60)),
                ('translation_text', models.CharField(max_length=60)),
                ('group_of_words', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words_set', to='app.groupofwords')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words_set', to='app.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='ThemeWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=60)),
                ('group_of_words', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme_words_set', to='app.groupofwords')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rule_set', to='app.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='groupofwords',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_of_words_set', to='app.lesson'),
        ),
        migrations.CreateModel(
            name='Dictation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(unique=True)),
                ('text', models.TextField()),
                ('lesson', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dictation', to='app.lesson')),
            ],
        ),
    ]
