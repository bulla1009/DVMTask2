from django.urls import include, path

#from .views import store, vendors, customers
from .views import store,vendors,customers
urlpatterns = [
    path('', store.home, name='home'),
    path('vendors/', include(([
        path('', vendors.ProdListView.as_view(), name='prod_list'),
        path('prod/', vendors.ProdCreateView.as_view(), name='prod_add_list'),
        #path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        #path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        #path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'core'), namespace='vendors')),

    path('customers/', include(([
        path('', customers.AllProdListView.as_view(), name='prod_list'),
        #path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        #path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        #path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        #path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        path('wallet/add/',customers.WalletCreateView.as_view(), name='wallet_add'),
        path('wallet/<int:pk>',customers.WalletEditView.as_view(), name='wallet_edit'),
        #path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        #path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'core'), namespace='customers')),
]
