from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>', views.ProductDetailtView.as_view()),
]



