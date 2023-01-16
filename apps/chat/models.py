from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название канала")


class Message(models.Model):
    nickname = models.CharField(max_length=255, verbose_name="Никнейм")
    time = models.DateTimeField(auto_now_add=True, verbose_name="Время")
    text = models.TextField(verbose_name="Текст")
    chat = models.ForeignKey(Chat, models.CASCADE, verbose_name="Канал")
