# Generated by Django 2.1.7 on 2019-03-21 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('position', models.IntegerField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('deleted', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('position', models.IntegerField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('deleted', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.Category')),
            ],
        ),
    ]
