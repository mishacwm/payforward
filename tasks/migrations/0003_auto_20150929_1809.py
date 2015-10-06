# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150929_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tag',
            field=models.ManyToManyField(related_name='tasks', verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xb3\xd0\xb8', to='tasks.Tag'),
        ),
    ]
