# Generated by Django 2.2.17 on 2020-11-30 02:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='课程名')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长（分钟）')),
                ('degree', models.CharField(choices=[('low', '初级'), ('normal', '中级'), ('high', '高级')], max_length=6, verbose_name='难度')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('category', models.CharField(default='后端开发', max_length=20, verbose_name='课程类别')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='课程标签')),
                ('youneed_know', models.CharField(default='', max_length=300, verbose_name='课程须知')),
                ('teacher_tell', models.CharField(default='', max_length=300, verbose_name='老师告诉你')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('image', models.ImageField(upload_to='course/%Y/%m', verbose_name='封面图')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='讲师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='章节名')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长（分钟）')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            options={
                'verbose_name': '课程章节',
                'verbose_name_plural': '课程章节',
            },
        ),
        migrations.CreateModel(
            name='Vedio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='视频名称')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长（分钟）')),
                ('url', models.CharField(max_length=200, verbose_name='访问地址')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='资源名称')),
                ('file', models.FileField(max_length=200, upload_to='course/resource/%Y/%m', verbose_name='下载地址')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程资源',
                'verbose_name_plural': '课程资源',
            },
        ),
    ]
