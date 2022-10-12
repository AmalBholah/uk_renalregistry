# Generated by Django 3.2.6 on 2022-06-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("renaldataregistry", "0004_patientassessmentmed_1"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patientmedicationassessment",
            name="antihypertensives_others1",
        ),
        migrations.RemoveField(
            model_name="patientmedicationassessment",
            name="antihypertensives_others2",
        ),
        migrations.RemoveField(
            model_name="patientmedicationassessment",
            name="antihypertensives_others3",
        ),
        migrations.RemoveField(
            model_name="patientmedicationassessment",
            name="antihypertensives_others4",
        ),
        migrations.RemoveField(
            model_name="patientmedicationassessment",
            name="antihypertensives_others5",
        ),
        migrations.RemoveField(
            model_name="patientmedicationassessment",
            name="methyldopa",
        ),
        migrations.AddField(
            model_name="patientmedicationassessment",
            name="bpdrugs_others",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No"), ("U", "Unknown")],
                default="U",
                max_length=1,
                verbose_name="Others",
            ),
        ),
        migrations.AddField(
            model_name="patientmedicationassessment",
            name="centrally_acting",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No"), ("U", "Unknown")],
                default="U",
                max_length=1,
                verbose_name="Centrally acting",
            ),
        ),
        migrations.AddField(
            model_name="patientmedicationassessment",
            name="loop_diuretics",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No"), ("U", "Unknown")],
                default="U",
                max_length=1,
                verbose_name="Loop diuretics",
            ),
        ),
        migrations.AddField(
            model_name="patientmedicationassessment",
            name="mra",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No"), ("U", "Unknown")],
                default="U",
                max_length=1,
                verbose_name="MRA",
            ),
        ),
        migrations.AddField(
            model_name="patientmedicationassessment",
            name="p_vasodilators",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No"), ("U", "Unknown")],
                default="U",
                max_length=1,
                verbose_name="P Vasodilators",
            ),
        ),
        migrations.AddField(
            model_name="patientmedicationassessment",
            name="renin_inhibitors",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No"), ("U", "Unknown")],
                default="U",
                max_length=1,
                verbose_name="Renin Inhibitors",
            ),
        ),
        migrations.AddField(
            model_name="patientmedicationassessment",
            name="thiazides",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No"), ("U", "Unknown")],
                default="U",
                max_length=1,
                verbose_name="Thiazides",
            ),
        ),
    ]
