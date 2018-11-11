from django.shortcuts import render
from bankapiapp.models import BankView
from bankapiapp.serializer import BankSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

# Create your views here.
class GetBranchDetails(APIView):
    serializer_class = BankSerializer

    def get(self, request, format=None):
        template_name = 'bankapiapp/branch.html'
        ifsc_code = request.GET.get('txtSearch')
        bank_detail = BankView.objects.filter(ifsc = ifsc_code)
        serializer = BankSerializer(bank_detail, many=True)
        return Response({'data' : serializer.data}, template_name=template_name)

class GetAllBranch(APIView):
    
    serializer_class = BankSerializer

    def get(self, request, format=None):
        template_name = 'bankapiapp/allbranch.html'
        bank_ = request.GET.get('txtbank')
        city_ = request.GET.get('txtcity')
        bank_detail = BankView.objects.filter(Q(bank_name__iexact=bank_) & Q(city__iexact=city_))
        serializer = BankSerializer(bank_detail, many=True)
        # print(bank_detail)
        return Response({'data' : serializer.data}, template_name=template_name)
