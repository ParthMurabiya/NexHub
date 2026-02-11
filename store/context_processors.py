from .models import Account

def logged_in_user(request):
    user_id = request.session.get("user_id")
    user = None

    if user_id:
        user = Account.objects.filter(id=user_id).first()

    return {
        "logged_user": user
    }
