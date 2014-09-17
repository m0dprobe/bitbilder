# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitbilder', '0004_auto_20140911_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bit',
            name='license',
            field=models.CharField(choices=[('CC0 (Public Domain)', 'CC0 (Public Domain)'), ('für OE verwendbar', 'für die OE nutzbar'), ('WTFPL', 'nutzbar unter WTF PL'), ('unbekannt (aus Gründen)', 'unbekannt')], max_length=100, verbose_name='Lizenz'),
        ),
    ]
