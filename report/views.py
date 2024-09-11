from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from school.models.app_settings import AppSettingModel
from school.models.school import SchoolModel
from student.models.student import StudentModel
from professors.models.teacher import TeacherModel
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from openpyxl import Workbook

from user.models.user import UserModel



# Create your views here.
@login_required(login_url='connexion:signin')
def rapport(request):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting == 1:
        if count_school == 1 :  
            return render(request, 'report/rapport.html')
        else:   
            return redirect('school:checkschool')
    else:
        return redirect('school:checksetting')



@login_required(login_url='connexion:signin')
def generate_pdf(request):
    selected = request.POST.get('choix')
    print(selected)
    # Create a BytesIO buffer to hold the PDF
    buffer = BytesIO()
    
    # Create a PDF object using the buffer
    pdf = canvas.Canvas(buffer)
    
    # Fetch data from the database
    data = StudentModel.objects.all()
    
    # Example: add text or content to the PDF
    pdf.drawString(100, 800, "Data Report")
    
    y_position = 750  # Starting Y position for data entries
    
    for record in data:
        # You can format the data as needed (e.g., record.name, record.value)
        pdf.drawString(100, y_position, f"Record: {record.nom} - prenoms : {record.prenom} - date de creation : {record.date_de_creation}")
        y_position -= 20  # Move down for the next line
    
    # Finalize the PDF
    pdf.showPage()
    pdf.save()
    
    # Get the value of the BytesIO buffer and create an HTTP response
    pdf_output = buffer.getvalue()
    buffer.close()
    
    response = HttpResponse(pdf_output, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    return response

@login_required(login_url='connexion:signin')
def generate_excel(request):
    # Create an in-memory workbook
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Data Report"
    
    # Fetch data from the database
    data = StudentModel.objects.all()
    
    # Add headers (if needed)
    worksheet.append(["ID", "Name", "prenom", "date de creation"])
    
    # Write data to Excel
    for record in data:
        worksheet.append([record.id, record.nom, record.prenom, record.date_de_creation])
    
    # Prepare the response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="report.xlsx"'
    
    # Save the workbook to the response
    workbook.save(response)
    
    return response