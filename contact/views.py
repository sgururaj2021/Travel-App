from django.shortcuts import render, redirect
from .forms import ContactForm 


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

        else:
            return redirect('/')   
       
    form = ContactForm()
    return render(request, 'contact.html', {'form' : form})



    
    



