from django.shortcuts import render, redirect
from .models import Payout
from .forms import PayoutModelForm
from datetime import datetime


# Create your views here.
def main_page(request):
    payout_list = Payout.objects.all()
    context = { 'payout_list': payout_list }

    return render(request, 'table/items.html', context=context)


def add_payout(request):
    if request.method == "GET":
        forms = PayoutModelForm()
        context = { 'forms': forms }

        return render(request, 'table/add.html', context=context)
    
    else:
        forms = PayoutModelForm(request.POST)
        
        if forms.is_valid():
            forms = forms.save(commit=False)
            now = datetime.now()
            forms.buy_date = f"{now.year}-{now.month}-{now.day}"
            forms.save()

            return redirect('table:main')
        else:
            redirect('table:add')

        


