# Generated by Django 3.2.12 on 2022-02-18 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user_avatar/%username', verbose_name='头像'),
        ),
    ]
