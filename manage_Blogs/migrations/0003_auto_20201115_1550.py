# Generated by Django 3.1.3 on 2020-11-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_Blogs', '0002_auto_20201115_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='edited_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
