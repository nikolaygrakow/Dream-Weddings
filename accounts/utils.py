from django.core.mail import send_mail

def send_password_changed_email(user):
    send_mail(
        subject="Your password has been changed",
        message=(
            f"Hello {user.get_username()},\n\n"
            "Your Dream Weddings account password has been changed successfully.\n\n"
            "If you did not make this change, please contact us immediately.\n\n"
            "Kind regards,\n"
            "The Dream Weddings Team"
        ),
        from_email=None,
        recipient_list=[user.email],
        fail_silently=False,
    )