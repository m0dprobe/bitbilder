# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bit',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('bit_image', models.ImageField(verbose_name='Bitbild', upload_to='')),
                ('bit_vector', models.FileField(verbose_name='Bit-SVG', upload_to='')),
                ('bitname', models.CharField(max_length=50, verbose_name='Bit-Name')),
                ('author', models.CharField(max_length=100, verbose_name='Autor')),
                ('creation_date', models.DateField(verbose_name='Erstell-Datum')),
                ('license', models.CharField(max_length=100, verbose_name='Lizenz', choices=[('CC0', 'CC0 (Public Domain)'), ('OE', 'für die OE uneingeschränkt nutzbar'), ('WTFPL', 'uneingeschränkt nutzbar unter WTF PL')])),
                ('reserved', models.BooleanField(verbose_name='Reserviert?', default=False)),
                ('reserved_for', models.CharField(max_length=100, verbose_name='Reserviert für', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
