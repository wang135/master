# Generated by Django 2.0 on 2020-02-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jsonss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='客户姓名')),
                ('id_no', models.CharField(max_length=100, verbose_name='身份证号')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('dict_credit_group', models.TextField(blank=True, null=True)),
                ('bl_json', models.CharField(blank=True, max_length=500, null=True)),
                ('cl_td', models.TextField(blank=True, null=True)),
                ('cl_br', models.TextField(blank=True, null=True)),
                ('df1_dict', models.TextField(blank=True, max_length=500, null=True)),
                ('score', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peopleinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='客户姓名')),
                ('id_no', models.CharField(max_length=100, verbose_name='身份证号')),
                ('cellphone', models.CharField(max_length=100, verbose_name='身份证号')),
                ('channel', models.CharField(max_length=100, verbose_name='渠道')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
