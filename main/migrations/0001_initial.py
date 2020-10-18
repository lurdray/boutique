# Generated by Django 3.1.2 on 2020-10-16 19:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cataloque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=50)),
                ('image', models.ImageField(upload_to='Images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('comment', models.TextField()),
                ('name', models.CharField(default='none', max_length=60)),
                ('post', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CommentBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=50)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=60)),
                ('email', models.CharField(default='none', max_length=60)),
                ('phone', models.CharField(default='none', max_length=60)),
                ('message', models.CharField(default='none', max_length=60)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.TextField()),
                ('price', models.CharField(default='none', max_length=60)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=350)),
                ('description', models.CharField(max_length=350)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('company', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('footer', models.TextField(blank=True, max_length=50)),
                ('newsletter', models.CharField(blank=True, max_length=50)),
                ('smtpport', models.CharField(blank=True, max_length=50)),
                ('icon', models.ImageField(blank=True, upload_to='images')),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('aboutheader', models.TextField(blank=True, max_length=500)),
                ('aboutus', models.TextField(blank=True, max_length=500)),
                ('contact', models.TextField(blank=True, max_length=500)),
                ('references', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(upload_to='images')),
                ('imagetwo', models.ImageField(upload_to='images')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(default='none', max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
