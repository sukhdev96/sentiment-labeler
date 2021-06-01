from sentiment_label.models import Sentiment
from django.shortcuts import render, get_object_or_404, redirect
import random


# Create your views here.


def SplashView(request):
    if request.method =='POST':
        print(request.POST.get('name'))
        request.session['labeler'] = request.POST.get('name').lower()
        return redirect('../label/')
    return render(request, "sentiment_label/splash.html")

    

def LabelView(request):
    if request.method =="GET":
        if 'labeler' not in request.session:
            return redirect('/')
        labeler = request.session['labeler']

        queryset = Sentiment.objects.exclude(author_1__contains = str(labeler.lower())).exclude(author_2__contains = str(labeler.lower())).filter(sentiment_3 = '')
        print(queryset)
        try:
            post = random.choice(queryset)
            print(post.content)
            context = {'post': post, 'user':request.session['labeler']}
        except:
            post = {'content':'No Posts Available. Try again Later'}
            context = {'post': post, 'user':request.session['labeler']}
        print('User is: '+request.session['labeler'])
        request.session['post_id'] = post.id
    if request.method =='POST':
        if 'labeler' not in request.session:
            return redirect('/')
        labeler = request.session['labeler']
        post = Sentiment.objects.filter(id = request.session['post_id'])
        post = post[0]
        sentiment = request.POST.get('sentiment')
        if post.author_1 == '' :
            post.author_1=labeler
            post.sentiment_1=sentiment
            post.save()
            return redirect('../label/')
        elif post.author_2 =='' :
            post.author_2=labeler
            post.sentiment_2=sentiment
            post.save()
            return redirect('../label/')
        elif post.author_3 =='' :
            post.author_3=labeler
            post.sentiment_3=sentiment
            post.save()
            return redirect('../label/')
        else:
            print('ERROR. POST ALREADY HAS MAXIMUM OF 3 SENTIMENTS')
            return redirect('../label/')

    return render(request, "sentiment_label/label.html",context)