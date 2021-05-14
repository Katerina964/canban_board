from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CardForm


@login_required(login_url='/accounts/login/')
def list(request):
    user_id = request.user.id
    todo = Card.objects.filter(state="TD", user=user_id)
    doing = Card.objects.filter(state="D", user=user_id)
    done = Card.objects.filter(state="DN", user=user_id)
    context = {'todo': todo, 'doing': doing, 'done': done}
    return render(request, 'canban_board/list.html', context)


def logout_view(request):
    logout(request)
    return redirect('canban_board:list')


def create_card(request):
    form = CardForm()
    context = {'form': form}
    return render(request, 'canban_board/create_card.html', context)


def delete_card(request, pk):
    resume = get_object_or_404(Card, pk=pk)
    resume.delete()
    return redirect('canban_board:list')


def change_card(request):
    pass
