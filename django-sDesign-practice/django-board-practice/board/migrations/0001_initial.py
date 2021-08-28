# Generated by Django 3.1.2 on 2020-10-24 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fc_user', '0003_auto_20201021_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='작성시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fc_user.fc_user', verbose_name='작성자')),
            ],
        ),
    ]
