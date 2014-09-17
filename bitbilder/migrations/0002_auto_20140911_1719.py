# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitbilder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bit',
            name='bit_image',
            field=models.ImageField(verbose_name='Bitbild', upload_to='/img'),
        ),
        migrations.AlterField(
            model_name='bit',
            name='bit_vector',
            field=models.FileField(verbose_name='Bit-SVG', upload_to='/svg'),
        ),
    ]
