from django.views.generic import ListView, CreateView  # new
from django.urls import reverse_lazy  # new

from .forms import PostForm  # new
from .models import Post

from django.shortcuts import render, redirect

import cv2
import os


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


def ara(request):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    img = cv2.imread('media/images/tom.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
    cv2.imwrite('media/images/tom_chnged.jpg', img)

    return render(request, 'final.html', {"img_url": "tom_chnged.jpg"})
