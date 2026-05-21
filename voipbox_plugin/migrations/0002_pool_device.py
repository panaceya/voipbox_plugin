from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0207_remove_redundant_indexes"),
        ("voipbox_plugin", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pool",
            name="device",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="voipbox_pools",
                to="dcim.device",
            ),
        ),
    ]
