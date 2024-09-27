from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item


# Create your views here.
def home(request):
    if request.method == "POST":
        item_text = request.POST.get("item_text", "")
        item = Item(item_text=item_text)
        item.save()
        return redirect("/")

    items = Item.objects.all()
    return render(
        request, "lists/home.html", {"items": items}
    )
