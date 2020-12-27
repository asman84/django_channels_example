

import channels.layers

from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver



from posts.models import Post


@receiver(post_save, sender=Post)
def send_notification_created_post(sender, created, instance, *args, **kwargs):
    if created:
        channel_layer = channels.layers.get_channel_layer()

        channel_name = f"post_notifications_{instance.author.id}"

        async_to_sync(channel_layer.group_send)(channel_name, {
            "type": "send_post_notification",
            "message": "post is created, you were asssigned as author",
        })

