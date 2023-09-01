from django.shortcuts import render
from .models import *
from django.http import HttpResponse
#from django.views.generic.base import TemplateView
from .models import dbform
from openpyxl.drawing.image import Image
from openpyxl import load_workbook
from apply.utils import render_to_pdf
import pandas
# Create your views here.

def home(request):
    return render(request, "index.html")

def userreg(request):
    return render(request, 'adding.html')

def insertuser(request):
    vname = request.POST['name']
    vreg_no = request.POST['reg_no']
    vemail = request.POST['email']
    vphone = request.POST['phone']
    vaddress = request.POST['address']
    vdob = request.POST['dob']
    vimage = request.FILES['image']
    vsign = request.FILES['sign']
    eg = dbform(name = vname, reg_no = vreg_no, email = vemail,
                 phone = vphone, address = vaddress, dob = vdob, image = vimage, sign = vsign)
    eg.save() 
    return render(request, 'index.html')  
   
def output(request):
    try:
        Detail = dbform.objects.order_by('-id')[:1]
        return render(request, 'success.html', {'Detail': Detail})
      
    except dbform.DoesNotExist:
        return render(request,'success.html', {'error': 'No data found.'})

def exportdjango(request):
    filename = "c:/Users/DELL/Desktop/django project/regform/apply/resources/Form template2.xlsx"
    wb = load_workbook(filename)
    response = HttpResponse(content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['content-Disposition'] = 'attachment; filename = "Form template2.xlsx" '

    filename2 = "c:/Users/DELL/Desktop/django project/regform/apply/resources/form config.xlsx"
    excel_data_df = pandas.read_excel(filename2, sheet_name='Sheet1', header=None)
    Dict = excel_data_df.to_dict(orient='records')
 
    
    sheet = wb.active
    details = dbform.objects.latest('id')
    sheet[Dict[0][0]] = getattr(details, Dict[0][1])        
    sheet[Dict[1][0]] = getattr(details,Dict[1][1])
    sheet[Dict[2][0]] = getattr(details,Dict[2][1])
    sheet[Dict[3][0]] = getattr(details,Dict[3][1])
    sheet[Dict[4][0]] = getattr(details,Dict[4][1])
    sheet[Dict[5][0]] = getattr(details, Dict[5][1])

    img = Image(getattr(details, Dict[6][1]))
    img.width = 120
    img.height = 170
    sheet.add_image(img, Dict[6][0]) 
    Sign =Image(getattr(details, Dict[7][1]))
    Sign.width = 190
    Sign.height = 70
    sheet.add_image(Sign, Dict[7][0])

    wb.save(response)
    return response


def ResultList(request):
    template_name = "pdf.html"
    records = dbform.objects.all().order_by("id")

    return render_to_pdf(
        template_name,
        {
            "record": records,
        },
    )