# Generated by Django 4.0 on 2022-01-07 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('Sc', 'Science'), ('Art', 'Arts'), ('Cmc', 'commerce'), ('Math', 'Maths')], default='Maths', max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tackle_api.student')),
            ],
        ),
    ]