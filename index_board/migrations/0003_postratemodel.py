# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_board', '0002_auto_20150423_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostRateModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('date', models.DateTimeField()),
                ('type', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
