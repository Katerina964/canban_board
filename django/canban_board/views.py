from django.shortcuts import render, redirect
from .models import Card
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
def list(request):
    plan = Card.objects.filter(state="P")
    doing = Card.objects.filter(state="D")
    done = Card.objects.filter(state="DN")
    context = {'plan': plan, 'doing': doing, 'done': done}
    return render(request, 'canban_board/list.html', context)
