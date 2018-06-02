from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView
from shareShack.forms import DonationForm, CheckOutForm
from shareShack.models import Organization, Borrower, Item
import datetime

# Create your views here.

#staff dashboard
@login_required
def staff(request):
    return render(request, 'dashboard.html')

# borrower list view
@login_required
def borrowers(request):
    borrowers = Borrower.objects.all().order_by('last_name')
    return render(request, 'borrowers.html', { 'borrowers': borrowers })

# borrower detail view
@login_required
def borrower(request, borrower_id):
    borrower = get_object_or_404(Borrower, pk=borrower_id)
    return render(request, 'borrower.html', { 'borrower': borrower})

# borrower list view
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
# item detail view
def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item.html', {'item': item})

@login_required
# checkedout item list
def checkedOutItems(request):
    now = datetime.datetime.utcnow()
    #checkedOut = Item.objects.all().exclude(checked_Out_To = None).order_by('name')
    checkedOut = Item.objects.all().exclude(checked_Out_To = None).filter(due_Back__gte = now.date()).order_by('checked_Out_To')
    overdue = Item.objects.all().filter(due_Back__lte = now.date()).order_by('due_Back')
    return render(request, 'checkedoutitems.html', { 'checkedOut': checkedOut, 'overdue': overdue})


# new item create form
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
                condition = form.cleaned_data.get('condition'),
                donor = form.cleaned_data.get('donor'),
                date_Added = form.cleaned_data.get('date_Added')
            )
            # return HttpResponseRedirect("/shareShack/items")
            return HttpResponseRedirect(reverse('itemList'))
        if form.errors:
            #print(form.errors)
            errors = form.errors

        context = {'form':form, 'errors':errors}
        return render(request, self.template_name, context)

# item update
class CheckOut(UpdateView):
    template_name = "checkOut.html"

    def get(self,request, item_id):
        item_obj = get_object_or_404(Item, pk=item_id)
        form = CheckOutForm(instance=item_obj)
        return render(request, self.template_name, {'form':form, 'item':item_obj })

    def post(self,request, item_id):
        item_obj = get_object_or_404(Item, pk=item_id)
        form = CheckOutForm(request.POST, instance=item_obj)
        errors = None
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('checkedOutItems'))
        if form.errors:
            #print(form.errors)
            errors = form.errors

        context = {'form':form, 'errors':errors}
        return render(request, self.template_name, context)


'''def department(request):
    querySet = Item.objects.all().filter(department__iexact= 'RE')
    return render(request, 'department.html', { 'querySet': querySet}) '''
