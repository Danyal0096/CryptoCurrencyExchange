# Generated by Django 4.2.3 on 2023-07-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cryptoexchange", "0003_customer_stockvalue"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer", name="balance", field=models.FloatField(null=True),
        ),
    ]
