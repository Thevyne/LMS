from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('student-registration/', views.student_registration, name='student_registration'),
    path('admin-registration/', views.admin_registration, name='admin_registration'),
    path('login/', views.user_login, name='login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path("", views.index, name="index"),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_update/<int:book_id>/', views.update_availability, name='update_availability'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('request_book/<int:book_id>/', views.request_book, name='request_book'),
    path('view_requests/', views.view_requests, name='view_requests'),
    path('available_books/', views.available_books, name='available_books'),
    path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
    path('approved_books/', views.approved_books, name='approved_books'),
    path('librarian/add-category/', views.librarian_add_category, name='add_category'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>/', views.category_books, name='category_books'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('request-book/', views.request_book, name='request_book'),
    path('search-books/', views.search_books, name='search_books'),
    path('view-all-students/', views.view_all_students, name='view_all_students'),
    path('available-books/<int:book_id>/', views.update_available_copies, name='update_copies_available'),
    path('search-students/', views.search_students, name='search_students'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Add other URLs as needed
]
