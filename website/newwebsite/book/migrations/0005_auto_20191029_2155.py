# Generated by Django 2.2.6 on 2019-10-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20191028_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_deleted',
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='student',
            name='introduce',
            field=models.TextField(verbose_name='介绍'),
        ),
    ]