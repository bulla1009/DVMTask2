from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import vendor_required
#from ..forms import StudentInterestsForm, StudentSignUpForm, TakeQuizForm
from ..forms import VendorSignUpForm
from ..models import Vendors, User, Product


class VendorSignUpView(CreateView):
    model = User
    #fields = '__all__'
    form_class = VendorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('vendors:prod_list')
@method_decorator([login_required, vendor_required], name='dispatch')
class ProdListView(ListView):
    model = Product
    #ordering = ('name', )
    context_object_name = 'products'
    template_name = 'vendors/prod_list.html'

    def get_queryset(self):
        user = self.request.user
        #student_interests = student.interests.values_list('pk', flat=True)
        #taken_quizzes = student.quizzes.values_list('pk', flat=True)
        queryset = Product.objects.filter(owner=user) \
            #.exclude(pk__in=taken_quizzes) \
            #.annotate(questions_count=Count('questions')) \
            #.filter(questions_count__gt=0)
        return queryset

@method_decorator([login_required, vendor_required], name='dispatch')
class ProdCreateView(CreateView):
    model = Product
    fields=('name','description','qty','price')
    template_name = 'vendors/prod_add_form.html'

    def form_valid(self, form):
        prod = form.save(commit=False)
        prod.owner = self.request.user
        prod.save()
        messages.success(self.request, 'The product was created successfully!')
        return redirect('vendors:prod_list')

