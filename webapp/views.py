from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.template import loader
import github
import sqlite3
import pandas as pd
import datetime
'''

This is the Problem related to Github API usage which you can find on https://developer.github.com/v3/

1. Create API for searching the Users.
2. Go through the Documentation and have provision of filtering the user available in the Api params.
3. As any API call is made, store all user related info in a Django table. You can use any database of your choice.
Table should have only unique users stored, if duplicate entry come, update the user.
4. Show all the stored users in Admin Panel, with image if available as thumbnail.
5. In Admin Panel users can be searched on the basis date of added, there email. Add Filters which you have added the 2 point.
6. Create a Report in Admin Panel of No of users added to the database in a day, week and month. Also, how many search API calls has been made in a day, week and month.

Use Django rest Framework if possible.

Make a GitHub project for the above and commit your work after some interval of time or whenever one point is implemented.
https://api.github.com/users/vishakraj25
https://api.github.com/search/users?q=created:2017-11-05+vishakraj25+in:login&type=Users
p.execute("CREATE UNIQUE INDEX idx_webapp_information_idd ON webapp_information (idd);")
'''

# Create your views here.
def index(request):
    '''return HttpResponse('<h3>HelloGit</h3>')'''
    return render(request, 'webapp/home.html',{'info':['If you would like to contact me, please email me.','vishak.shanmu@gmail.com']})
def show(request):
    fil=open('/home/vishakraj25/project/webapp/t.txt','a')
    fil.write('open show')
    fil.close()
    if request.method == 'POST':
        #getting values from post
        username = request.POST.get('name')
        sp()
        l=[]
        g=github.Github()
        users=g.search_users(str(username)+" in:login")
        fil=open('/home/vishakraj25/project/webapp/t.txt','a')
        fil.write('for data'+str(users))
        fil.close()
        for user in users:

              login=user.login
              fil=open('/home/vishakraj25/project/webapp/t.txt','a')
              fil.write(str(login))
              fil.close()
              idd=user.id
              avatar_url=user.avatar_url
              gravatar_id=user.gravatar_id
              url=user.url
              html_url=user.html_url
              followers_url=user.followers_url
              following_url=user.following_url
              gists_url=user.gists_url
              starred_url=user.starred_url
              subscriptions_url=user.subscriptions_url
              organizations_url=user.organizations_url
              repos_url=user.repos_url
              events_url=user.events_url
              received_events_url=user.received_events_url
              typ=user.type
              site_admin=user.site_admin
              name=user.name
              company=user.company
              blog=user.blog
              location=user.location
              email=user.email
              hireable=user.hireable
              bio=user.bio
              public_repos=user.public_repos
              public_gists=user.public_gists
              followers=user.followers
              following=user.following
              created_at=user.created_at
              updated_at=user.updated_at
              date=datetime.datetime.now()
              dat=str(date.year)+'-'+str(date.month)+'-'+str(date.day)
              data=[login, idd, avatar_url, gravatar_id, url, html_url, followers_url, following_url, gists_url, starred_url, subscriptions_url, organizations_url, repos_url, events_url, received_events_url,typ,site_admin, name, company, blog, location, email, hireable, bio, public_repos, public_gists, followers, following, created_at, updated_at, dat]
              for d in data:
                  if d==None:
                      d='nnone'

              fil=open('/home/vishakraj25/project/webapp/t.txt','a')
              fil.write(str(data))
              fil.close()
              result,error=base(data)

              l.append(data)
              fil=open('/home/vishakraj25/project/webapp/t.txt','a')
              fil.write('l data')
              fil.close()

              fil=open('/home/vishakraj25/project/webapp/t.txt','a')
              fil.write('passed data')
              fil.close()

        #adding the values in a context variable
        title=['login', 'idd',  'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'repos_url', 'events_url', 'received_events_url','type','site_admin', 'name', 'company', 'blog', 'location', 'email', 'hireable', 'bio', 'public_repos', 'public_gists', 'followers', 'following', 'created_at', 'updated_at', 'date']

        context = {
            'result': result,
            'error': error,
            'title': title,
            'l': l,
        }


        #getting our showdata template
        template = loader.get_template('webapp/show.html')

        #returing the template
        return HttpResponse(template.render(context, request))
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('webapp/home.html')

def base( data):
    from django.db import connection, transaction
    try:
        cur=connection.cursor()
        if cur.execute('INSERT OR REPLACE INTO webapp_information(login, idd, avatar_url, gravatar_id, url, html_url, followers_url, following_url, gists_url, starred_url, subscriptions_url, organizations_url, repos_url, events_url, received_events_url,typ,site_admin, name, company, blog, location, email, hireable, bio, public_repos, public_gists, followers, following, created_at, updated_at, dat) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',data):
            fil=open('/home/vishakraj25/project/webapp/t.txt','a')
            fil.write('INSERT')
            fil.close()


        connection.connection.commit()
        result='Good'
        error='None'
        '''da=pd.read_sql_querry("'SElECT * FROM information WHERE id =?',(data[i])",con)'''

    except sqlite3.Error:
        if connection:
            error='Error Made..Rolling Back..'
            transaction.rollback()
            result='rollback'
            error='None'
            fil=open('/home/vishakraj25/project/webapp/t.txt','a')
            fil.write('ERROR IF')
            fil.close()
        else:
            error='None'
            fil=open('/home/vishakraj25/project/webapp/t.txt','a')
            fil.write('ERROR ELSE')
            fil.close()
            result='rollback'
    finally:
        if connection:
            connection.close()
            result='finally'
            error='None'
        fil=open('/home/vishakraj25/project/webapp/t.txt','a')
        fil.write('open final')
        fil.close()
    return(result,error)

def sp():
    from django.db import connection, transaction
    try:
        cur=connection.cursor()

        date=datetime.datetime.now()
        dat=str(date.year)+'-'+str(date.month)+'-'+str(date.day)
        cur.execute('INSERT INTO webapp_sapi(dat) VALUES(%s)',[dat])
        connection.connection.commit()

    except sqlite3.Error:
        if connection:
            error='Error Made..Rolling Back..'
            transaction.rollback()
            result='rollback'
            error='None'
        else:
            error='None'
    finally:
        if connection:
            connection.close()
            result='finally'
            error='None'
