from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_vendor:
            return redirect('vendors:prod_list') #Shows the product list
        else:
            return redirect('customers:prod_list')
    
    return render(request, 'store/home.html')
