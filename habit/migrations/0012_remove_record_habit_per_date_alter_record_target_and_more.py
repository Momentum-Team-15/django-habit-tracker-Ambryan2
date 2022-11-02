# Generated by Django 4.1.3 on 2022-11-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0011_remove_date_dday_remove_date_dmonth_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='record',
            name='habit_per_date',
        ),
        migrations.AlterField(
            model_name='record',
            name='target',
            field=models.FloatField(blank=True),
        ),
        migrations.AddConstraint(
            model_name='habit',
            constraint=models.UniqueConstraint(fields=('action', 'user'), name='habit_action'),
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('h_date', 'r_habit', 'user'), name='habit_per_date'),
        ),
    ]
