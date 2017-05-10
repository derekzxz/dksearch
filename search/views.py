from django.shortcuts import render
from .models import Leader
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm


def index(request):
    leaders_list = Leader.objects.all()
    no_match = False
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            search_filter = cd['search_filter']
            search_text = cd['search_text']
            if search_text:
                if search_filter == 'all':
                    leaders_list = Leader.objects.filter(available=True).filter(Q(person__contains=search_text)|
                                                                               Q(title__iexact=search_text)|
                                                                               Q(company__contains=search_text)|
                                                                               Q(industry__contains=search_text)|
                                                                               Q(geography__contains=search_text))
                if search_filter == 'person':
                    leaders_list = Leader.objects.filter(available=True).filter(person__contains=search_text)
                if search_filter == 'title':
                    leaders_list = Leader.objects.filter(available=True).filter(title__iexact=search_text)
                if search_filter == 'company':
                    leaders_list = Leader.objects.filter(available=True).filter(company__contains=search_text)
                if search_filter == 'industry':
                    leaders_list = Leader.objects.filter(available=True).filter(industry__contains=search_text)
                if search_filter == 'geography':
                    leaders_list = Leader.objects.filter(available=True).filter(geography__contains=search_text)
                if not leaders_list:
                    no_match = True
    else:
        form = SearchForm()
    paginator = Paginator(leaders_list, 5)  # five results per page
    page = request.GET.get('page')
    try:
        leaders = paginator.page(page)
    except PageNotAnInteger:
        leaders = paginator.page(1)
    except EmptyPage:
        leaders = paginator.page(paginator.num_pages)
    if paginator.num_pages > 1:          # if the search results only take one page(that is the number of results is below 5)
        need_pagination = True           # there will be no pagination
    else:
        need_pagination = False
    return render(request, 'index.html', {'form': form, 'leaders': leaders,
                                          'need_pagination': need_pagination, 'no_match': no_match})



