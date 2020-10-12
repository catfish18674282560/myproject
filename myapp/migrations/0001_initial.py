# Generated by Django 3.1.1 on 2020-09-26 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='书名')),
            ],
            options={
                'verbose_name': '书籍',
                'verbose_name_plural': '书籍',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('content', models.TextField(verbose_name='正文')),
                ('status', models.CharField(choices=[('draft', '草稿'), ('published', '发布中')], default='draft', max_length=10, verbose_name='文章状态')),
                ('priority', models.IntegerField(default=0, verbose_name='优先级')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='myapp.book', verbose_name='书名')),
            ],
            options={
                'verbose_name': '文章列表',
                'verbose_name_plural': '文章列表',
                'ordering': ('-priority',),
            },
        ),
    ]
