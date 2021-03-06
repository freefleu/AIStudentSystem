# Generated by Django 2.1.4 on 2019-03-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cour_id', models.CharField(max_length=10, unique=True)),
                ('cour_name', models.CharField(max_length=20)),
                ('cour_teacher', models.CharField(max_length=20)),
                ('cour_timeplace', models.CharField(max_length=30)),
                ('cour_college', models.CharField(max_length=20)),
                ('cour_stunum', models.IntegerField()),
                ('cour_score', models.FloatField()),
                ('cour_avescore', models.FloatField()),
                ('cour_failrate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Courseselection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sel_time', models.DateTimeField()),
                ('sel_score', models.FloatField()),
                ('sel_grade', models.FloatField()),
                ('sel_cour', models.ForeignKey(on_delete='CASCADE', related_name='courseset', to='assistantmodel.Course', to_field='cour_id')),
            ],
        ),
        
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=10, unique=True)),
                ('stu_name', models.CharField(max_length=20)),
                ('stu_password', models.CharField(max_length=20)),
                ('stu_gender', models.CharField(max_length=2)),
                ('stu_college', models.CharField(max_length=20)),
                ('stu_label1', models.BooleanField()),
                ('stu_label2', models.BooleanField()),
                ('stu_label3', models.BooleanField()),
                ('stu_label4', models.BooleanField()),
                ('stu_label5', models.BooleanField()),
                ('stu_label6', models.BooleanField()),
            ],
        ),
       
        migrations.AddField(
            model_name='courseselection',
            name='sel_stu',
            field=models.ForeignKey(on_delete='CASCADE', related_name='studentset', to='assistantmodel.Student', to_field='stu_id'),
        ),
    ]
