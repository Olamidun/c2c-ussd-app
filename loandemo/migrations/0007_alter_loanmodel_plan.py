# Generated by Django 3.2.9 on 2021-11-24 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loandemo', '0006_alter_loanmodel_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanmodel',
            name='plan',
            field=models.CharField(max_length=20),
        ),
    ]