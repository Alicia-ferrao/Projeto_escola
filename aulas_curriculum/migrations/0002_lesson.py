# Generated by Django 2.2.9 on 2022-06-06 21:02

import aulas_curriculum.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aulas_curriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Chapter no.')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=aulas_curriculum.models.save_lesson_files, verbose_name='Video')),
                ('ppt', models.FileField(blank=True, upload_to=aulas_curriculum.models.save_lesson_files, verbose_name='Presentations')),
                ('Notes', models.FileField(blank=True, upload_to=aulas_curriculum.models.save_lesson_files, verbose_name='Notes')),
                ('Standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas_curriculum.Standard')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='aulas_curriculum.Subject')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
