from django.urls import path
from .views import HomePageView, BookListView, BookCreateView, SingleBookView, ThanksView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("delete_existing_book/<int:pk>/", BookDeleteView.as_view(), name="bookdelete" ),
    path("update_details_book/<int:pk>/", BookUpdateView.as_view(), name="customerupdate" ),
    path("thankyou/",ThanksView.as_view(), name="thanks" ),
    path("add_new_book/", BookCreateView.as_view(), name="newbook"),
    path("list_all_books/", BookListView.as_view(), name="booklist"),
    path("", HomePageView.as_view(), name="home"),
]

    