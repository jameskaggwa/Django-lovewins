from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'law/index.html', {'title': 'law'})
def about(request):
    return render(request, 'law/about.html', {'title': 'About'})
def community(request):
    return render(request, 'law/community.html', {'title': 'Community'})
def events(request):
    return render(request, 'law/events.html', {'title': 'Events'})
def gallery(request):
    return render(request, 'law/gallery.html', {'title': 'Gallery'})
def projects(request):
    return render(request, 'law/projects.html', {'title': 'Projects'})
def chat(request):
    return render(request, 'law/chat.html', {'title': 'Chat'})
