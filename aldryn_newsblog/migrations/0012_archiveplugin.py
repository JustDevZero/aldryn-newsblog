# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150313_1040'),
        ('aldryn_newsblog', '0011_tagsplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('app_config', models.ForeignKey(to='aldryn_newsblog.NewsBlogConfig')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
