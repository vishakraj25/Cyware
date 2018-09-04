from django.contrib import admin
from .models import information,sapi
import pytz,datetime
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe


# Register your models here.
class l(admin.ModelAdmin):

    search_fields=['email','created_at']
    change_list_template='admin/webapp/report.html'
    def changelist_view(self, request, extra_context=None):
        today = datetime.datetime.now().replace(tzinfo=pytz.UTC).date()
        uday=information.objects.filter(dat__day=today.day,)
        e = today + datetime.timedelta(days=-7)
        umonth=information.objects.filter(dat__month=today.month,)
        uweek=information.objects.filter(dat__gte=e,)
        sday=sapi.objects.filter(dat__day=today.day,)
        smonth=sapi.objects.filter(dat__month=today.month,)
        sweek=sapi.objects.filter(dat__gte=e,)
        extra_context = {'uday':len(uday),'umonth':len(umonth),'uweek':len(uweek),'sday':len(sday),'smonth':len(smonth),'sweek':len(sweek)}
        return super(l, self).changelist_view(request, extra_context=extra_context)
'''
def t():
        from django.db import connection, transaction
        try:
            fil=open('/home/vishakraj25/project/webapp/t.txt','a')
            fil.write('open base')
            fil.close()
            cur=connection.cursor()
            cur.execute("SElECT * FROM webapp_information WHERE dat  BETWEEN date('now', 'start of day') AND date('now', 'localtime');")
            o=cur.fetchall()
            one=[]
            for oo in o:
                one.append(oo)
            uday=len(one)
            cur.execute("SELECT * FROM webapp_information WHERE dat BETWEEN date('now', '-6 days') AND date('now', 'localtime');")
            o=cur.fetchall()
            one=[]
            for oo in o:
                    one.append(oo)
            uweek=len(one)
            cur.execute("SELECT * FROM webapp_information WHERE dat BETWEEN date('now', 'start of month') AND date('now', 'localtime');")
            o=cur.fetchall()
            one=[]
            for oo in o:
                one.append(oo)
            umonth=len(one)
            cur.execute("SElECT * FROM webapp_sapi WHERE dat  BETWEEN date('now', 'start of day') AND date('now', 'localtime');")
            o=cur.fetchall()
            one=[]
            for oo in o:
                one.append(oo)
            sday=len(one)
            cur.execute("SELECT * FROM webapp_sapi WHERE dat BETWEEN date('now', '-6 days') AND date('now', 'localtime');")
            o=cur.fetchall()
            one=[]
            for oo in o:
                one.append(oo)
            sweek=len(one)
            cur.execute("SELECT * FROM webapp_sapi WHERE dat BETWEEN date('now', 'start of month') AND date('now', 'localtime');")
            o=cur.fetchall()
            one=[]
            for oo in o:
                one.append(oo)
            smonth=len(one)
        except:
            if connection:
                error='Error Made..Rolling Back..'
            else:
                error='None'
        finally:
            if connection:
                connection.close()
        return(uday,umonth,uweek,sday,smonth,sweek)
'''




admin.site.register(information,l)
admin.site.register(sapi)
