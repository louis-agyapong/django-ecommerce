# Generated by Django 4.0.3 on 2022-03-09 23:56

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(help_text='A URL-friendly title.', max_length=100, verbose_name='Slug')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='inventory.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'product Category',
                'verbose_name_plural': 'product categories',
                'ordering': ['name'],
            },
        ),
    ]
