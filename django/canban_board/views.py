from django.shortcuts import render, redirect
from .models import Card
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url='/accounts/login/')
def list(request):
    user_id = request.user.id
    plan = Card.objects.filter(state="P", user=user_id)
    doing = Card.objects.filter(state="D", user=user_id)
    done = Card.objects.filter(state="DN", user=user_id)
    context = {'plan': plan, 'doing': doing, 'done': done}
    return render(request, 'canban_board/list.html', context)


def logout_view(request):
    logout(request)
    return redirect('canban_board:list')


def create_card(request):
    pass


def change_card(request):
    pass
