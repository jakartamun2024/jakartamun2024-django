# Generated by Django 4.2.5 on 2023-12-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_delegate', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('institution', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact_number', models.CharField(max_length=20)),
                ('line_id', models.CharField(max_length=50)),
                ('first_council_preference', models.CharField(max_length=255)),
                ('country_first_council', models.CharField(max_length=50)),
                ('second_council_preference', models.CharField(max_length=255)),
                ('country_second_council', models.CharField(max_length=50)),
                ('third_council_preference', models.CharField(max_length=255)),
                ('country_third_council', models.CharField(max_length=50)),
                ('previous_mun_experience', models.TextField()),
                ('dietary_restriction', models.CharField(max_length=255)),
                ('special_medical_condition', models.TextField()),
                ('accom_status', models.CharField(max_length=50)),
                ('proof_of_transfer', models.FileField(upload_to='uploads/')),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participants',
            },
        ),
    ]
