#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=50, verbose_name='Имя категории')
	title = models.CharField(max_length=50, verbose_name='Название категории')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'категории'

	def __unicode__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=50, verbose_name='Имя тега')
	title = models.CharField(max_length=50, verbose_name='Название тега')

	class Meta:
		verbose_name = 'Тег'
		verbose_name_plural = 'теги'

	def __unicode__(self):
		return self.title

class Task(models.Model):
	user = models.ForeignKey(User, related_name='tasks', verbose_name='Автор')
	title = models.CharField(max_length=100, verbose_name='Название')
	description = models.TextField(verbose_name='Описание')
	create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	end_date = models.DateTimeField(blank=True, null=True, verbose_name='Сроки задачи')
	category = models.ForeignKey(Category, related_name='tasks', verbose_name='Категория')
	tag = models.ManyToManyField(Tag, related_name='tasks', verbose_name='Теги')

	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'

	def __unicode__(self):
		return self.title
