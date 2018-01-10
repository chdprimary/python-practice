from django.shortcuts import render, redirect
from .models import Topic
from learning_logs.forms import TopicForm

def index(request):
    """The home page for learning logs."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    # This 3rd argument below (context) is data to be manipulated by the template
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a topic and its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Allows user to create a new topic."""
    if request.method == 'POST':
        topic = TopicForm(request.POST)
        if topic.is_valid():
            topic.save()
            return redirect('/topics/')

    topic = TopicForm()
    return render(request, 'learning_logs/new_topic.html', {
        'topic': topic,
    })