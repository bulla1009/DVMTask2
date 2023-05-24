from django.urls import include, path
from django.contrib import admin
from core.views import store,vendors,customers
#from core.views import store, vendors, teachers

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', store.SignUpView.as_view(), name='signup'),
    path('accounts/signup/vendor/', vendors.VendorSignUpView.as_view(), name='vendor_signup'),
    path('accounts/signup/customer/', customers.CustomerSignUpView.as_view(), name='customer_signup'),
]
