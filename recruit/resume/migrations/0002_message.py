# Generated by Django 3.0.3 on 2024-06-24 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='消息内容')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('is_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='接收方')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='发送方')),
            ],
            options={
                'verbose_name': '消息',
                'verbose_name_plural': '消息',
                'ordering': ['-timestamp'],
            },
        ),
    ]
