# **SETUP 

> apps.py
>> class AppConfig(Appconfig):
>> 
>> name = 'App Name'
> 
>> def ready(self):
>>
>> import appname.Signals

>__init__.py
>>
>> default_app_config='appname.apps.AppConfig

#### create signals.py file 


*** Documentation ***
# Signals
***
>the signals are utils that allow as to associate events with actions

>signals allow certain senders to notify a set of receivers that some action has taken place

# Built In Signals

1) Login And Logout Signals
2) Management Signals
3) Request/Response Signals
4) Test Signals
5) Database Wrappers


* Receiver function: this function takes sender arguments along with keyword args
***
    def reciver_fun(sender, request, user, **kwargs)
        pass

* Connectiog/Registering Reciver Function
* thir two ways
1) Manual Connect Router: reg a receiver function using the
   #### signal.connect()
   > signal.connect(receiver_fun, sender=None, weak=True, dispatch_uid=None)
   
2) Decorator
   > @receiver(signal or list of signals, sender)
    

# Custom Signals
#### all signals are django.sidpatch.signals instance

### sending signals 
1) signal.send(sender, **kwargs)
2) signal.send_robust(sender, ** kwargs)

   | Function      | Description               |
   |---------------|---------------------------|
   | send          | Does not catch exceptions |
   | send_robust   | All errors are catch      |


### disconnecting signal

   > signal.disconnect(reciver=None, sender=None, dispatch_uid=None)

 #signals.py
> 
> import signals
> import receiver
> notification = signal(providing_args=["request","user"])

> @receiver(notification)
> def show(sender, **kwargs):
>     print(sender)

 #views.py

> #import signal file
> 
>  def home(request):
>     signals.notification.sent(sender=None)
>     request=request, user=['vinayak','anand']
>     return render.......


