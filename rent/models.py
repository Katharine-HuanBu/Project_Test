from tabnanny import verbose
from django.db import models
from house.models import *
import datetime
# Create your models here.

class Rent(models.Model):
    """
    出租表
    """
    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name='House')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name="h_rent_user")
    # 租的时候的租金
    price = models.FloatField(verbose_name='Rent Price Per Month')
    # 下单时间
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Rent Time')
    # 开始时间
    start_at = models.DateField(verbose_name='Start Date')
    # 租的月份数
    months = models.IntegerField(verbose_name='Rent Months', default=1)
    # 结束时间
    end_at = models.DateField(verbose_name='End Date')
    # 总价
    money = models.FloatField(verbose_name='total money', default=0)
    STATUS_CHOICES = (
        ('normal', 'normal'),
        ('apply to unsubscribe', 'apply to unsubscribe'),
        ('unsubscribed', 'unsubscribed'),
        ('delayed', 'delayed'),
    )
    # Unsubscribe needs to be reviewed by the administrator
    status = models.CharField(max_length=32, verbose_name='status', choices=STATUS_CHOICES, default='normal')
    rent_type_choices = (
        ('First Rent', 'Frst Rent'),
        ('Delay', 'Delay')
    )
    rent_type = models.CharField(verbose_name='Rent Type', max_length=32, choices=rent_type_choices, default='First Rent')
    # 父ID
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='from')

    # @property
    # def total_money(self):
    #     """
    #     Total price
    #     """
    #     return self.months * self.house.price

    # @property
    # def is_deadline(self):
    #     """
    #     Whether or not on the deadline
    #     :return:
    #     """
    #     return datetime.datetime.now().date() >= self.deadline

    # @property
    # def current_status(self):
    #     """
    #     Current state
    #     1. The lease
    #     2. Lease cancellation has been applied for
    #     3. Succeeded
    #     4. Continue to postpone
    #     :return:
    #     """
    #     pass
    #     # TODO

    class Meta:
        verbose_name = 'User Rents'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

    def __str__(self):
        return f'{self.house.name} - {self.user.username} - {self.create_at}'

class Unsubscribe(models.Model):
    """
    取消预定:
    """
    rent = models.OneToOneField(Rent, on_delete=models.CASCADE, verbose_name='Rent Info')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')
    STATUS_CHOICES = (
        ('wait to approve', 'wait to approve'),
        ('approve', 'approve'),
    )
    # Unsubscribe needs to be reviewed by the administrator
    status = models.CharField(max_length=32, verbose_name='Status', choices=STATUS_CHOICES)
    # update time
    update_at = models.DateTimeField(verbose_name='Update Time', auto_now=True)
    # Whether to come from the delay
    is_from_delay = models.BooleanField(verbose_name='Is From Delay', default=False)
    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

    def __str__(self):
        return str(self.rent)