from django.shortcuts import render, redirect, get_object_or_404
from .models import Users


def user_list(request):
    users = Users.objects.all()
    return render(request, "index.html", {'users': users})

def user_detail(request, pk):
    users = get_object_or_404(Users,pk=pk)
    context = {"users":users}
    return render(request, "user_detail.html", context)

def update_user(request, pk):
    user = get_object_or_404(Users, pk=pk)
    if request.method == "POST":
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.save()
        return redirect("app:list")
    return render(request, "index.html", {"user": user})

def add_user(request):
    return render(request, "user_form.html")
    
def create_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        user = Users(name=name, email=email, phone=phone)
        user.save()
        return redirect("app:list")
    return render(request, "index.html")
 
def delete_user(request, pk):
    user = get_object_or_404(Users, pk=pk)       
    user.delete()
    return redirect("app:list")

    