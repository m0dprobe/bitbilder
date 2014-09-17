# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitbilder', '0003_auto_20140911_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bit',
            name='bitname',
            field=models.CharField(max_length=50, unique=True, verbose_name='Bit-Name'),
        ),
    ]
