# Generated by Django 4.1.3 on 2022-11-01 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0007_remove_habit_h_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='r_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habit.habit'),
        ),
    ]
