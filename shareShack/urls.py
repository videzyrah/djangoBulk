from django.conf.urls import url
from shareShack import views as sS_views
from shareShack.views import AddDonation, CheckOut
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^$', sS_views.staff, name = 'staffboard'),

    url(r'^borrowers/$', sS_views.borrowers, name = 'borrowerList'),
    url(r'^(?P<borrower_id>\d+)/$', sS_views.borrower),

    url(r'^items/$', sS_views.items, name = 'itemList'),
    url(r'^item/(?P<item_id>\d+)/$', sS_views.item, name = 'item'),
    url(r'^checkedoutitems/$', sS_views.checkedOutItems, name = 'checkedOutItems'),
    url(r'^addDonation/$', AddDonation.as_view(), name ='addDonation'),
    url(r'^checkout/(?P<item_id>\d+)$', CheckOut.as_view(), name ='checkOut')


]
