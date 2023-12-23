from django.urls import path
from contact import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'contact'


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # user (CRUD)
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
    
    path('loan/make/', views.loancreate, name='create_loan'),
    path('loan/<int:loan_id>/detail/', views.loan, name='loan'),
    path('loan/<int:loan_id>/update/', views.update, name='update_loan'),
    path('loan/<int:loan_id>/delete/', views.delete, name='delete_loan'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
