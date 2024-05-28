from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import BigData.templates
import pandas as pd
import re

@csrf_exempt
@require_POST
def generatedDataCountry(request, code, category):
        df = pd.read_excel('N:\SOFTWARE\DERS PROJELERI\Ağ Programlama\world-data-2023.xlsx')
        data_as_dicts = df.to_dict(orient='records')

        for row in data_as_dicts:
            if str(row["Abbreviation"]).lower() == str(code).lower():
                return JsonResponse({"data": row[category]})

@csrf_exempt
@require_POST
def generatedDataCountries(request, category):
    nodes = []
    edges = []
    
    df = pd.read_excel('N:\SOFTWARE\DERS PROJELERI\Ağ Programlama\world-data-2023.xlsx')
    data_as_dicts = df.to_dict(orient='records')
    datas = list(data_as_dicts)
        
    for i, row in enumerate(datas):
        nodes.append({"id": i + 1, "label": str(row["Country"]),})
        for j, rowi in enumerate(datas):
            x = filter(str(row[category]))
            y = filter(str(rowi[category]))
            if (abs(x - y) > (max(x, y) * 99) / 100):
                edges.append({"from": i + 1, "to": j + 1})
                break

    return JsonResponse({"nodes": nodes, "edges": edges})

def filter(text):
    result = re.sub(r'[^0-9.]', '', text)
    if result != '':
        return float(result)
    else:
        return 0.0

def generatedData(request):
    return render(request, '../templates/BigDataProject/generatedData.html')
