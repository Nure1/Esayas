from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics 
from .models import Location 
from .serializers import LocationSerializer 
from openpyxl import Workbook

class LocationListAPIView(generics.ListAPIView): 
    queryset = Location.objects.all() 
    serializer_class = LocationSerializer

class LocationUpdateAPIView(generics.UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationCreateAPIView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDeleteAPIView(generics.DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

def export_to_excel(request):
    # Fetch data from the model
    locations = Location.objects.all()


    # Create a new workbook and add a worksheet
    workbook = Workbook()
    worksheet = workbook.active


    # Get all field names from the Location model
    field_names = [field.name for field in Location._meta.get_fields() if field.concrete]


    # Write column headers
    for col_num, field_name in enumerate(field_names, 1):
        worksheet.cell(row=1, column=col_num, value=field_name)


    # Write data rows
    for row_num, location in enumerate(locations, 2):
        for col_num, field_name in enumerate(field_names, 1):
            if field_name == 'user':
                user_value = getattr(location.user, 'username', '')
                worksheet.cell(row=row_num, column=col_num, value=user_value)
            else:
                field_value = getattr(location, field_name, '')
                worksheet.cell(row=row_num, column=col_num, value=field_value)


    # Set the response content type
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=locations.xlsx'


    # Save the workbook to the response
    workbook.save(response)


    return response
