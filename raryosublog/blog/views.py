from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from blog.models import blogdata
from django.forms import ModelForm


class blogform(ModelForm):
    class Meta:
        model = blogdata
        fields = ('title', 'text', 'date', )

# Create your views here.
def edit(request):
    blogs = blogdata()
    form = None
    if request.method == 'POST':
        form = blogform(request.POST, instance=blogs)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog:show')
        pass
    else:
        form = blogform(instance=blogs)
    return render_to_response('blog/blogedit.html', {'form': form}, context_instance=RequestContext(request))

def show(request):
    blogs = blogdata.objects.all()
    return render_to_response('blog/blogshow.html', {'blogs': blogs}, context_instance=RequestContext(request))
