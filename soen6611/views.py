import csv
from django.shortcuts import render

def display_csv(request):
    file_path = "soen6611/final_data.csv"  # Replace with your CSV file path

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    return render(request, 'csv_display/display.html', {'data': data})
