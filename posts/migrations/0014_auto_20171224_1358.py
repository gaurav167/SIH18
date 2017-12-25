# Generated by Django 2.0 on 2017-12-24 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20170608_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('likes', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Category'),
        ),
    ]
