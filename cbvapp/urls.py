from django.urls import path
from cbvapp import views

urlpatterns = [
    path('view_comments' , views.view_comments),
    path('1st' , views.FirstView.as_view()),
    path('2nd' , views.SecondView.as_view()),
    path('school-list' , views.SchoolListView.as_view(), name='school-list'),
    # path('<int:pk>' , views.SchoolDetailView.as_view(), name='school_detail'),
    # or
    # path('school<int:pk>' , views.SchoolDetailView.as_view(), name='school_detail'),
    # or
    # path('school/<int:pk>' , views.SchoolDetailView.as_view(), name='school_detail'),
    # or
    path('school=<int:pk>' , views.SchoolDetailView.as_view(), name='school_detail'),
    path('create-school' , views.SchoolCreateView.as_view(), name='create-school'),
    path('delete=<int:pk>' , views.SchoolDeleteView.as_view(), name='delete'),
    path('school_updation_success' , views.SchoolUpdationSuccess.as_view(), name='school_updation_success'),
    path('update=<int:pk>' , views.SchoolUpdateView.as_view(), name='update'),
]