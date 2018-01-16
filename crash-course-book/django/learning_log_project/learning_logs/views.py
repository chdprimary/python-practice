from django.shortcuts import render, redirect
from .models import Topic
from learning_logs.forms import TopicForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

def index(request):
    """The home page for learning logs."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    # This 3rd argument below (context) is data to be manipulated by the template
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a topic and its entries."""
    topic = Topic.objects.get(id=topic_id)
    if request.user != topic.owner:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Allows user to create a new topic."""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('/topics/')

    form = TopicForm()
    return render(request, 'learning_logs/new_topic.html', {
        'form': form,
    })