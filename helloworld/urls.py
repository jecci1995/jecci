from django.conf.urls import url
from django.urls import path
from . import view,mysql_db,index,democtl


urlpatterns = [
    #path('hello/',view.hello),
    #path('testdb/',testdb.testdb),
    #path('search/',search.search),
    #path('search-form/',search.search_from),
    #url(r'^index/$', view.hello),
    url(r'^$', index.login),
    ##html-rule
    url(r'^login.html$', index.login),
    url(r'^index.html$', view.hello),
    url(r'^index-body.html$', index.index_body),
    url(r'^task-console-list.html$', index.task_console_list),
    url(r'^task-console-add.html$', index.task_console_add),
    url(r'^task-console-con.html$', index.task_console_con),
    url(r'^user-console-add.html$', index.user_console_add),
    url(r'^user-console-list.html$', index.user_console_list),
    url(r'^demo-console.html$', index.demo_console),
    url(r'^demo-console-history.html$', index.demo_console_history),
    url(r'^demo-console-add.html$', index.demo_console_add),


    ##form-rule-add
    url(r'^task_form_action$', mysql_db.taskdb),
    url(r'^task_table_action$', mysql_db.tasklist),
    url(r'^user_form_action$', mysql_db.useradddb),
    url(r'^user_table_action$', mysql_db.userlist),
    url(r'^democtl_list_action$', mysql_db.democtllist),
    url(r'^demoste_list_action$', mysql_db.demostelist),
    url(r'^demo_form_action$', mysql_db.democtladddb),

    ##del-rule
    url(r'^user_del_action$', mysql_db.userdelaction),
    url(r'^task_del_action$', mysql_db.taskdelaction),
    url(r'^democtl_del_action$', mysql_db.democtldelaction),

    ##democtl-rule
    url(r'^democtl_run_action$', democtl.democtl_run_action),
    url(r'^democtl_stop_action$', democtl.democtl_stop_action),
    url(r'^democtl_reload_action$', democtl.democtl_reload_action),




    ##location-rule
    url(r'^login/$', view.login),
    url(r'^hello.html$', view.hello),

]
