from django.urls import path

from .views import CustomerListCreateAPIView, CustomerRetrieveUpdateAPIView

app_name = "customer"


urlpatterns = [
    path(
        "",
        CustomerListCreateAPIView.as_view(),
        name="customer-list-create",
    ),
    path(
        "<int:pk>/",
        CustomerRetrieveUpdateAPIView.as_view(),
        name="customer-retrieve-update",
    ),
]
