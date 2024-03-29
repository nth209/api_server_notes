# Generated by Django 2.1.3 on 2019-07-20 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quan',
            fields=[
                ('id_quan', models.AutoField(primary_key=True, serialize=False)),
                ('ten_quan', models.CharField(max_length=255, verbose_name='Tên Quận')),
            ],
        ),
        migrations.CreateModel(
            name='thanhpho',
            fields=[
                ('id_thanhpho', models.AutoField(primary_key=True, serialize=False)),
                ('ten_thanhpho', models.CharField(max_length=255, verbose_name='Tên thành phố')),
            ],
        ),
        migrations.CreateModel(
            name='userDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh_anh', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('detele_flg', models.IntegerField(default=0)),
                ('id_quan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.quan')),
                ('id_thanhpho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.thanhpho')),
            ],
        ),
        migrations.CreateModel(
            name='xa',
            fields=[
                ('id_xa', models.AutoField(primary_key=True, serialize=False)),
                ('ten_xa', models.CharField(max_length=255, verbose_name='Tên xã')),
                ('id_quan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.quan')),
            ],
        ),
        migrations.AddField(
            model_name='userdetail',
            name='id_xa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.xa'),
        ),
        migrations.AddField(
            model_name='quan',
            name='id_thanhpho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.thanhpho'),
        ),
    ]
