# Backend
**Backend** is the backend and database of a website by the name of **Market Place**, **backend** provide APIs to front end of this website.
Find the frontend and more about this website here: https://github.com/zahra-raha/frontend

**Market Place** is a safe and unique place, where sellers can easily advertise thier second handed items. Our mission is to help people find thier needed items and contact to the seller through prepared from. Market Place launched in February 2023 as Django only website and launched in June 2023 with React/Django.



# Super Admin credentials
1. Admin:
  - Username : admin
  - Password : zahra098
2. User:
  - Username: user
  - Password: zahra098

Deployed link : https://backend-market.herokuapp.com/

# Database
There is two custom apps designed here, Userrofile and Post; Userprofile contain profile model and post app contain Post, Post category, Post comment and Inbox.

Here is the ER diagram:
![ER diagram](https://github.com/zahra-raha/Backend/er.jpeg)


# Profile resource APIs
- ^profile/$ [name='profile-list']
- ^profile\.(?P<format>[a-z0-9]+)/?$ [name='profile-list']
- ^profile/(?P<pk>[^/.]+)/$ [name='profile-detail']
- ^profile/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='profile-detail']

# Post resource APIs
- ^post/$ [name='post-list']
- ^post\.(?P<format>[a-z0-9]+)/?$ [name='post-list']
- ^post/(?P<pk>[^/.]+)/$ [name='post-detail']
- ^post/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='post-detail']
- ^post-categories/$ [name='post-cats-list']
- ^post-categories\.(?P<format>[a-z0-9]+)/?$ [name='post-cats-list']
- ^post-categories/(?P<pk>[^/.]+)/$ [name='post-cats-detail']
- ^post-categories/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='post-cats-detail']
- ^post-comments/$ [name='post-comments-list']
- ^post-comments\.(?P<format>[a-z0-9]+)/?$ [name='post-comments-list']
- ^post-comments/(?P<pk>[^/.]+)/$ [name='post-comments-detail']
- ^post-comments/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='post-comments-detail']
- ^inbox/$ [name='inbox-list']
- ^inbox\.(?P<format>[a-z0-9]+)/?$ [name='inbox-list']
- ^inbox/(?P<pk>[^/.]+)/$ [name='inbox-detail']
- ^inbox/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='inbox-detail']

# Others APIs
- admin/
- api-token-auth/
- ^$ [name='api-root']
- user/<int:pk>/ [name='user']
- register/ [name='auth_register']
- ^media/(?P<path>.*)$

### User Goals

- To connect thier website to this backend 
- To advertise his items to sell and find prospective customers

### Developer Goals

- To help people in yard sales
- To create a fully functional API using best technologies 



# Languages

- [Python3](https://www.python.org/)

# Technologies

**Libraries**
- [Django](https://www.djangoproject.com/)
Python web framework
- [Django Restframework](https://www.django-rest-framework.org/)
Django REST framework is a powerful and flexible toolkit for building Web APIs

**Database**
- [sqlite3](https://www.sqlite.org/)
Relational database used to store all the persistent data

**IDE**
- [Gitpod](https://gitpod.io/)
Gitpod is used as IDE for this web app

**Deployment**
- [Heroku](https://www.heroku.com/)
Heroku is a platform as a service (PaaS) application that provides developers with hosting and data storage in the cloud. There are many tiers of service, though I used the free one. 


# Testing
## Manual Testing
1. post APIs
  - List posts api is functional &check;
  - Add new post api is functional &check;
  - Delete post api is functional &check;
  - Like/dislike post api is functional &check;
  - Add comment to a post api is functional &check;
  - Contact to seller api is functional &check;
  - Filter posts by category api is functional &check;

2. Userprofile APIs
  - List profiles api is functional &check; 
  - View profile detail api is functional &check; 
  - Update profile detail api is functional &check; 
3. Super Admin
  - Super admin can manage all categories, customer ,messages and advertisement posts.  &check;
  - Super admin can approve advertisements.  &check;

# Deployment to Heroku

  - On Heroku create an account and log in.
  - Goto ci-students team
  - Click ***new*** and ***create new app***.
  - Choose a name for your app, select region and click on ***Create App***
  - Under the ***Settings*** click ***Reveal Config Vars*** and all environment variables:
    - Set DISABLE_COLLECTSTATIC
  - In the local IDE:
    - Pip install dependencies.
    - Create ***requirements.txt*** ($ pip3 freeze --local > requirements.txt)
    - Create a ***Procfile*** (```$ echo web: gunicorn <app_name>.wsgi > Procfile```)
    - Create an evn.py file and add all your environment variables.
    - Create a .gitignore file and add your env.py files
    - Push all the changes
  
  - In Heroku ***Deploy*** Tab, the ***deployment method*** select Github,connect you gethub account if its not already connected
  - Select repository
  - Scroll down to Manual deploy and deploy branch.
  - Once the build is complete, go back to Heroku and click on ***Open App***
 
# Credits
- Tutorials in [Code Institute](https://codeinstitute.net/global/)
- [Stackoverflow website](https://stackoverflow.com/)
- A friend [Ali Aref Mohammadzada](https://github.com/Ali-Aref)