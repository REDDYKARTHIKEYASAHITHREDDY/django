# Generated by Django 5.0.4 on 2024-04-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_course_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]