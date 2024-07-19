from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utility import currency_listing, convert

# Create your views here.
def home(request):
    if request.method == 'POST':
        base_currency = request.POST['base_currency']
        target_currency = request.POST['target_currency']
        amount = float(request.POST.get('amount'))
        result_ = convert(base_currency, amount, target_currency)

        print(f'{amount} {base_currency} in {target_currency} is {result_}')
        request.session['result'] = result_
        request.session['target_currency'] = target_currency
        return redirect('Ex_rate:result')
    else:
        template_name = 'index.html'
        conv_rates = currency_listing()
        context = {
            'conv_rates': conv_rates,
        }
        return render(request, template_name, context)

def result(request):
    print(request.session['result'])
    template_name = 'result.html'
    context = {
        'amount': request.session['result'],
        'target_currency': request.session['target_currency']
    }
    # return request('Ex_rate:home')
    return render(request, template_name, context)