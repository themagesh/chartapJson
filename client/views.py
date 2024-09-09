from django.shortcuts import render, redirect
from .forms import StockForm
import json
import os
from django.conf import settings

DB_FILE_PATH = os.path.join(settings.BASE_DIR, 'db.json')

def write_to_db(data):
    try:
        with open(DB_FILE_PATH, 'r+') as file:
            db = json.load(file)
            db.append(data)
            file.seek(0)
            json.dump(db, file, indent=4)
    except FileNotFoundError:
        with open(DB_FILE_PATH, 'w') as file:
            json.dump([data], file, indent=4)

def read_from_db():
    try:
        with open(DB_FILE_PATH, 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []

def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock_data = {
                            'stockCode': form.cleaned_data['stockCode'],
                            'companyName': form.cleaned_data['companyName'],
                            'industry':form.cleaned_data['industry'],
                            'sector':form.cleaned_data['sector'],
                            'website':form.cleaned_data['website'],
                            'about': form.cleaned_data['about'],
                            'singleLine':form.cleaned_data['singleLine'],
                            'upTrend':form.cleaned_data['upTrend'],
                            'downTrend':form.cleaned_data['downTrend'],
                            'lineCross':form.cleaned_data['lineCross'],
                            'lineTouch':form.cleaned_data['lineTouch'],
                        }
            write_to_db(stock_data)
            return redirect('add_stock')
        
    else:
        form = StockForm()
    stocks= read_from_db()[-1:] 
       
    return render(request, 'add_stock.html', {'form': form,'stocks': stocks})

def display_name(request):
    stocks = read_from_db() 
    return render(request, 'add_stock.html', {'stocks': stocks})

