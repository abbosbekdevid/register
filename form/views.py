from django.shortcuts import render
from .models import PersonModel
from django.http import HttpResponse
# Create your views here.




def home_page(request):
    if request.method == "POST":
        print(request.POST)
        full_name = request.POST.get("full_name", "Bunday key topilmadi")
        user_name = request.POST.get("user_name", "Bunday key topilmadi")
        email = request.POST.get("email", "Bunday key topilmadi")
        number = request.POST.get("number", "Bunday key topilmadi")
        password_1 = request.POST.get("password_1", "Bunday key topilmadi")
        password_2 = request.POST.get("password_2", "Bunday key topilmadi")
        gender = request.POST.get("gender", "Bunday key topilmadi")
        print(full_name, email, password_1, password_2)
        
        if password_1 != password_2:
            error = "Parol bir xil emas"
            return render(request, "index.html", {"error": error})
        
        
        # Django ORM code for adding data to database
        PersonModel.objects.create(
            full_name = full_name, 
            user_name = user_name,
            number = number, 
            email = email, 
            password = password_1,
            gender = gender
        )
        return HttpResponse("Succsessfull")
    return render(request, "index.html")
