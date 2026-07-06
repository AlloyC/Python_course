from django.urls import path
from .views import homePageThree, homePageTwo, homePageOne, homePageFive, recent, paid, contact, animals, library, correction, AboutView, signup, login, logout

urlpatterns = [
    path('recent', recent, name="recent"),
    path('paid', paid, name="paid"),
    path('contact', contact, name="contact"),
    path('animals', animals, name="animals"),
    path('about_us', AboutView.as_view(), name="about_us"),
    path('home1', homePageOne, name="home1"),
    path('home2', homePageTwo, name="home2"),
    path('home3', homePageThree, name="home3"),
    path('home5', homePageFive, name="home5"),
    path('correction', correction, name="correction"),
    path('library', library, name="library"),
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
]