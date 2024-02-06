from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import EmailMessage

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    # ログインをしたときの処理

    #送信元のIPアドレスを手に入れる
    ip_list = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_list:
        ip  = ip_list.split(',')[0]
    else:
        ip  = request.META.get('REMOTE_ADDR')


    user_agent  = request.META.get('HTTP_USER_AGENT')


    body = "ご利用ありがとうございます。下記端末でログインされました。\n\n"
    body += f"IPアドレス: {ip}\n"
    body += f"ユーザーエージェント: {user_agent}\n\n"

    msg = EmailMessage(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[ request.user.email ],
            subject ="セキュリティ通知",
            body=body,
          )

    msg.send(fail_silently=False)

    print(f'{user.username}がログインしました。')

@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    # ログアウトをしたときの処理
    print(f'{user.username}がログアウトしました。')



