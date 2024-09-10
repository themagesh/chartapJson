from django.shortcuts import render, redirect
from .forms import StockForm
import json
import os
from django.conf import settings
from collections import OrderedDict

DB_FILE_PATH = os.path.join(settings.BASE_DIR, 'db.json')
 
def write_to_db(data):
    try:
        with open(DB_FILE_PATH, 'r+') as file:
            db = json.load(file)
            if not db or 'id' not in db[-1]:
                db = []
            # Determine the new ID
            new_id = db[-1]['id'] + 1 if db else 1
            # db=[]
            # if db and 'id' in db[1]:
            #     new_id = db[-1]['id'] + 1
            # else:
            #     new_id = 1
            stock_data = OrderedDict()
            stock_data['id'] = new_id
            stock_data.update(data)

            db.append(stock_data)
            file.seek(0)
            json.dump(db, file, indent=4)
            file.truncate() 
    except FileNotFoundError:
        stock_data = OrderedDict()
        stock_data['id'] = 1
        stock_data.update(data)
        with open(DB_FILE_PATH, 'w') as file:
            json.dump([stock_data], file, indent=4)

def read_from_db():
    try:
        with open(DB_FILE_PATH, 'r') as file:
            return json.load(file)
        
    except  json.JSONDecodeError:
        print("Error decoding JSON. The file might be corrupted.")
        return []
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
                            'lineTouch':form.cleaned_data['lineTouch'],
                            'lineCross':form.cleaned_data['lineCross'],
                            
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

