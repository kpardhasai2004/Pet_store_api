# Generated by Django 4.1.7 on 2023-03-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('parent', models.CharField(max_length=225)),
                ('type', models.CharField(max_length=225)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=225)),
            ],
        ),
    ]