# Generated by Django 3.2.12 on 2022-07-10 06:23

from django.db import migrations
import mirage.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220710_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogdetailpage',
            name='intro',
            field=mirage.fields.EncryptedCharField(max_length=250),
        ),
    ]
