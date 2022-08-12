# Generated by Django 4.0.6 on 2022-08-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.CharField(max_length=30)),
                ('businessNum', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('bsName', models.CharField(max_length=100)),
                ('repName', models.CharField(max_length=12)),
                ('birth', models.IntegerField()),
                ('phoneNum', models.IntegerField()),
                ('address', models.TextField()),
                ('registeration', models.ImageField(upload_to='')),
                ('report', models.ImageField(upload_to='')),
            ],
        ),
    ]
