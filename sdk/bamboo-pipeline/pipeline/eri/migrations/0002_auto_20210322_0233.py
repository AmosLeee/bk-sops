# Generated by Django 2.2.19 on 2021-03-22 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eri", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="process",
            name="root_pipeline_id",
            field=models.CharField(db_index=True, max_length=33, verbose_name="根流程 ID"),
        ),
    ]
