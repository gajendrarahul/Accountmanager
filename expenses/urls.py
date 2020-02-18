from django.urls import path
from .views import ExpensesAddView,ExpensesCategoryView,ExpensesView,EditExpensesView,DeleteExpenses
urlpatterns = [
    path('expenses_category/',ExpensesCategoryView.as_view(), name='expenses_category_view'),
    path('expenses_add/', ExpensesAddView.as_view(), name='expenses_add'),
    path('edit-expenses/<slug:slug>',EditExpensesView, name='edit_expenses'),
    path('expenses/',ExpensesView.as_view(), name='expenses_view'),
    path('expenses-dalete/<slug:slug>',DeleteExpenses, name='delete_expenses'),


]