# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import chanping.modelsmixin.chanping
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('name', models.CharField(max_length=100, verbose_name='\u59d3\u540d')),
                ('email', models.CharField(max_length=100, verbose_name='\u90ae\u7bb1', blank=True)),
                ('mobile', models.CharField(max_length=100, verbose_name='\u624b\u673a')),
                ('subject', models.TextField(verbose_name='\u8bf4\u660e', blank=True)),
            ],
            options={
                'verbose_name': '\u7559\u8a00',
                'verbose_name_plural': '\u7559\u8a00',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('fabuTime', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('laiyuan', models.CharField(max_length=100, verbose_name='\u6765\u6e90')),
                ('xiangqing', models.TextField(verbose_name='\u8be6\u60c5')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb',
                'verbose_name_plural': '\u65b0\u95fb',
            },
            bases=(models.Model, chanping.modelsmixin.chanping.newMixin),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('name', models.CharField(max_length=100, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('pic', models.ImageField(upload_to=b'uploads/%Y/%m/%d', verbose_name='\u4ea7\u54c1\u56fe\u7247')),
                ('guige', models.CharField(max_length=100, verbose_name='\u4ea7\u54c1\u89c4\u683c')),
                ('price', models.FloatField(max_length=100, verbose_name='\u4ea7\u54c1\u4ef7\u683c')),
                ('publicTime', models.DateField(null=True, verbose_name='\u51fa\u7248\u65f6\u95f4', blank=True)),
                ('shuoming', models.CharField(max_length=100, null=True, verbose_name='\u4ea7\u54c1\u8bf4\u660e', blank=True)),
                ('jianjie', ckeditor.fields.RichTextField(verbose_name='\u4ea7\u54c1\u7b80\u4ecb')),
                ('shunxu', models.CharField(default=b'99', max_length=100, verbose_name='\u4ea7\u54c1\u987a\u5e8f', db_index=True)),
                ('introduce', models.CharField(default=b'0', max_length=100, verbose_name='\u662f\u5426\u63a8\u8350', choices=[('1', '\u662f'), ('0', '\u5426')])),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1',
                'verbose_name_plural': '\u4ea7\u54c1',
            },
            bases=(models.Model, chanping.modelsmixin.chanping.productMixin),
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(verbose_name='\u7236\u7c7b', blank=True, to='chanping.ProductClass', null=True)),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u5206\u7c7b',
                'verbose_name_plural': '\u4ea7\u54c1\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='pclass',
            field=models.ForeignKey(related_name='product', verbose_name='\u4ea7\u54c1\u7c7b\u522b', to='chanping.ProductClass'),
        ),
    ]
