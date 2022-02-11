# Easy Environment
> only works with bash and zsh on unix (linux and mac).  

A python library to rapidly set, get, and view local environment variables (currently only for bash and zsh shells in unix).

[ [PyPi Link](https://pypi.org/project/easy-environment/0.1/) ]


### Example Usage Below

```
import easy_environment as environ


""" 
get env dict
================
 - input  : None
 - output : list[dict]
"""
env_dict = environ.get_env_dict()


""" 
get env var
================
 - input  : (str) key
 - output : (str) value
"""
env_dict = environ.get_env("EXAMPLE_KEY")


""" 
set env var
================
 - input  : (str) key, 
            (str) value
 - output : list[dict]
"""
# set env var -> None
env_dict = environ.set_env_var("EXAMPLE_KEY", "EXAMPLE_VALUE)
```
