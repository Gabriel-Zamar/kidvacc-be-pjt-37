<<<<<<< HEAD
# Generated by Django 3.2.4 on 2021-07-06 21:33
=======
# Generated by Django 3.2.4 on 2021-07-05 08:14
>>>>>>> 3fe9c7ea0c0f1c149b08f4491ae7f9161d389760

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20210703_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
