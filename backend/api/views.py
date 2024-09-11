from api import models, serializers
from rest_framework.generics import ListAPIView

class UserList(ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class CustomerList(ListAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

class InvoiceList(ListAPIView):
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer

class RevenueList(ListAPIView):
    queryset = models.Revenue.objects.all()
    serializer_class = serializers.RevenueSerializer

class LatestInvoices(ListAPIView):
    serializer_class = serializers.InvoiceSerializer
    def get_queryset(self):
        queryset = models.Invoice.objects.all().order_by("-date")[:5]
        return queryset
