from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from customer.models import Customer
from .serializers import CustomerCreateSerializer, CustomerSerializer, CustomerUpdateSerializer


class CustomerListCreateAPIView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    input_serializer_class = CustomerCreateSerializer

    queryset = Customer.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.input_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = Customer(**serializer.validated_data)
        customer.save()
        output_serializer = self.serializer_class(customer)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class CustomerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CustomerSerializer
    input_serializer_class = CustomerUpdateSerializer

    queryset = Customer.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.input_serializer_class(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
