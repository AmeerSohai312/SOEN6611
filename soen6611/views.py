import csv
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



def display_csv(request):
    file_path = "soen6611/final_data.csv"  # Replace with your CSV file path

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    return render(request, 'display.html', {'data': data})

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.reader(decoded_file)
        data = list(csv_reader)
        html_output = '<table border="1">'
        for row in data:
            html_output += '<tr>'
            for column in row:
                html_output += f'<td>{column}</td>'
            html_output += '</tr>'
        html_output += '</table>'
        return HttpResponse(html_output)
    return render(request, 'uploadFile.html')

def show_csv_content(request):
    data = request.session.get('csv_data')
    return render(request, 'csv_content.html', {'data': data})
