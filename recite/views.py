from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Words

def index(request):
    one = Words.objects.order_by("?").first()
    return render(request, "recite/index.html", locals())

def hans(request):
    word = request.GET.get('word')
    one = get_object_or_404(Words, word = word)
    context = {}
    context['hans'] = one.hans
    return JsonResponse(context)
