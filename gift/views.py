from django.db.models import Avg
from django.shortcuts import render, redirect

from .models import Ideas, Comments
from .forms import CommentForm, IdeaForm
from django.contrib.auth.decorators import login_required


@login_required()
def frontpage(request):
    ideas = Ideas.objects.all()
    tabrate = []
    for idea in ideas:
        coco = Comments.objects.filter(idea_id=idea.id)
        if coco:
            tabrate.append(round(coco.aggregate(Avg('rate')).get('rate__avg'), 1))
        else:
            tabrate.append('?')

    return render(request, 'idkdo/frontpage.html', {'ideas': ideas, 'tabrate': tabrate})


@login_required()
def idea_detail(request, slug):
    idea = Ideas.objects.get(slug=slug)
    user = request.user

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.idea = idea
            comment.save()

            return redirect('idea_detail', slug=idea.slug)
    else:
        form = CommentForm()

    return render(request, 'idkdo/idea_detail.html', {'idea': idea, 'form': form})


@login_required()
def idea_creation(request):
    user = request.user
    form = IdeaForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            form.instance.user = user
            form.save()

            return redirect('frontpage')
    else:
        form = IdeaForm()

    return render(request, 'idkdo/ideacreation.html', {'idea': form, 'form': form})