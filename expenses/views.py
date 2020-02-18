from django.shortcuts import render,redirect
from django.views import View
from .form import ExpensesCategoryForm,ExpensesForm
from expenses.models import ExpensesCategory,Expenses
from django.contrib import messages
# Create your views here.
class ExpensesCategoryView(View):
    template_name = 'expenses_category.html'

    def get(self, request):
        context = {
            'form': ExpensesCategoryForm(),
            'category':ExpensesCategory.objects.filter(user_id=request.user.id)
        }
        return render(request, self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=ExpensesCategoryForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request,messages.SUCCESS,"Expenses category created successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"Sorry error occured!!! try again ")
            return redirect('dashboard')


class ExpensesAddView(View):
    template_name = 'add_expenses.html'

    def get(self,request):
        context = {
            'form': ExpensesForm(id=request.user.id),
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = ExpensesForm(request.user.id, request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "successfully added")
            return redirect('expenses_view')
        else:
            return render(request, self.template_name, context={'form': form})

class ExpensesView(View):
    template_name = 'expenses.html'

    def get(self,request):
        context ={
            'all':Expenses.objects.filter(category__in=ExpensesCategory.objects.filter(user_id=request.user.id)),
        }
        return render(request,self.template_name,context)

def EditExpensesView(request,slug):
    if request.method=="GET":
        context = {
            'form':ExpensesForm(request.user.id,instance=Expenses.objects.get(slug=slug))
        }
        return render(request,'edit_expenses.html',context)
    else:
        form = ExpensesForm(request.user.id, request.POST, request.FILES or None, instance=Expenses.objects.get(slug=slug))
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'expenses Edited successfully')
            return redirect('expenses_view')
        else:
            messages.add_message(request,messages.ERROR,'Sorry error occured.... Try again!!!')
            return render(request,'edit_expenses.html', {'form':form})

def DeleteExpenses(request,slug):
    expenses = Expenses.objects.get(slug=slug)
    expenses.delete()
    messages.add_message(request,messages.SUCCESS,'Expenses deleted successfully')
    return redirect('expenses_view')