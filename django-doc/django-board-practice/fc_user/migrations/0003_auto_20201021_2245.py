# Generated by Django 3.1.2 on 2020-10-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fc_user', '0002_auto_20201021_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fc_user',
            options={'verbose_name': '보더콜리단', 'verbose_name_plural': '보더콜리단'},
        ),
        migrations.AddField(
            model_name='fc_user',
            name='useremail',
            field=models.EmailField(default='wjdwjd1501@gmail.com', max_length=128, verbose_name='사용자 이메일'),
            preserve_default=False,
        ),
    ]