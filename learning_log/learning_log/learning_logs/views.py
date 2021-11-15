from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth import logout
# Create your views here.


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    # show a single topic and all its entries
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    # add a new topic
    if request.method != 'POST':
        # no data submitted create a blank form
        form = TopicForm()
    else:
        # POST data submitted process data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(requests, topic_id):
    # add a new entry for a particular topic
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # no data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submittedl process it
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    # edit an existing entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # post data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def logout_view(request):
    # log out the user
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
