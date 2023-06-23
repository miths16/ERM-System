# Generated by Django 4.2 on 2023-06-21 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('emp_id', models.IntegerField()),
                ('emailid', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=50, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('joiningdate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corpid', models.CharField(max_length=50, null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('joiningdate', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeDetail',
        ),
        migrations.AddField(
            model_name='employeedata',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.managerdetail'),
        ),
    ]