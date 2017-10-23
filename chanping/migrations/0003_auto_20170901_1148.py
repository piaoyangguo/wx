# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chanping', '0002_happy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pclass',
        ),
        migrations.RemoveField(
            model_name='productclass',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductClass',
        ),
    ]
