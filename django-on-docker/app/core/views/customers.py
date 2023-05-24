from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse,reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import customer_required
#from ..forms import StudentInterestsForm, StudentSignUpForm, TakeQuizForm
from ..forms import CustomerSignUpForm
from ..models import User,Product,Wallet


class CustomerSignUpView(CreateView):
    model = User
    #fields = '__all__'
    form_class = CustomerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()        
        login(self.request, user)
        return redirect('customers:prod_list')
        
@method_decorator([login_required, customer_required], name='dispatch')
class AllProdListView(ListView):
    model = Product
    #ordering = ('name', )
    context_object_name = 'products'
    template_name = 'customers/prod_list.html'

    def get_queryset(self):
        #student = self.request.user.student
        #student_interests = student.interests.values_list('pk', flat=True)
        #taken_quizzes = student.quizzes.values_list('pk', flat=True)
        queryset = Product.objects.all() \
            #.exclude(pk__in=taken_quizzes) \
            #.annotate(questions_count=Count('questions')) \
            #.filter(questions_count__gt=0)
        return queryset

@method_decorator([login_required, customer_required], name='dispatch')
class WalletCreateView(CreateView):
    model = Wallet
    fields = ('amount',)
    template_name = 'customers/wallet_add_form.html'

    def form_valid(self, form):
        wallet = form.save(commit=False)
        wallet.user = self.request.user
        wallet.save()
        messages.success(self.request, 'The wallet was created successfully!')
        return redirect('customers:prod_list')
@method_decorator([login_required, customer_required], name='dispatch')
class WalletEditView(UpdateView):
    model = Wallet
    fields = ('amount',)
    template_name = 'customers/wallet_update_form.html'
    
    def get_success_url(self):
        return reverse('customers:prod_list')
    

