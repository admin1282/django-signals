from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

# -------- login signals ----------


@receiver(user_logged_in,sender=User)
def login_success(sender, request, **kwargs):
    print('login success')

@receiver(user_logged_out, sender=User)
def log_out(sender, request, **kwargs):
    print('log out')

@receiver(user_login_failed)
def login_failed(request,**kwargs):
    print("login failed")


# -------- model signals ----------

''''
1] pre_init(sender,args,kwargs):
    pass
    # this signal is sent at the begining of the model __init__() method

2] post_init(sender, instance):
    pass
    # this signed is send at the __init__() method finished
    
3] pre_save(sender, instace, rawm using, update_fields)
    pass
    # this is sent at the begning of model save() method
    
4] post_save(sender, instance, created, raw update_fields)
    pass
    # this is sent at the end of the save() method
    
5] pre_delete(sender, instance, using):
    pass
    # this sent at the begining of delete() methos

6] post_delete(sender, instance, using):
    pass
    # this is sent at the end model delete() method
    
'''



# -------- model signals ----------
'''
1] request_started(sender, environ):
    pass
    # send when django begins processing as http request
    
2] request_finished(sender)
    pass
    # send when django finished delivering http response to the client
    
3] get_request_exception(sender, request):
    pass
'''

# -------- managemant signals ----------

'''
1] pre_migrate(sender,app,config,verbosity,interactive, using, plan, apps):
    pass
    # sent by migrate command 
    
2] post_migrate(sender,app,config,verbosity,interactive, using, plan, apps):
    pass
'''


# -------- test signals ----------
# -------- Database  wrappers ----------

