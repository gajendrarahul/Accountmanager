from django.shortcuts import render,redirect
from django.views import View
from . form import IncomeCategoryForm,IncomeForm
from django.contrib import messages
from income.models import IncomeCategory,Income
# Create your views here.
class IncomeCategoryView(View):
    template_name = 'income_category.html'
    def get(self,request):
        context = {
            'form':IncomeCategoryForm(),
            'category':IncomeCategory.objects.filter(user_id=request.user.id)
        }
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form =IncomeCategoryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request,messages.SUCCESS,'saved successfully')
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,'sorry occured !!!!')
            return redirect('dashboard')

class IncomeAddView(View):
    template_name = 'add_income.html'
    def get(self,request):
        context = {
            'form':IncomeForm(id=request.user.id),
        }
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form = IncomeForm(request.user.id,request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"successfully added")
            return redirect('income_view')
        else:
            return render(request,self.template_name,context={'form':form})

class IncomeView(View):
    template_name = 'income.html'
    def get(self,request):
        context ={
            'all':Income.objects.filter(category__in=IncomeCategory.objects.filter(user_id=request.user.id)),
        }
        return render(request,self.template_name, context)

def EditIncomeView(request,slug):
    if request.method=="GET":
        context = {
            'form':IncomeForm(request.user.id,instance=Income.objects.get(slug=slug))
        }
        return render(request,'edit_income.html',context)
    else:
        form = IncomeForm(request.user.id, request.POST, request.FILES or None , instance=Income.objects.get(slug=slug))
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Income edited successfully')
            return redirect('income_view')
        else:
            messages.add_message(request,messages.ERROR,' Sorry Error Occured')
            return redirect('dashboard')

def DeleteIncome(request,slug):
    income = Income.objects.get(slug=slug)
    income.delete()
    messages.add_message(request,messages.SUCCESS,'Income deleted Successfully')
    return redirect('income_view')