from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
import uuid
import boto3

dynamodb = boto3.resource('dynamodb', region_name="YOUR_AWS_REGION")
table = dynamodb.Table('YourDynamoDBTable')

def index(request):
    response = table.scan()
    items = response['Items']
    return render(request,'index.html',{'items':items})

def add(request):
    if request.method == 'POST':
        item = {
            'id':str(uuid.uuid4()),
            'data':request.POST['data']
        }
        table.put_item(Item=item)
        return HttpResponse('Item added',status=200)