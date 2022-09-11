# Generated by Django 4.1 on 2022-09-11 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0001_initial"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order", options={"ordering": ["order_date"]},
        ),
        migrations.AlterField(
            model_name="lineitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="line_items",
                to="order.order",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="lineitem", unique_together={("order", "item")},
        ),
    ]
