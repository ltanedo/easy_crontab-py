# Easy Crontab
> only works with bash and zsh on unix (linux and mac).  

A python library to rapidly add and remove and view crontab jovs in unix (linux and mac).
[ [PyPi Link](https://pypi.org/project/easy-cron/0.1/) ]


### Example Usage Below

```
import easy_cron as cron


""" 
get cron list
================
 - input  : None
 - output : list[list]
"""
cron = cron.get_cron_list()


""" 
add job
================
 - input  : (dict) schedule   # keys ["minute", "hour, "day_monthly", "month", "day_weekly"]
            (str)  command  
 - output : None
"""
command  = "python3 example.py"
schedule = {
    "minute"       : , 
    "hour          : , 
    "day_monthly"  : , 
    "month"        : , 
    "day_weekly"   : ,
}
cron.add_job(schedule, command)

""" 
remove job
================
 - input  : (str) command, 
 - output : None
"""
cron.remove_job(""python3 example.py)
```
