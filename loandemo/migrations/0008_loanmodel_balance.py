# Generated by Django 3.2.9 on 2021-11-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loandemo', '0007_alter_loanmodel_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanmodel',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
