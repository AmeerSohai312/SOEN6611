import csv
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json



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


def analysis_page(request):
    return render(request, 'analysis_page.html')

def function_use_case_1(data):
    # Add your code for analyzing Use Case 1 here
    # This function should return the results in a format you want to display
    result = []
    for row in data:
        result_row = []
        for value in row:
            # Example mathematical operation (replace with your actual calculation)
            result_row.append(float(value) * 2)
        result.append(result_row)
    return result

def function_use_case_2(data):
    # Add your code for analyzing Use Case 2 here
    # This function should return the results in a format you want to display
    result = []
    for row in data:
        result_row = []
        for value in row:
            # Example mathematical operation (replace with your actual calculation)
            result_row.append(float(value) ** 2)
        result.append(result_row)
    return result


def run_analysis(request):
    use_case = request.GET.get('use_case')
    data = request.session.get('csv_data', [])

    if use_case == 'use_case_1':
        results = function_use_case_1(data)
    elif use_case == 'use_case_2':
        results = function_use_case_2(data)
    else:
        results = "Invalid use case selected"

    return HttpResponse(json.dumps(results), content_type='application/json')

