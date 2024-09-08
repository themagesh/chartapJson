from django.shortcuts import render, redirect
from .forms import PersonForm
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

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person_data = {
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age']
            }
            write_to_db(person_data)
            return redirect('add_person')
        
    else:
        form = PersonForm()
        persons = read_from_db()[-2:] 
       
    return render(request, 'add_person.html', {'form': form,'persons': persons})

def display_name(request):
    persons = read_from_db() 
    return render(request, 'add_person.html', {'persons': persons})

