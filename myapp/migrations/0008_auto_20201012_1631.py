# Generated by Django 3.1.1 on 2020-10-12 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='是否显示出来'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='QQ',
            field=models.IntegerField(verbose_name='QQ'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='myapp.article', verbose_name='博客'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ip',
            field=models.CharField(max_length=255, verbose_name='客户端ip地址'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=20, verbose_name='用户名'),
        ),
    ]
