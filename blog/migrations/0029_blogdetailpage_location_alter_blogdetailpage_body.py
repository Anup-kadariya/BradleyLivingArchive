# Generated by Django 4.1.8 on 2024-04-21 16:16

from django.db import migrations, models
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0028_blogdetailpage_links"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogdetailpage",
            name="location",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="blogdetailpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    (
                        "video",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "video_embed",
                                    wagtail.embeds.blocks.EmbedBlock(
                                        help_text="Insert a video url here",
                                        required=False,
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                use_json_field=None,
            ),
        ),
    ]