# Generated by Django 3.1.2 on 2020-12-11 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentHelper', '0009_auto_20201128_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('course_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='studentHelper.course')),
                ('form', models.CharField(choices=[('ACTIV', 'aktywność'), ('EXAM', 'egzamin'), ('QUIZ', 'kartkówka'), ('TEST', 'kolokwium'), ('LIST', 'lista zadań')], max_length=5)),
                ('weight', models.FloatField()),
                ('type', models.CharField(choices=[('POINT', 'punkty'), ('MARK', 'ocena'), ('PERC', 'procent')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='CourseGroup',
            fields=[
                ('course_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='studentHelper.course')),
                ('weight', models.FloatField()),
                ('minimum', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Modyfication',
            fields=[
                ('course_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='studentHelper.course')),
                ('mod', models.CharField(choices=[('MINUS', '-'), ('PLUS', '+')], max_length=5)),
                ('val', models.FloatField()),
                ('type', models.CharField(choices=[('POINT', 'punkty'), ('MARK', 'ocena'), ('PERC', 'procent')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Thresholds',
            fields=[
                ('course_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='studentHelper.course')),
                ('p_2_0', models.FloatField()),
                ('k_2_0', models.FloatField()),
                ('p_2_5', models.FloatField()),
                ('k_2_5', models.FloatField()),
                ('p_3_0', models.FloatField()),
                ('k_3_0', models.FloatField()),
                ('p_3_5', models.FloatField()),
                ('k_3_5', models.FloatField()),
                ('p_4_0', models.FloatField()),
                ('k_4_0', models.FloatField()),
                ('p_4_5', models.FloatField()),
                ('k_4_5', models.FloatField()),
                ('p_5_0', models.FloatField()),
                ('k_5_0', models.FloatField()),
                ('p_5_5', models.FloatField()),
                ('k_5_5', models.FloatField()),
                ('type', models.CharField(choices=[('POINT', 'punkty'), ('MARK', 'ocena'), ('PERC', 'procent')], max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Rules',
        ),
    ]