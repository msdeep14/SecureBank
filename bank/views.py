from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bank.models import MyBankBranch
import urllib.parse
import collections
import itertools

# Create your views here.

def parse_ifsc_path(querypath):
    #  http://127.0.0.1:8000/fetchifsc/ifsc=ABHY0065002&limit=1&offset=1/
    return dict(urllib.parse.parse_qsl(querypath))

def parse_bank_path(querypath):
    # http://127.0.0.1:8000/fetchifsc/bankname=ABHY0065002&city=&limit=1&offset=1/
    return dict(urllib.parse.parse_qsl(querypath))


class FetchIfscView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,querypath):
        print("query:: ",querypath)

        query_dict = parse_ifsc_path(querypath)
        result=[]
        limit=1
        offset=0
        try:
            if('limit' in query_dict):
                limit=int(query_dict['limit'])
            if('offset' in query_dict):
                offset=int(query_dict['offset'])
        except ValueError:
            return Response([{"Message":"Invalid query parameters"}])

        ifsc=''
        if('ifsc' in query_dict):
            ifsc=query_dict['ifsc']

        # print("limit,offset,ifsc:: ", limit,"  ",offset,"  ",ifsc)

        if(ifsc==''):
            return Response([{"Message":"ifsc is required to fetch details"}])
        # one ifsc will return maximum one result => ifsc is unique for each bank
        if(limit<1 or offset>0):
            result=[]
        else:
            result = MyBankBranch.objects.all().filter(ifsc=ifsc).values('ifsc','bank_name','branch','address','city','district','state')
        # print(result)
        if not result:
            result=[{"Message":"NOT FOUND"}]
        return Response(result)

class FetchBankView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,querypath):
        print("query:: ",querypath)
        # print("request:: ",request)
        query_dict=parse_bank_path(querypath)

        # limit=int(query_dict['limit'])
        # offset=int(query_dict['offset'])
        # print("limit,offset:: ", limit,"  ",offset)
        # print("limit,offset:: ", query_dict['bankname'],"  ",query_dict['cityname'])
        bankname=''
        cityname=''
        if('bankname' in query_dict):
            bankname=query_dict['bankname']
        if('cityname' in query_dict):
            cityname=query_dict['cityname']

        if(bankname=='' or cityname==''):
            return Response([{"Message":"bankname and cityname both are required"}])

        result=MyBankBranch.objects.all().filter(bank_name=bankname,city=cityname).values('ifsc','bank_name','branch','address','district','city','state')

        count=len(result)
        limit=count
        offset=0
        if('limit' in query_dict):
            limit=int(query_dict['limit'])
        if('offset' in query_dict):
            offset=int(query_dict['offset'])

        # if(offset >=count or limit<1):
        #     result=[]

        result=MyBankBranch.objects.all().filter(bank_name=bankname,city=cityname).values('ifsc','bank_name','branch','address','district','city','state')[offset:limit+offset]
        # print(result)
        if not result:
            result=[{"Message":"NO DETAILS FOUND"}]
        return Response(result)
