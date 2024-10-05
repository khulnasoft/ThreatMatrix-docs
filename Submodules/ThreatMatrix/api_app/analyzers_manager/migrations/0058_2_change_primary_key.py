# Generated by Django 4.2.8 on 2024-01-09 14:31
import django
from django.contrib.postgres.expressions import ArraySubquery
from django.db import migrations, models


def migrate(apps, schema_editor):
    AnalyzerConfig = apps.get_model("analyzers_manager", "AnalyzerConfig")
    AnalyzerConfig.objects.update(
        disabled2=ArraySubquery(
            AnalyzerConfig.objects.filter(pk=models.OuterRef("pk")).values(
                "disabled_in_organizations__pk"
            )
        )
    )


class Migration(migrations.Migration):
    dependencies = [
        ("analyzers_manager", "0058_1_change_primary_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="analyzerconfig",
            name="disabled2",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.IntegerField(),
                blank=True,
                default=list,
                size=None,
            ),
        ),
        migrations.RunPython(migrate),
        migrations.AlterField(
            model_name="analyzerreport",
            name="config",
            field=models.CharField(max_length=100, null=False, blank=False),
        ),
        migrations.RemoveField(
            model_name="analyzerconfig", name="disabled_in_organizations"
        ),
    ]
