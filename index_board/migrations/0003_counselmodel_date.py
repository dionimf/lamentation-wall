# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_board', '0002_auto_20150501_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='counselmodel',
            name='date',
            field=models.DateField(default='2015-01-01'),
            preserve_default=False,
        ),
    ]
