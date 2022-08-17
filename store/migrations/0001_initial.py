
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreCake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price_mini', models.IntegerField(blank=True, null=True)),
                ('price_1', models.IntegerField(blank=True, null=True)),
                ('price_2', models.IntegerField(blank=True, null=True)),
                ('price_3', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='store/cake')),
                ('code', models.IntegerField(default=1)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.bssignupdetail')),
            ],
        ),
    ]
