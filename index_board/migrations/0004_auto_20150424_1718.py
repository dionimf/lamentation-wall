# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_board', '0003_postratemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lamentmodel',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
