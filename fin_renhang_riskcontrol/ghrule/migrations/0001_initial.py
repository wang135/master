# Generated by Django 2.0 on 2020-01-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peopleinfogonghang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='客户姓名')),
                ('id_no', models.CharField(max_length=100, verbose_name='身份证号')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]