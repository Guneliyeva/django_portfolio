from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import PortfolioForm

def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio_create')  
    else:
        form = PortfolioForm()
    return render(request, 'portfolio_form.html', {'form': form})
