from django.shortcuts import render
from django.http import HttpResponse
import random


def generate_randam_numbers() : 
    random_range_start = random.randint(1 , 10)
    random_range_end = random.randint(11 , 20) 
    random_ans = random.randint(random_range_start,random_range_end)
    print(random_ans)

    context={
        "random_range_start" : random_range_start , 
        "random_range_end" : random_range_end ,
        "random_ans" : random_ans
    }
    return context



def main_page (request) :
    if "random_ans"  not in request.session : 
         context =generate_randam_numbers()
         request.session["context"] =context 
         request.session["random_ans"] =context["random_ans"]
         request.session["random_range_start"] =context["random_range_start"]
         request.session["random_range_end"] =context["random_range_end"]

    else : 
        context = request.session["context"]




    return render (request , "guess.html" , context )





def change_guess(request) :
    context = generate_randam_numbers()
    request.session["random_ans"] =context["random_ans"]
    request.session["context"]  = context   
    return render(request , "reset_game.html" ,context)



def display_answer (request) :
    value = request.GET.get("inp" ,None)
    if value :
        if int(value) == request.session["random_ans"] :         
            return HttpResponse ('<div id="feedback" class="alert alert-success" role="alert">Correct !</div>')

        else:
            if int(value) > request.session["random_ans"] :
                return HttpResponse ('<div id="feedback" class="alert alert-danger" role="alert">Wrong Answer ,  The number is smaller !</div>')
            else :
                return HttpResponse ('<div id="feedback" class="alert alert-danger" role="alert">Wrong Answer ,  The number is greater !</div>')

        

    else : 
        return HttpResponse ('<div id="feedback" class="alert alert-warning" role="alert">Make your guess!</div>')

