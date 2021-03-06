# Generated by Django 2.1.4 on 2018-12-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('size', models.IntegerField()),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('mk_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LoginID', models.CharField(max_length=20)),
                ('PassWord', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=10)),
                ('Sex', models.BooleanField(default=True)),
                ('EmailAdd', models.CharField(default='', max_length=30)),
                ('TelNum', models.IntegerField(default=-1)),
                ('Birthday', models.DateField(max_length=20, null=True)),
                ('JoinTime', models.DateField()),
                ('LessonCover', models.IntegerField(default=0)),
            ],
        ),
    ]
