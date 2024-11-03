from . import views
from django.urls import path
urlpatterns = [
        path('<int:cart_id>', views.CartViewSet.as_view() , name="cart_view"),
        path('cartItem/<str:cart_id>/<str:id>', views.CartItemViewSet.as_view() , name="cartItem_view")
]
