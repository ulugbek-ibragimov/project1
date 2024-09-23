from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from apps.products.models import UserProductLesson, UserProduct

@receiver(post_save, sender=UserProductLesson)
def update_watched_condition(sender, instance, created, **kwargs):
    if not created:
        duration = instance.lesson.duration
        user_product_lessons = UserProductLesson.objects.filter(user_product=instance.user_product)
        for user_product_lesson in user_product_lessons:
            if user_product_lesson.view_duration.total_seconds() > duration * 0.8:
                instance.watched = True
                instance.save()

