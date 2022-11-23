from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db import connection
from  django.contrib import messages
from . import forms
from json import dumps

def home(request):
    return render(request,'index.html')

def highway(request):
    showall = models.Highway.objects.all()
    context = {
        'data': showall
    }
    return render(request, 'Highways.html', context)

def insert(request):
    if request.method == "POST":
        if request.POST.get('highway_number') and request.POST.get('highway_name') and request.POST.get(
                'highway_type') and request.POST.get('built_date') and request.POST.get('total_length') and request.POST.get(
                'number_of_lanes'):
            saverecord = models.Highway()
            saverecord.highway_number = request.POST.get('highway_number')
            saverecord.highway_name = request.POST.get('highway_name')
            saverecord.highway_type = request.POST.get('highway_type')
            saverecord.built_date = request.POST.get('built_date')
            saverecord.total_length_in_km = request.POST.get('total_length')
            saverecord.number_of_lanes = request.POST.get('number_of_lanes')


            allval = models.Highway.objects.all()

            for i in allval:
                if i.highway_number == request.POST.get('highway_number'):
                    messages.warning(request, 'Highway already exists!')
                    return render(request, 'InsertHighway.html')

            saverecord.save()
            messages.success(request, 'Highway ' + saverecord.highway_number + ' is saved succesfully!!')
            return render(request, 'InsertHighway.html')
    else:
        return render(request, 'InsertHighway.html')

def sortHighways(request):
    if request.method == "POST":
        if request.POST.get('Sort'):
            type = request.POST.get('Sort')
            sorted = models.Highway.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request, 'Highways.html', context)
    else:
        return render(request,'Highways.html')

def editHighway(request,id):
    Highway=models.Highway.objects.get(highway_number=id)
    context={ 'edithighway' : Highway}
    return render(request,'editHighway.html',context)

def updateHighway(request,id):
    Highway=models.Highway.objects.get(highway_number=id)
    form=forms.HighwayForms(request.POST,instance=Highway)
    if form.is_valid():
        form.save()
        messages.success(request,"Highway details for Highway Number "+ Highway.highway_number +" has been updated successfully.")
    else:
        messages.error(request,"Please Enter valid details")
    return render(request,'editHighway.html',{'edithighway':Highway})

def deleteHighway(request,id):
    Highway=models.Highway.objects.get(highway_number=id)
    Highway.delete()
    showall = models.Highway.objects.all()
    context = {
        'data': showall
    }
    return render(request, 'Highways.html', context)

def tenders(request):
    showall = models.Tender.objects.all()
    context = {
        'data': showall
    }
    return render(request, 'Tenders.html', context)

def sortTenders(request):
    if request.method == "POST":
        if request.POST.get('Sort'):
            type = request.POST.get('Sort')
            sorted = models.Tender.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request, 'Tenders.html', context)
    else:
        return render(request,'Tenders.html')

def insertTenders(request):
    if request.method == "POST":
        if request.POST.get('tender_no') and request.POST.get('tender_title') and request.POST.get(
                'bid_submission_start_date') and request.POST.get('bid_submission_end_date') :
            saverecord = models.Tender()
            saverecord.tender_no = request.POST.get('tender_no')
            saverecord.tender_title = request.POST.get('tender_title')
            saverecord.bid_submission_start_date = request.POST.get('bid_submission_start_date')
            saverecord.bid_submission_end_date = request.POST.get('bid_submission_end_date')

            allval = models.Tender.objects.all()

            for i in allval:
                if i.tender_no == request.POST.get('tender_no'):
                    messages.warning(request, 'Tender already exists!')
                    return render(request, 'InsertTender.html')

            saverecord.save()
            messages.success(request, 'Tender ' + saverecord.tender_no + ' is saved succesfully!!')
            return render(request, 'InsertTender.html')
    else:
        return render(request, 'InsertTender.html')

def editTender(request,id):
    Tender = models.Tender.objects.get(tender_no=id)
    context = {'edittender': Tender}
    return render(request, 'editTender.html', context)

def updateTender(request,id):
    Tender = models.Tender.objects.get(tender_no=id)
    form = forms.TednerForms(request.POST, instance=Tender)
    if form.is_valid():
        form.save()
        messages.success(request,
                         "Tender details for Tender Number " + str(Tender.tender_no) + " has been updated successfully.")
    else:
        messages.error(request, "Please Enter valid details")
    return render(request, 'editTender.html', {'edittender': Tender})

def deleteTender(request,id):
    Tender = models.Tender.objects.get(tender_no=id)
    Tender.delete()
    showall = models.Tender.objects.all()
    context = {
        'data': showall
    }
    return render(request, 'Tenders.html', context)

def runquery(request):
    raw_query = "select highway.* from highway_refined_schema.highway natural join highway_refined_schema.maintenance natural join (highway_refined_schema.problem1 natural join highway_refined_schema.problem2) where problem2.maintenance_priority='High'"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    data = cursor.fetchall()

    return render(request, 'Highway_query.html', {'data': data})

def runquery2(request):
    raw_query = "select * from highway_refined_schema.tenders where bid_submission_end_date-bid_submission_start_date > 20;"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    data = cursor.fetchall()
    return render(request,'Tender_query.html',{'data': data})

def runquery3(request):
    raw_query = "select count(highway_number) from highway_refined_schema.highway where extract(year from built_date) = 2022;"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    data = cursor.fetchall()
    raw_query = "select count(highway_number) from highway_refined_schema.highway where extract(year from built_date) = 2021;"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    data1 = cursor.fetchall()

    raw_query = "select count(highway_number) from highway_refined_schema.highway where extract(year from built_date) = 2020;"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    data2 = cursor.fetchall()
    context = { 'data1' : data,
                'data2' : data1,
                'data3' : data2}
    dataJSON = dumps(context)
    return render(request,'Highway_chart.html',{'data' : dataJSON})

def search(request):
    Highway = models.Highway.objects.get(highway_number=request.POST.get('search'))
    context = {'highway': Highway}
    return render(request, 'Search.html', context)

def searchtender(request):
    Tender = models.Tender.objects.get(tender_no=request.POST.get('search'))
    context = { 'tender' : Tender }
    return render(request, 'SearchTender.html', context)