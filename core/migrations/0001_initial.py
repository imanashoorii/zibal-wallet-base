# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-09-07 12:48
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('companyName', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('mobile', models.CharField(max_length=11, null=True)),
                ('mobileVerifiedAt', models.DateTimeField(null=True)),
                ('transactionPerDay', models.IntegerField(null=True)),
                ('posWantedNum', models.IntegerField(null=True)),
                ('activityDesc', models.TextField(null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('status', models.IntegerField(default=0)),
                ('userType', models.IntegerField(default=0, null=True)),
                ('operatorUserStatus', models.IntegerField(default=0, null=True)),
                ('economyCode', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('postalCode', models.CharField(max_length=20, null=True)),
                ('nationalCode', models.CharField(max_length=20, null=True)),
                ('referralCode', models.CharField(max_length=120, null=True)),
                ('checkoutDelayByDay', models.IntegerField(default=0)),
                ('comment', models.TextField(null=True)),
                ('maxWallets', models.IntegerField(default=0)),
                ('mobileVerifyToken', models.IntegerField(null=True)),
                ('verifyTokenExpireAt', models.DateTimeField(null=True)),
                ('forgotPasswordVerifyToken', models.CharField(max_length=88, null=True)),
                ('forgotPasswordVerifyTokenExpiredAt', models.DateTimeField(null=True)),
                ('emailVerifyToken', models.CharField(max_length=88, null=True)),
                ('emailVerifyTokenExpireAt', models.DateTimeField(null=True)),
                ('emailVerifiedAt', models.DateTimeField(null=True)),
                ('IPGLoyalty', models.IntegerField(null=True)),
                ('userDataStatus', models.IntegerField(default=0)),
                ('hubspotContactId', models.IntegerField(default=None, null=True)),
                ('permissions', models.TextField(null=True)),
                ('agreementIP', models.CharField(default=None, max_length=20, null=True)),
                ('twoFactor', models.BooleanField(default=False)),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True)),
                ('wageWallet', models.CharField(max_length=30, null=True)),
                ('secondPassword', models.CharField(blank=True, max_length=128, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='contactUS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('actualName', models.CharField(max_length=100, null=True)),
                ('fileSize', models.IntegerField(null=True)),
                ('type', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('ticketId', models.CharField(default=None, max_length=200, null=True)),
                ('allowedUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='allowedFiles', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MySQLTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('number', models.IntegerField()),
                ('createdAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('value', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=0, null=True)),
                ('body', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('commentedOnUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('createdAt',),
            },
        ),
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('iOS', 'iOS'), ('Android', 'Android'), ('Web', 'Web')], max_length=20)),
                ('token', models.CharField(max_length=200, unique=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together=set([('user', 'type')]),
        ),
    ]
