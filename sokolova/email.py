from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import telebot
import requests

bot = telebot.TeleBot("6533754623:AAH8NPuSGH18BnetxoYoyLSypV-YmY7WRpM")


def send_message(text: str):
    token = "6533754623:AAH8NPuSGH18BnetxoYoyLSypV-YmY7WRpM"
    url = "https://api.telegram.org/bot"
    channel_id = "@testlabdjango"
    url += token
    method = url + "/sendMessage"
    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")


def send_contact_email_message(subject, email, content, ip, user_id):
    """
    Function to send contact form email
    """
    user = User.objects.get(id=user_id) if user_id else None
    message = render_to_string('feedback_email_send.html', {
        'email': email,
        'content': content,
        'ip': ip,
        'user': user,
    })
    bot.send_message(945125790, message)
    send_message(message)
