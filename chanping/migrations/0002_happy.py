# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chanping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Happy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('man', models.CharField(max_length=100, verbose_name='\u59d3\u540d\uff08\u7537\uff09')),
                ('human', models.CharField(max_length=100, verbose_name='\u59d3\u540d\uff08\u5973\uff09')),
                ('mettingtime', models.DateTimeField(verbose_name='\u9047\u89c1\u65f6\u95f4')),
                ('pwd', models.CharField(max_length=100, verbose_name='\u79d8\u94a5')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
