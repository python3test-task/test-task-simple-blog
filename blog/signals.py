from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Contact
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender = Post)
def followers_send_emails(instance, **kwargs):
    """
    Отправляем подписчикам почтовое уведомление о создании новог 
    поста (как через интерфейс сайта, так и через админку).
    """
    emails = []
    followers = Contact.objects.filter(user_to=instance.author)
    for u in followers: 
        emails.append(u.user_from.email)
    subject = 'Появилься новый пост'
    post_url = settings.DEFAULT_DOMAIN + instance.get_absolute_url()  # создаем полную ссылку на пост
    message = 'У автора: {} новый пост: \n{} \n\n{}'.format(instance.author, instance.title, post_url)               
    mail_sent = send_mail(subject, message, 'admin@myshop.com', emails)    
