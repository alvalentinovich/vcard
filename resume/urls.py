from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^resume/$', views.resume_list, name='resume_list'),
    url(r'^resume/(?P<pk>\d+)/$', views.resume_detail, name='resume_detail'),
    url(r'^resume/new/$', views.resume_new, name='resume_new'),
    url(r'^resume/(?P<pk>\d+)/edit/$', views.resume_edit, name='resume_edit'),
    url(r'^resume/drafts/$', views.resume_draft_list, name='resume_draft_list'),
    url(r'^resume/(?P<pk>\d+)/publish/$', views.resume_publish, name='resume_publish'),
    url(r'^resume/(?P<pk>\d+)/remove/$', views.resume_remove, name='resume_remove'),
    url(r'^resume/(?P<pk>\d+)/offer/$', views.add_offer_to_resume, name='add_offer_to_resume'),
    url(r'^resume/offer/(?P<pk>\d+)/approve/$', views.offer_approve, name='offer_approve'),
    url(r'^resume/offer/(?P<pk>\d+)/remove/$', views.offer_remove, name='offer_remove'),
]
