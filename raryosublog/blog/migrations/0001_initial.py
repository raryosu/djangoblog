# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
