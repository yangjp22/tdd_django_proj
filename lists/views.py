from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.method == "POST":
        return render(request, "lists/home.html", {"new_list_item": request.POST.get("item_text", '')})
    return render(
        request, "lists/home.html", {"new_list_item": request.POST.get("item_text", '')}
    )
