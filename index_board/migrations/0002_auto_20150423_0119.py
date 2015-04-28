# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lamentmodel',
            name='text',
            field=models.TextField(max_length=300),
        ),
    ]
