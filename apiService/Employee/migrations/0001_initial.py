# Generated by Django 3.1.3 on 2020-11-26 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeName', models.CharField(max_length=200)),
                ('DateJoin', models.CharField(max_length=200)),
                ('PhotoFileName', models.CharField(max_length=200)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.departments')),
            ],
        ),
    ]
