__all__ = ['controller']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
Js('use strict')
var.get('controller').get('js')
pass


# Add lib to the module scope
controller = var.to_python()