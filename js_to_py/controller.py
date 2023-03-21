from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
Js('use strict')
(var.get('printer')/var.get('controller').get('js'))
pass
