# Generated by Django 3.1.3 on 2023-04-06 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230406_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='course',
        ),
        migrations.AddField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson'),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200),
        ),
    ]