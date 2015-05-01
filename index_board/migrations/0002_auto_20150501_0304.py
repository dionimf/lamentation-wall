# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('index_board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LamentCriesModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('lament', models.ForeignKey(to='index_board.LamentModel')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostRateModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('date', models.DateTimeField()),
                ('type', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='lamentmodel',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='lamentmodel',
            name='text',
            field=models.TextField(max_length=300),
        ),
    ]
