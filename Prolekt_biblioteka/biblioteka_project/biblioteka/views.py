from django.shortcuts import render
from django.http import HttpResponse

from biblioteka.forms import RegistrationForm
from .forms import izmenen
from .forms import new_book
import sqlite3
import random
import re



def index(request):
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()
    cursor.execute("SELECT id,title FROM biblioteka_book")
    all_employees = cursor.fetchall()
    cursor.execute("SELECT id FROM biblioteka_book")
    id = cursor.fetchall()
    arr = []
    i = 0
    id = [item[0] for item in id]
    print(id)
    for employee in all_employees:
        slovar = {}
        slovar['id'] = id[i]
        slovar['bok'] = employee
        t = slovar
        arr.append(t)
        print(arr)
        slovar = {}
        i += 1
    spisok = {'book': arr}
    print(spisok)
    con.close()
    return render(request, 'Html_osnova.html', spisok)


def udalen(request):
    i = 0
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            nomer = form.cleaned_data['nomer']
            con = sqlite3.connect('db.sqlite3')
            cursor = con.cursor()
            sql_delete_query = ""f"DELETE from biblioteka_book where id = {nomer}"""
            cursor.execute(sql_delete_query)
            con.commit()
            print("Запись успешно удалена")
            cursor.close()
            print(nomer)
            if i == 1:
                return render(request, 'Html_forms_udaleni.html')
    else:
        form = RegistrationForm()
    return render(request, 'Html_forms_udaleni.html',{'form': form})


def dobavlen(request):
    i = 0
    form = new_book()
    if request.method == "POST":
        form = new_book(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            opisanie = form.cleaned_data['opisanie']
            date = form.cleaned_data['date']
            id = random.randint(10, 1000)
            print(title ,author ,opisanie ,date , id)
            con = sqlite3.connect('db.sqlite3')
            cursor = con.cursor()
            sqlite_insert_query = f"""INSERT INTO biblioteka_book
                                      (id, title, author, opisanie, date)
                                      VALUES
                                      ({id}, '{title}', '{author}', '{opisanie}', '{date}');"""
            cursor.execute(sqlite_insert_query)
            con.commit()
            cursor.close()
            if i == 1:
                return render(request, 'new_book.html', {'form': form})

    return render(request, 'new_book.html', {'form': form})


def izmenenie(request):
    form = izmenen()
    if request.method == "POST":
        form = izmenen(request.POST)
        if form.is_valid():
            id_book = form.cleaned_data['id_book']
            element = form.cleaned_data['element']
            na_cho = form.cleaned_data['na_cho']
            print(id_book,element, na_cho)
            y = 0
            if int(element) == 1:
                y = 'title'
            elif int(element) == 2:
                y = 'author'
            elif int(element) == 3:
                y = 'opisanie'
            con = sqlite3.connect('db.sqlite3')
            cursor = con.cursor()
            sql_update_query = f"""Update biblioteka_book set {y} = '{na_cho}' where id = {int(id_book)}"""
            cursor.execute(sql_update_query)
            con.commit()
            cursor.close()
            return render(request, 'izmenie.html', {'form': form})
    return render(request, 'izmenie.html', {'form': form})


def podrobn(request, book_id):
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM biblioteka_book WHERE id = {book_id}")
    podr = cursor.fetchall()
    con.commit()
    for i in podr:
        podr = list(i)
    print(podr)
    cursor.close()
    book_info = {'id': podr[0],'title': podr[1], 'author': podr[2], 'opisanie': podr[3], 'date': podr[4]}
    return render(request, 'podrob.html', book_info)


