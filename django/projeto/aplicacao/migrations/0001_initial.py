# Generated by Django 2.2.14 on 2020-07-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetName', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('complement', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('neighbourhood', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
                ('latitude', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
    ]
