from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.utils.datetime_safe import datetime
from django.db.models import Q

from blogs.forms import PostForm
from blogs.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'blogs/home.html'

    def get_queryset(self):
        result = super().get_queryset()

        if self.request.user.is_authenticated:
            return result.filter(Q(owner=self.request.user) | Q(pub_date__lte=datetime.now()))
        else:
            return result.filter(pub_date__lte=datetime.now()).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Wordplease'
        context['claim'] = 'Una plataforma de blogs hecha con Django'
        return context


class BlogsView(ListView):

    def get(self, request):
        users = User.objects.all()
        context = {'users': users}
        return render(request, 'blogs/blogs.html', context)


class BlogView(ListView):
    model = Post
    template_name = 'blogs/posts.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(owner__username=self.kwargs['owner']).order_by('-pub_date')
        else:
            return Post.objects.filter(owner__username=self.kwargs['owner'], pub_date__lte=datetime.now()).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog de ' + self.kwargs['owner']
        context['claim'] = 'Blog con los posts creados por ' + self.kwargs['owner']
        return context


class PostView(View):

    def get(self, request, pk, owner):
        """
        Muestra un post
        :param request: objeto HttpRequest
        :param pk: identificador del post
        :param username: identificador del dueño
        :return: HttpResponse con la respuesta
        """

        try:
            if self.request.user.is_authenticated:
                post = Post.objects.select_related().get(pk=pk)
            else:
                post = Post.objects.filter(pub_date__lte=datetime.now()).select_related().get(pk=pk)
            owner = User.objects.get(username=owner)
        except Post.DoesNotExist:
            return HttpResponse('No existe la respuesta que buscas', status=404)

        context = {'post': post, 'owner': owner}

        return render(request, 'blogs/post.html', context)


@method_decorator(login_required, name='dispatch')
class PostFormView(View):

    def get(self, request):
        """
        Muestra el formulario para la creacion de un post
        :param request: objeto HttpRequest
        :return: HttpResponse con la respuesta
        """

        form = PostForm()
        context = {'form': form}
        return render(request, 'blogs/form.html', context)

    def post(self, request):
        """
        Procesa el formulario para la crear el anuncio
        :param request: objeto HttpRequest
        :return: HttpResponse con la respuesta
        """

        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            messages.success(request, 'Anuncio creado correctamente')
        context = {'form': form}
        return render(request, 'blogs/form.html', context)
