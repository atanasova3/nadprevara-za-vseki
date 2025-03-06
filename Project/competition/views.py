from django.shortcuts import render
import httpx
import os
def index(request):

 return render(request, "index.html")


def sustezaniq(request):
    return render(request, "sustezaniq.html")
def mathematics(request):
    import google.generativeai as genai
    genai.configure(api_key="AIzaSyBhoq8jV_jMZ6cbRXOlp0LMrziH_ticvao")
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(
        "Намери състезания,олимпиади по математика в България и ги форматирай: дд-мм-гггг, град. Дай го s HTML tagove, без допълнителен текст, само информацията.")

    context = {
        "predmet": "Matematika",
        "test": "Test",
        "otgovor": response.text[7:-3], # remove ```html at the front and ``` at the end
    }

    return render(request, "matematika.html", context)
def bel(request):
    import google.generativeai as genai
    genai.configure(api_key="AIzaSyBhoq8jV_jMZ6cbRXOlp0LMrziH_ticvao")
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(
        "Намери състезания,олимпиади по Български  в България и ги форматирай: дд-мм-гггг, град. Дай го s HTML tagove, без допълнителен текст, само информацията.")

    context = {
        "predmet": "bulgarski",
        "test": "Test",
        "otgovor": response.text[7:-3],  # remove ```html at the front and ``` at the end
    }

    return render(request, "bel.html",context)
def kalendar(request):
    return render(request, "kalendar.html")
def ang(request):
    return render(request, "ang.html")
def himiq(request):
    return render(request, "himiq.html")
def geo(request):
    return render(request, "geo.html")
def istoriq(request):
    return render(request, "istoriq.html")
def bio(request):
    return render(request, "bio.html")
def fizika(request):
    return render(request, "fizika.html")
def it(request):
    return render(request, "it.html")


