# Generated by Django 5.0.3 on 2024-03-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=30)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'tblstudent',
            },
        ),
    ]
