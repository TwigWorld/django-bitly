# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bittle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('absolute_url', models.URLField()),
                ('hash', models.CharField(max_length=10)),
                ('shortKeywordUrl', models.URLField(blank=True)),
                ('shortUrl', models.URLField()),
                ('userHash', models.CharField(max_length=10)),
                ('statstring', models.TextField(editable=False, blank=True)),
                ('statstamp', models.DateTimeField(null=True, editable=False, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='StringHolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('absolute_url', models.URLField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='bittle',
            unique_together=set([('content_type', 'object_id')]),
        ),
    ]
