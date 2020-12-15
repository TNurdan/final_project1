from django.shortcuts import render

# Create your views here.
from .models import Position, Player, Club

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_players=Player.objects.all().count()
    num_clubs=Club.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    # status
    num_positions=Position.objects.count()
    # Метод 'all()' применен по умолчанию.
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_players':num_players,'num_clubs':num_clubs, 'num_positions':num_positions, 'num_visits':num_visits}, # num_visits appended
    )
from django.views import generic

class PlayerListView(generic.ListView):
    model = Player
    paginate_by = 2
class PlayerDetailView(generic.DetailView):
    model = Player
    paginate_by = 10

class ClubListView(generic.ListView):
    model = Club
    paginate_by = 10
def ClubDetailView(request, pk):
    club = Club.objects.get(pk=pk)
    players = Player.objects.all()
    return render(request, "catalog/club_detail.html", context = {"club": club, "players": players})
from django.views.generic import View    
from django.contrib.auth.mixins import LoginRequiredMixin
class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'