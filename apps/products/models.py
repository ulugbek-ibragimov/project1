from django.db import models
from django.utils.translation import gettext_lazy as _
from moviepy.editor import VideoFileClip
from datetime import timedelta

from numpy.ma.core import less_equal

from apps.users.models import User



class Lesson(models.Model):
    title = models.CharField(_("Title"), max_length=128)
    url_to_lesson = models.FileField(upload_to='lessons/files/', verbose_name="File")
    duration = models.DurationField(verbose_name="Duration", editable=False, blank=True, null=True)

    def save(
            self,
            *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        super().save(*args, force_insert, force_update, using, update_fields)

        if self.url_to_lesson and not self.duration:
            clip = VideoFileClip(self.url_to_lesson.path)
            self.duration = timedelta(seconds=clip.duration)
            self.save()

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return self.title

class Owner(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    class Meta:
        verbose_name = _('Owner')
        verbose_name_plural = _('Owner')

class Product(models.Model):
    owner = models.ForeignKey(to=Owner, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, null=True, blank=True)
    lesson = models.ManyToManyField(to=Lesson, related_name='products')
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

class UserProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product", related_name='product_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User", related_name='user_products')
    lesson = models.ManyToManyField(Lesson, verbose_name="Lesson", related_name='user_products')

    class Meta:
        verbose_name = "User Product"
        verbose_name_plural = "User Products"
    def __str__(self):
        return f"product: {self.product.title} user: {self.user}"

class UserProductLesson(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Lesson", related_name='user_product_lessons')
    user_product = models.ForeignKey(UserProduct, on_delete=models.CASCADE, verbose_name="user_product_lessons",
                                    related_name='user_product_lessons')
    view_duration = models.DurationField(verbose_name="View duration")
    watched = models.BooleanField(default=False, verbose_name="Watched")


    class Meta:
        verbose_name = "User product lesson"
        verbose_name_plural = "User product lessons"
    def __str__(self):
        return f"{self.user_product} lesson: {self.lesson}"