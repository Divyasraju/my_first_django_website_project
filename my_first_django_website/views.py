from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def count_page(request):
    text = request.GET["usertext"]
    char_len = len(text)
    words_list = text.split()

    word_dictionary = {}

    for word in words_list:
        if word in word_dictionary.keys():
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'count.html', {"text":text, "text_len":char_len, "words_len" : len(words_list), "word_dictionary": word_dictionary})