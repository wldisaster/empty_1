from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .models import Theme, Content
from .forms import ThemeForm, ContentForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    """博客主页"""
    return render(request, 'simple_blogs/index.html')


@login_required
def themes(request):
    """显示所有主题"""
    themes = Theme.objects.filter(owner=request.user).order_by('date_added')
    context = {'themes': themes}
    return render(request, 'simple_blogs/themes.html', context)


@login_required
def theme(request, theme_id):
    """显示主题及其内容"""
    theme = Theme.objects.get(id=theme_id)
    # 确认请求主题属于当前用户
    if theme.owner != request.user:
        raise Http404
    contents = theme.content_set.order_by('-date_added')
    context = {'theme': theme, 'contents': contents}
    return render(request, 'simple_blogs/theme.html', context)


@login_required
def new_theme(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据，创建新表单
        form = ThemeForm()
    else:
        # POST提交的数据，对数据进行处理
        form = ThemeForm(request.POST)
        if form.is_valid():
            new_theme = form.save(commit=False)
            new_theme.owner = request.user
            new_theme.save()
            return HttpResponseRedirect(reverse('simple_blogs:themes'))

    context = {'form': form}
    return render(request, 'simple_blogs/new_theme.html', context)


@login_required
def new_content(request, theme_id):
    """在特定主题中添加新内容"""
    theme = Theme.objects.get(id=theme_id)

    if request.method != 'POST':
        # 未提交数据，创建新表单
        form = ContentForm()
    else:
        # POST提交的数据，对数据进行处理
        form = ContentForm(data=request.POST)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.theme = theme
            new_content.save()
            return HttpResponseRedirect(reverse('simple_blogs:theme', args=[theme_id]))

    context = {'theme': theme, 'form': form}
    return render(request, 'simple_blogs/new_content.html', context)


@login_required
def edit_content(request, content_id):
    """编辑内容"""
    content = Content.objects.get(id=content_id)
    theme = content.theme
    if theme.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前内容填充表单
        form = ContentForm(instance=content)
    else:
        # POST提交的数据，对数据进行处理
        form = ContentForm(instance=content, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('simple_blogs:theme', args=[theme.id]))

    context = {'content': content, 'theme': theme, 'form': form}
    return render(request, 'simple_blogs/edit_content.html', context)
