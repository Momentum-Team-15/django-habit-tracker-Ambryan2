# Generated by Django 4.1.3 on 2022-11-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0013_alter_record_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='actual_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
