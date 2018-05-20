from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from shareShack.forms import DonationForm
from shareShack.models import Organization, Borrower, Item, CheckOut, Return
import datetime

# Create your views here.
def borrowers(request):
    borrowers = Borrower.objects.all().order_by('last_name')
    return render(request, 'borrowers.html', { 'borrowers': borrowers })

def borrower(request, borrower_id):
    borrower = get_object_or_404(Borrower, pk=borrower_id)
    return render(request, 'borrower.html', { 'borrower': borrower})

def items(request):
    furniture = Item.objects.all().order_by('name').filter(department__iexact='FU')
    catering = Item.objects.all().order_by('name').filter(department__iexact='CA')
    landscaping = Item.objects.all().order_by('name').filter(department__iexact='LA')
    recreation = Item.objects.all().order_by('name').filter(department__iexact='RE')
    maintenance = Item.objects.all().order_by('name').filter(department__iexact='MA')

    time = datetime.datetime.utcnow()

    farts = "farts"
    context = {'furniture' : furniture,
                'catering' : catering,
                'landscaping' : landscaping,
                'recreation' : recreation,
                'maintenance' : maintenance,
                'time' : time,
                'farts' : farts}


    return render(request, 'items.html', context)

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item.html', { 'item': item})

def checkedOutItems(request):
    now = datetime.datetime.utcnow()
    #checkedOut = Item.objects.all().exclude(checked_Out_To = None).order_by('name')
    checkedOut = Item.objects.all().exclude(checked_Out_To = None).filter(due_Back__gte = now.date()).order_by('checked_Out_To')
    overdue = Item.objects.all().filter(due_Back__lte = now.date()).order_by('due_Back')
    return render(request, 'checkedoutitems.html', { 'checkedOut': checkedOut, 'overdue': overdue})

def dashboard(request):
    return render(request, 'dashboard.html')

class AddDonation(TemplateView):
    template_name = "addDonation.html"

    def get(self,request):
        form = DonationForm()
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = DonationForm(request.POST or None)
        errors = None
        if form.is_valid():
            obj = Item.objects.create(
                department = form.cleaned_data.get('department'),
                writtenId = form.cleaned_data.get('writtenId'),
                name = form.cleaned_data.get('name'),
                date_Added = form.cleaned_data.get('date_Added')
            )
            # return HttpResponseRedirect("/shareShack/items")
            return HttpResponseRedirect(reverse('itemList'))
        if form.errors:
            #print(form.errors)
            errors = form.errors

        context = {'form':form, 'errors':errors}
        return render(request, self.template_name, context)

'''
class UpdateItem(UpdateView):
    template_name = "updateItem.html"

    def get(self,request):
        form = DonationForm()
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = DonationForm(request.POST or None)
        errors = None
        if form.is_valid():
            obj = Item.objects.create(
                department = form.cleaned_data.get('department'),
                writtenId = form.cleaned_data.get('writtenId'),
                name = form.cleaned_data.get('name'),
                date_Added = form.cleaned_data.get('date_Added')
            )
            return HttpResponseRedirect("/shareShack/items")
        if form.errors:
            #print(form.errors)
            errors = form.errors

        context = {'form':form, 'errors':errors}
        return render(request, self.template_name, context)
'''

'''def department(request):
    querySet = Item.objects.all().filter(department__iexact= 'RE')
    return render(request, 'department.html', { 'querySet': querySet}) '''
