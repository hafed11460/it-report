from account.models import Account
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse



# Create your models here.
class Rapport (models.Model):

    CHEF_DEP = 'CHEF_DEP'
    CHEF_SRV = 'CHEF_SRV'
    DI = 'DI'
    MAIL = 'MAIL'
    TR_INTR = 'TR_INTR'

    YEAR_IN_SCHOOL_CHOICES = [
        (CHEF_DEP, 'Par le Chef departement Informatique'),
        (CHEF_SRV, 'Par le Chef service IR&SI'),
        (DI, 'Par DI'),
        (MAIL, 'Par Mail'),
        (TR_INTR, 'Travaux Internes à La Structure'),
    ]
    author = models.ForeignKey(Account, verbose_name=_("author"), on_delete=models.CASCADE)
    date =  models.DateField(_("date"),  auto_now_add=False)
    starthour =  models.TimeField(_('start hour '))
    endhour =  models.TimeField(_('end hour '))
    title = models.TextField(_("title"))
    description = models.TextField(_("description"))
    equipment = models.TextField(_("equipment"))
    state_befor = models.TextField(_("state befor "),null=True,blank=True)
    state_after = models.TextField(_("state after "))
    device_used = models.TextField(_("Device Used"),null=True,blank=True)
    type_di = models.CharField(_("Type DI"),
        max_length=20,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=TR_INTR,
    )
    # type_di = models.TextField(_("Type DI"))
    n_di = models.TextField(_("N° DI"),null=True,blank=True)
    note = models.TextField(_("note"),null=True,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('rapport:rapport-detail', kwargs={'pk': self.pk})
