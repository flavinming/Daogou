# -*-coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone


class Column(models.Model):
    name = models.CharField('栏目', max_length=50)
    slug = models.CharField('网址', max_length=50)
    order_num = models.IntegerField('顺序', )
    show_nav = models.BooleanField('导航栏显示', default=True)

    class Meta:
        ordering = ('-order_num',)
        verbose_name = '栏目'
        verbose_name_plural = '栏目'

    def __str__(self):
        return self.name


class Product(models.Model):
    SOURCE_CHOICES = (
        ('jd', '京东'),
        ('taobao', '淘宝店铺'),
        ('tmall', '天猫店铺'),
        ('vip', '唯品会'),
        ('mj', '蘑菇街'),
        ('jumei', '聚美优品'),
        ('other', '精选店铺')
    )
    title = models.CharField('标题', max_length=100)
    item_id = models.CharField('商品编号', blank=True, max_length=50)
    price = models.FloatField('单价')
    original_price = models.FloatField('历史单价', blank=True, null=True)
    item_image = models.ImageField('商品图片', upload_to="images/%Y/%m/%d", blank=True)
    original_image = models.CharField('商品原始')
    ad_url = models.URLField('推广链接', blank=True, max_length=500)
    original_url = models.URLField('原链接', blank=True, max_length=500)

    column = models.ManyToManyField(Column, verbose_name="归属栏目")

    item_source = models.CharField('来源', max_length=50, choices=SOURCE_CHOICES)
    is_new = models.BooleanField('新品', default=True, blank=True)
    solded = models.IntegerField('已销售', blank=True, null=True)
    publish = models.DateTimeField('发布时间', default=timezone.now)

    # tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        verbose_name = '商品'
        verbose_name_plural = '商品'
        unique_together = ('title', 'price', 'ad_url')

    def __str__(self):
        return self.title


class JdItem(models.Model):
    item_id = models.IntegerField('商品编号', unique=True, blank=True)
    original_url = models.URLField('原始链接', blank=True, max_length=250)
    ad_url = models.URLField('推广链接', blank=True, max_length=500)
    publish = models.DateTimeField('发布时间', default=timezone.now, blank=True)

    class Meta:
        verbose_name = '京东推广'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.original_url

