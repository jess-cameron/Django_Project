from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import StoryForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import NewsStory, UserFavorite


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['is_favorite'] = request.user.userfavorite_set.filter(news_story=context['story']).exists()
        return self.render_to_response(context)

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def add_favorite(request, news_story_id):
    news_story = get_object_or_404(NewsStory, id=news_story_id)
    request.user.userfavorite_set.get_or_create(news_story=news_story)
    # return redirect('news_detail', news_story_id=news_story_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def remove_favorite(request, news_story_id):
    news_story = get_object_or_404(NewsStory, id=news_story_id)
    request.user.userfavorite_set.filter(news_story=news_story).delete()
    # return redirect('news_detail', news_story_id=news_story_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def FavoriteView(request):
    new = NewsStory.objects.filter(favorited_by=request.user)
    # return render(request,'users/favorites.html', {'favorite_stories': new})
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def index_view(request):
        context = {
            "table_list": ProjectProfile.objects.all(),
            "title": "Table_List"
    }
        return render(request, 'index.html', context)