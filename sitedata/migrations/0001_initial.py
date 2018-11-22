# Generated by Django 2.0.5 on 2018-11-21 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricUseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid_parallel', models.BooleanField(verbose_name='grid parallel without power injecting')),
                ('service_voltage', models.FloatField(verbose_name='Service voltage (kV)')),
                ('Ave_Elec_Demand_Jan', models.FloatField(verbose_name='Average electric demand January (kW)')),
                ('Peak_Elec_Demand_Jan', models.FloatField(verbose_name='Peak electric demand January (kW)')),
            ],
        ),
        migrations.CreateModel(
            name='FuelUseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SiteData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=200, verbose_name='Project name')),
                ('operating_hours', models.IntegerField(verbose_name='Operating hours per day')),
                ('operating_days', models.IntegerField(verbose_name='Operating days per week')),
                ('operating_weeks', models.IntegerField(verbose_name='Operating weeks per year')),
                ('alitude', models.IntegerField(verbose_name='Alitude (m)')),
                ('summer_temp', models.FloatField(verbose_name='Summer design temperature')),
                ('winter_temp', models.FloatField(verbose_name='Winter design temperature')),
            ],
        ),
        migrations.CreateModel(
            name='ThermalLoads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='electricusedata',
            name='projectname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitedata.SiteData'),
        ),
    ]
