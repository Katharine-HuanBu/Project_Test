from django.db import models
from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class House(models.Model):
    """
    House table
    """
    #Define the field for the name of the house
    name = models.CharField(max_length=32, verbose_name='name')
    picture = models.ImageField(upload_to='houses')
    house_type_choices = (
        ('Houses', 'Houses'),
        ('Flats/Apartments', 'Flats/Apartments'),
        ('House/Flat Share', 'House/Flat Share'),
        ('Student Private Halls', 'Student Private Halls'),
        ('Other', 'Other')
    )
    house_type = models.CharField(verbose_name='house type', max_length=32, choices=house_type_choices)
    #Define the description of the house in this field
    description = RichTextUploadingField(verbose_name='detail')
    # Define the area of the house in this field
    area = models.FloatField(verbose_name='area')
    # Define the price of the house in this field
    price = models.FloatField(verbose_name='price(permonth)')
    # Define the position of the house in this field
    position = models.CharField(max_length=64, verbose_name='position')
    # bed_num
    bed_num = models.IntegerField(verbose_name='bed num', default=1)
    # post_code
    post_code = models.CharField(verbose_name='post code', default='430071', max_length=32)
    # Define the create time of the house in this field
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='online time')
    # The current status of house information
    # TODO status Not rent | have for rent
    STATUS_CHOICES = (
        ('wait to rent', 'wait to rent'),
        ('rented', 'rented'),
    )
    status = models.CharField(max_length=32, verbose_name='status', choices=STATUS_CHOICES, default='wait to rent')
    # update time
    update_time = models.DateTimeField(verbose_name='update time', auto_now=True)
    # @property
    # def deadline(self):
    #     """
    #     Display expiration time
    #     """
    #     # Find the current rent
    #     if self.status == 'rented':
    #         # Find the most recent rental
    #         lastest_rent = self.rent_set.last()
    #         status = lastest_rent.status
    #         if status in ['normal', 'delayed', 'apply to unsubscribe']:
    #             return lastest_rent.deadline
    #         else:
    #             return 'wait to rent'
    #     else:
    #         return 'wait to rent'

    class Meta:
        verbose_name = 'house'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

    def __str__(self):
        return str(self.name)

class HouseImages(models.Model):
    """
    房屋轮播图
    """
    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name='House')
    picture = models.ImageField(upload_to='house_images')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='create_at')

    class Meta:
        verbose_name = 'house_images'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

class Comments(models.Model):
    """
    房屋评论
    """
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='content')
    label_choices = (
        ('Postitive', 'Positive'),
        ('Negative', 'Negative'),
    )
    label = models.CharField(verbose_name='sentiment label', max_length=32, choices=label_choices, default='Positive')
    score = models.FloatField(verbose_name='sentiment score', default=1)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='create_at')

    class Meta:
        verbose_name = 'house_comments'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

