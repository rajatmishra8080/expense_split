from django.shortcuts import render,redirect
from .models import contact,expence
from django.db.models import Sum,Count
from django.http import JsonResponse

# Create your views here.
def home(request):
    out=contact.objects.all()
    context={"out":out}
    return render(request,'home.html',context)

def addcontact(request):
    if request.method=="POST":
        mycontact=contact(
            fname=request.POST["fname"],
            email=request.POST["email"],
            phone = request.POST["phone"],
        )
        if mycontact is not None:
            mycontact.save()
            return redirect('/')
    return render(request,'form.html')

def overview(request):
    try:
        expenses = expence.objects.all().order_by('expenseBy').annotate(total_exp=Sum('expenseAmount'))
        total_expense = expenses.aggregate(total=Sum('expenseAmount'))['total']
        num_people = len(set(expn.expenseBy for expn in expenses))
      
        # Calculate sharing_amount
        sharing_amount = total_expense / num_people
        
        context = {
            'expenses': expenses,
            'total_expense': total_expense,
            'sharing_amount': sharing_amount,
            'num_people' : num_people,  
            }
    except:
            return redirect('error')
    return render(request,'overview.html',context)

def expense(request):
    if request.method=="POST":
        myexpense=expence(
            expenseDate=request.POST["expenseDate"],
            expenseTitle=request.POST["expenseTitle"],
            expenseAmount=request.POST["expenseAmount"],
            expenseBy=request.POST["expenseBy"],
            )
        if myexpense is not None:
            myexpense.save()
            return redirect('overview')
    out=contact.objects.all()
    context={"out":out}
    return render(request,'expense.html',context)

def settle_up_report(request):
    try:
        members_data = expence.objects.values('expenseBy').annotate(total_expense=Sum('expenseAmount'))
        total_members = expence.objects.values('expenseBy').annotate(total=Count('expenseBy'))

        average_expense = sum(member['total_expense'] for member in members_data) / len(total_members)

        settle_up_data = []

        for member_data in members_data:
            expense_by = member_data['expenseBy']
            total_expense = member_data['total_expense']
            settle_amount = average_expense - total_expense
            settle_up_data.append({'expenseBy': expense_by, 'totalExpense': total_expense, 'settleAmount': settle_amount})
    except:
        return redirect('error')
    return render(request, 'settleup.html', {'settle_up_data': settle_up_data})

def reset_records(request):
    expence.objects.all().delete()
    return JsonResponse({'message': 'All records have been reset'})

def error(request):
    return render(request,'error.html')

def simplify_expenses(request):
    expenses = expence.objects.values('expenseBy').annotate(total_expense=Sum('expenseAmount'))
    average_expense = sum(expense['total_expense'] for expense in expenses) / len(expenses)

    simplified_expenses = []

    for expense in expenses:
        expense_by = expense['expenseBy']
        total_expense = expense['total_expense']
        settle_amount = total_expense - average_expense
        simplified_expenses.append({'expenseBy': expense_by, 'settleAmount': settle_amount})

    return render(request, 'simplify_expenses.html', {'simplified_expenses': simplified_expenses})