from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookCreate
from django.http import HttpResponse

#DataFlair
def index(request):
    Books = Book.objects.all()
    return render(request, 'project2/books.html', {'Books': Books})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'project2/upload_form.html', {'upload_form':upload})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        selected = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = selected)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'project2/upload_form.html', {'upload_form':book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        selected = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    selected.delete()
    return redirect('index')

def send_message(request):
    #send_mail(subject='Given subject', message='Here is my message', from_email = settings.EMAIL_HOST_USER, recipient_list=["almas.kenes220702  @gmail.com"])
    email = EmailMessage(
        'Hello', 'Body', settings.EMAIL_HOST_USER, ["almas.kenes220702@gmail.com"]
    )
    email.send(fail_silently=False)
    return render(request, 'project2/success.html')
