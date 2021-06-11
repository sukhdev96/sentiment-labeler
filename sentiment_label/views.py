from sentiment_label.models import Post,Label
from django.shortcuts import render, get_object_or_404, redirect
import random


# Create your views here.


def SplashView(request):
    request.session['error'] = ''
    if request.method =='GET':
        request.session['error'] = 'False'
    if request.method =='POST':
        pf_number = request.POST.get('pf_number')
        if pf_number.startswith("00") and len(pf_number) == 8:
            print(pf_number)
            request.session['labeler'] = pf_number
            return redirect('../label/')
            request.session['error'] = 'False'
        else:
            print('Invalid PF Number')
            request.session['error'] = 'True'
            print(request.session['error'])
    return render(request, "sentiment_label/splash.html", {'error':request.session['error']})

    

def LabelView(request):
    if request.method =="GET":
        if 'labeler' not in request.session:
            return redirect('/')
        labeler = request.session['labeler']
        past_labels = Label.objects.filter(labeler = labeler)
        past_ids = [x.post_ID for x in past_labels]
        print('Past IDs = '+ str(past_ids))
        available_posts = Post.objects.exclude(id__in=past_ids).exclude(no_of_labels__gt=4)
        print(available_posts)
        # queryset = Post.objects.exclude(author_1__contains = str(labeler.lower())).exclude(author_2__contains = str(labeler.lower())).filter(sentiment_3 = '')
        # print(queryset)
        try:
            post = random.choice(available_posts)
            if len(post.content) > 450:
                post_text = post.content[:450] + '.....'
            else:
                post_text = post.content
            print(len(post.content))
            context = {'post': post, 'user':request.session['labeler'], 'post_text': post_text}
            request.session['post_id'] = post.id
        except:
            # post = {'content':'No Posts Available. Try again Later'}
            # print(post)
            post_text = 'No Posts Available. Try again Later'
            context = {'post_text': post_text, 'user':request.session['labeler']}
        print('User is: '+request.session['labeler'])
    if request.method =='POST':
        if 'labeler' not in request.session:
            return redirect('/')
        labeler = request.session['labeler']
        post = Post.objects.filter(id = request.session['post_id'])
        post = post[0]
        sentiment = request.POST.get('sentiment')
        try:
            p = Label(post_ID = request.session['post_id'] , content = post.content, labeler = labeler, sentiment = sentiment)
            p.save()
            post.no_of_labels += 1
            # post.author_1=labeler
            # post.sentiment_1=sentiment
            post.save()
            return redirect('../label/')
        except:
            print('ERROR SUBMITTING')
            return redirect('../label/')
        # elif post.author_3 =='' :
        #     post.author_3=labeler
        #     post.sentiment_3=sentiment
        #     post.save()
        #     return redirect('../label/')
        # else:
        #     print('ERROR SUBMITTING')
        #     # return redirect('../label/')

    return render(request, "sentiment_label/label.html",context)