

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import Lesson


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        load_section = request.path.split('/')[-2]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        if load_section == 'courses':
            slug = request.path.split('/')[-1]
            context['lesson'] = find_lesson(slug)
            if context['lesson'] is None:
                html_template = loader.get_template('home/page-404.html')
                return HttpResponse(html_template.render(context, request))

            lesson = find_lesson(slug)
            return render(request, 'home/course-page.html', {'lesson': lesson})

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def find_lesson(slug):
    try:
        return Lesson.objects.get(slug=slug)
    except Lesson.DoesNotExist:
        return None
