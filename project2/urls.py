from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [

    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
    path('success/', views.send_message),
]