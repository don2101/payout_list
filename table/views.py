from django.shortcuts import render
from .models import Payout
from .forms import PayoutModelForm


# Create your views here.
def main_page(request):
    payout_list = Payout.objects.all()
    context = { 'payout_list': payout_list }

    return render(request, 'table/items.html', context=context)


def add_payout(request):
    forms = PayoutModelForm()
    context = { 'forms': forms }

    return render(request, 'table/add.html', context=context)


