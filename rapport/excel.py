
from rapport.models import Rapport
from django.shortcuts import render , get_object_or_404
import time
from datetime import date
from django.core import serializers
from django.http import HttpResponse
import json
from django.views import View
import threading
import zipfile
import os
import concurrent.futures
import xlsxwriter
from datetime import datetime,timedelta
import io
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ToExcelFileView(LoginRequiredMixin,View):
    template_name = 'rapport/rapport_list.html'
    # queryset = Switch.objects.all()
    login_url = '/login/'
    def get(self, request, format=None):
        user = request.user
        startDate = request.GET.get('startdate','')
        endDate = request.GET.get('enddate','')
        if not startDate:
            startDate =datetime.today().strftime('%Y-%m-%d')
        if not endDate:
            endDate =datetime.today().strftime('%Y-%m-%d')
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=your_template_name.xlsx'
        excel_file = createExcelFile(user,startDate,endDate)
        response.write(excel_file)
        return response


header = ['N°','DATE','HEURE','DESCRIPTION DE L\'INTERVENTION','EQUIPEMENT','ETAT APRES L\'INTERVENTION','DUREE D\'INTERVENTION','TYPE DE LA DEMANDE','N° DI','PIECES UTILISEES','OBSERVATION']

def createExcelFile(user,startDate,endDate):
    # employees = Employee.objects.all()
    output      = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    worksheet = workbook.add_worksheet('rapport')

    # worksheet.set_default_row(20)

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#F5DEB3'})


    headerCell = workbook.add_format({
        'bold': 1,
        # 'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#F5F5F5'})

    employeeCell = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#F5F5F5'})

    hourCell = workbook.add_format({
        # 'bold': 1,
        # 'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        # 'fg_color': '#F5F5F5'
        })







    ## start  header ##########
    # set width cell
    worksheet.set_column(0, 0, 5)
    worksheet.set_column(1, 1, 10)
    worksheet.set_column(2, 2, 10)
    worksheet.set_column(3, 3, 50)
    worksheet.set_column(4, 4, 25)
    worksheet.set_column(5, 5, 25)
    worksheet.set_column(6, 6, 25)
    worksheet.set_column(7, 7, 25)
    worksheet.set_column(8, 8, 25)
    worksheet.set_column(9, 9, 25)
    worksheet.set_column(10, 10, 25)


    # worksheet.write(3, col, 'Employee Name',headerCell)
    row = 0
    col = 0

    for day in header:
        worksheet.write(row,col,str(day) ,headerCell)
        col +=1

    rapports = Rapport.objects.filter(author=user,date__range=[startDate,endDate])
    di_type = dict(Rapport.YEAR_IN_SCHOOL_CHOICES)
    row = 1
    hour_format = '%H:%M:%S'
    for rp in rapports:
        print(rp.starthour)
        tm = datetime.strptime(str(rp.endhour), hour_format) - datetime.strptime(str(rp.starthour), hour_format)
        worksheet.write(row,0,str(rp.id) ,hourCell)
        worksheet.write(row,1,str(rp.date) ,hourCell)
        worksheet.write(row,2,str(rp.starthour) ,hourCell)
        worksheet.write(row,3,str(rp.description) ,hourCell)
        worksheet.write(row,4,str(rp.equipment) ,hourCell)
        worksheet.write(row,5,str(rp.state_after) ,hourCell)
        worksheet.write(row,6,str(tm) ,hourCell)
        worksheet.write(row,7,str(di_type[rp.type_di]) ,hourCell)
        worksheet.write(row,8,str(rp.n_di) ,hourCell)
        worksheet.write(row,9,str(rp.device_used) ,hourCell)
        worksheet.write(row,10,str(rp.note) ,hourCell)
        row +=1






    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data