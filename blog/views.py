from django.shortcuts import render

posts = [
    {
        'author': 'Prithvi Shah',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date': '27/06/24' 
    },
    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date': '26/06/24' 
    }
    
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})