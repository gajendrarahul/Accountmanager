from django.urls import path
from income.views import IncomeAddView,IncomeCategoryView,IncomeView,EditIncomeView,DeleteIncome
urlpatterns =[
    path('income-category/',IncomeCategoryView.as_view(), name='income_category_view'),
    path('income-add/',IncomeAddView.as_view(), name='income_add'),
    path('edit-income/<slug:slug>',EditIncomeView, name='edit_income'),
    path('income/',IncomeView.as_view(), name='income_view'),
    path('income-delete/<slug:slug>',DeleteIncome, name='delete_income'),

]