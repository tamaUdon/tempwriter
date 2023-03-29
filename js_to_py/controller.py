from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['_asyncToGenerator', 'init', '$', 'printer', 'showMessage', 'set58mm', 'pair', 'set80mm', 'printText', '_toConsumableArray', 'cut', 'printImage', 'loadImage'])
@Js
def PyJsHoisted__toConsumableArray_(arr, this, arguments, var=var):
    var = Scope({'arr':arr, 'this':this, 'arguments':arguments}, var)
    var.registers(['arr', 'i', 'arr2'])
    if var.get('Array').callprop('isArray', var.get('arr')):
        #for JS loop
        var.put('i', Js(0.0))
        var.put('arr2', var.get('Array')(var.get('arr').get('length')))
        while (var.get('i')<var.get('arr').get('length')):
            var.get('arr2').put(var.get('i'), var.get('arr').get(var.get('i')))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return var.get('arr2')
    else:
        return var.get('Array').callprop('from', var.get('arr'))
PyJsHoisted__toConsumableArray_.func_name = '_toConsumableArray'
var.put('_toConsumableArray', PyJsHoisted__toConsumableArray_)
@Js
def PyJsHoisted__asyncToGenerator_(fn, this, arguments, var=var):
    var = Scope({'fn':fn, 'this':this, 'arguments':arguments}, var)
    var.registers(['fn'])
    @Js
    def PyJs_anonymous_37_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['gen'])
        var.put('gen', var.get('fn').callprop('apply', var.get(u"this"), var.get('arguments')))
        @Js
        def PyJs_anonymous_38_(resolve, reject, this, arguments, var=var):
            var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
            var.registers(['resolve', 'step', 'reject'])
            @Js
            def PyJsHoisted_step_(key, arg, this, arguments, var=var):
                var = Scope({'key':key, 'arg':arg, 'this':this, 'arguments':arguments}, var)
                var.registers(['key', 'info', 'arg', 'value'])
                try:
                    var.put('info', var.get('gen').callprop(var.get('key'), var.get('arg')))
                    var.put('value', var.get('info').get('value'))
                except PyJsException as PyJsTempException:
                    PyJsHolder_6572726f72_27405766 = var.own.get('error')
                    var.force_own_put('error', PyExceptionToJs(PyJsTempException))
                    try:
                        var.get('reject')(var.get('error'))
                        return var.get('undefined')
                    finally:
                        if PyJsHolder_6572726f72_27405766 is not None:
                            var.own['error'] = PyJsHolder_6572726f72_27405766
                        else:
                            del var.own['error']
                        del PyJsHolder_6572726f72_27405766
                if var.get('info').get('done'):
                    var.get('resolve')(var.get('value'))
                else:
                    @Js
                    def PyJs_anonymous_39_(value, this, arguments, var=var):
                        var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
                        var.registers(['value'])
                        var.get('step')(Js('next'), var.get('value'))
                    PyJs_anonymous_39_._set_name('anonymous')
                    @Js
                    def PyJs_anonymous_40_(err, this, arguments, var=var):
                        var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                        var.registers(['err'])
                        var.get('step')(Js('throw'), var.get('err'))
                    PyJs_anonymous_40_._set_name('anonymous')
                    return var.get('Promise').callprop('resolve', var.get('value')).callprop('then', PyJs_anonymous_39_, PyJs_anonymous_40_)
            PyJsHoisted_step_.func_name = 'step'
            var.put('step', PyJsHoisted_step_)
            pass
            return var.get('step')(Js('next'))
        PyJs_anonymous_38_._set_name('anonymous')
        return var.get('Promise').create(PyJs_anonymous_38_)
    PyJs_anonymous_37_._set_name('anonymous')
    return PyJs_anonymous_37_
PyJsHoisted__asyncToGenerator_.func_name = '_asyncToGenerator'
var.put('_asyncToGenerator', PyJsHoisted__asyncToGenerator_)
@Js
def PyJsHoisted_showMessage_(m, this, arguments, var=var):
    var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['m'])
    var.get('$')(Js('#message')).put('textContent', var.get('m'))
PyJsHoisted_showMessage_.func_name = 'showMessage'
var.put('showMessage', PyJsHoisted_showMessage_)
Js('use strict')
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['_ref'])
    @Js
    def PyJs__callee_1_(txt, this, arguments, var=var):
        var = Scope({'txt':txt, 'this':this, 'arguments':arguments, '_callee':PyJs__callee_1_}, var)
        var.registers(['txt', 'str'])
        pass
        @Js
        def PyJs_InlineNonPyName_2_(_context, this, arguments, var=var):
            var = Scope({'_context':_context, 'this':this, 'arguments':arguments, '_callee$':PyJs_InlineNonPyName_2_}, var)
            var.registers(['_context'])
            while Js(1.0):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('_context').put('prev', var.get('_context').get('next')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.get('_context').put('next', Js(2.0))
                        return var.get('printer').callprop('selectKanjiCode', Js('sjis'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.get('_context').put('next', Js(4.0))
                        return var.get('printer').callprop('enableKanjiMode')
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                        SWITCHED = True
                        var.get('_context').put('next', Js(6.0))
                        return var.get('printer').callprop('selectInternationalCharacter', Js(8))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                        SWITCHED = True
                        var.put('str', var.get('txt'))
                        var.get('_context').put('next', Js(9.0))
                        return var.get('printer').callprop('raw', var.get('Uint8Array').create(var.get('Escpos').get('Printer').callprop('encodeSJIS', var.get('str'))))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
                        SWITCHED = True
                        var.get('_context').put('next', Js(11.0))
                        return var.get('printer').callprop('disableKanjiMode')
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(11.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('end')):
                        SWITCHED = True
                        return var.get('_context').callprop('stop')
                    SWITCHED = True
                    break
        PyJs_InlineNonPyName_2_._set_name('_callee$')
        return var.get('regeneratorRuntime').callprop('wrap', PyJs_InlineNonPyName_2_, var.get('_callee'), var.get(u"this"))
    PyJs__callee_1_._set_name('_callee')
    var.put('_ref', var.get('_asyncToGenerator')(var.get('regeneratorRuntime').callprop('mark', PyJs__callee_1_)))
    @Js
    def PyJs_printText_3_(_x, this, arguments, var=var):
        var = Scope({'_x':_x, 'this':this, 'arguments':arguments, 'printText':PyJs_printText_3_}, var)
        var.registers(['_x'])
        return var.get('_ref').callprop('apply', var.get(u"this"), var.get('arguments'))
    PyJs_printText_3_._set_name('printText')
    return PyJs_printText_3_
PyJs_anonymous_0_._set_name('anonymous')
var.put('printText', PyJs_anonymous_0_())
@Js
def PyJs_anonymous_4_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['_ref2'])
    @Js
    def PyJs__callee2_5_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, '_callee2':PyJs__callee2_5_}, var)
        var.registers([])
        @Js
        def PyJs_InlineNonPyName_6_(_context2, this, arguments, var=var):
            var = Scope({'_context2':_context2, 'this':this, 'arguments':arguments, '_callee2$':PyJs_InlineNonPyName_6_}, var)
            var.registers(['_context2'])
            while Js(1.0):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('_context2').put('prev', var.get('_context2').get('next')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.get('_context2').put('next', Js(2.0))
                        return var.get('printer').callprop('cut')
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('end')):
                        SWITCHED = True
                        return var.get('_context2').callprop('stop')
                    SWITCHED = True
                    break
        PyJs_InlineNonPyName_6_._set_name('_callee2$')
        return var.get('regeneratorRuntime').callprop('wrap', PyJs_InlineNonPyName_6_, var.get('_callee2'), var.get(u"this"))
    PyJs__callee2_5_._set_name('_callee2')
    var.put('_ref2', var.get('_asyncToGenerator')(var.get('regeneratorRuntime').callprop('mark', PyJs__callee2_5_)))
    @Js
    def PyJs_cut_7_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'cut':PyJs_cut_7_}, var)
        var.registers([])
        return var.get('_ref2').callprop('apply', var.get(u"this"), var.get('arguments'))
    PyJs_cut_7_._set_name('cut')
    return PyJs_cut_7_
PyJs_anonymous_4_._set_name('anonymous')
var.put('cut', PyJs_anonymous_4_())
@Js
def PyJs_anonymous_8_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['_ref3'])
    @Js
    def PyJs__callee3_9_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, '_callee3':PyJs__callee3_9_}, var)
        var.registers(['xL', 'm', 'pH', 'data', 'a', 'imagedata', 'xH', 'inputFile', 'c', 'yH', 'fn', 'by', 'file', 'bx', 'pL', 'yL', 'img'])
        pass
        @Js
        def PyJs_InlineNonPyName_10_(_context3, this, arguments, var=var):
            var = Scope({'_context3':_context3, 'this':this, 'arguments':arguments, '_callee3$':PyJs_InlineNonPyName_10_}, var)
            var.registers(['_context3'])
            while Js(1.0):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('_context3').put('prev', var.get('_context3').get('next')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.put('inputFile', var.get('$')(Js('#input-file')))
                        if (var.get('inputFile').get('files').get('length')<Js(1.0)).neg():
                            var.get('_context3').put('next', Js(3.0))
                            break
                        return var.get('_context3').callprop('abrupt', Js('return'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                        SWITCHED = True
                        var.put('file', var.get('inputFile').get('files').get('0'))
                        var.get('_context3').put('next', Js(6.0))
                        return var.get('loadImage')(var.get('file'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                        SWITCHED = True
                        var.put('imagedata', var.get('_context3').get('sent'))
                        if var.get('confirm')(((Js('The image you selected has width of ')+var.get('imagedata').get('width'))+Js('px. Print it anyway?'))):
                            var.get('_context3').put('next', Js(9.0))
                            break
                        return var.get('_context3').callprop('abrupt', Js('return'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
                        SWITCHED = True
                        var.put('img', var.get('Escpos').get('BinaryImage').callprop('fromImageData', var.get('imagedata'), var.get('Escpos').get('BinaryImage').get('DITHER').get('SIERRA')))
                        var.put('data', var.get('img').callprop('toRaster'))
                        var.put('pL', ((var.get('data').get('length')+Js(10.0))%Js(256.0)))
                        var.put('pH', var.get('Math').callprop('floor', ((var.get('data').get('length')+Js(10.0))/Js(256.0))))
                        var.put('m', Js(48))
                        var.put('fn', Js(112))
                        var.put('a', Js(48))
                        var.put('bx', Js(1))
                        var.put('by', Js(1))
                        var.put('c', Js(49))
                        var.put('xL', (var.get('img').get('width')%Js(256.0)))
                        var.put('xH', var.get('Math').callprop('floor', (var.get('img').get('width')/Js(256.0))))
                        var.put('yL', (var.get('img').get('height')%Js(256.0)))
                        var.put('yH', var.get('Math').callprop('floor', (var.get('img').get('height')/Js(256.0))))
                        var.get('_context3').put('next', Js(25.0))
                        return var.get('printer').callprop('raw', var.get('Uint8Array').create(Js([Js(29), Js(40), Js(76), var.get('pL'), var.get('pH'), var.get('m'), var.get('fn'), var.get('a'), var.get('bx'), var.get('by'), var.get('c'), var.get('xL'), var.get('xH'), var.get('yL'), var.get('yH')]).callprop('concat', var.get('_toConsumableArray')(var.get('data')))))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(25.0)):
                        SWITCHED = True
                        var.get('_context3').put('next', Js(27.0))
                        return var.get('printer').callprop('raw', var.get('Uint8Array').create(Js([Js(29), Js(40), Js(76), Js(2), Js(0), Js(48), Js(50)])))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(27.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('end')):
                        SWITCHED = True
                        return var.get('_context3').callprop('stop')
                    SWITCHED = True
                    break
        PyJs_InlineNonPyName_10_._set_name('_callee3$')
        return var.get('regeneratorRuntime').callprop('wrap', PyJs_InlineNonPyName_10_, var.get('_callee3'), var.get(u"this"))
    PyJs__callee3_9_._set_name('_callee3')
    var.put('_ref3', var.get('_asyncToGenerator')(var.get('regeneratorRuntime').callprop('mark', PyJs__callee3_9_)))
    @Js
    def PyJs_printImage_11_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'printImage':PyJs_printImage_11_}, var)
        var.registers([])
        return var.get('_ref3').callprop('apply', var.get(u"this"), var.get('arguments'))
    PyJs_printImage_11_._set_name('printImage')
    return PyJs_printImage_11_
PyJs_anonymous_8_._set_name('anonymous')
var.put('printImage', PyJs_anonymous_8_())
@Js
def PyJs_anonymous_12_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['_ref4'])
    @Js
    def PyJs__callee4_13_(file, this, arguments, var=var):
        var = Scope({'file':file, 'this':this, 'arguments':arguments, '_callee4':PyJs__callee4_13_}, var)
        var.registers(['file'])
        @Js
        def PyJs_InlineNonPyName_14_(_context4, this, arguments, var=var):
            var = Scope({'_context4':_context4, 'this':this, 'arguments':arguments, '_callee4$':PyJs_InlineNonPyName_14_}, var)
            var.registers(['_context4'])
            while Js(1.0):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('_context4').put('prev', var.get('_context4').get('next')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.get('_context4').put('next', Js(2.0))
                        @Js
                        def PyJs_anonymous_15_(resolve, reject, this, arguments, var=var):
                            var = Scope({'resolve':resolve, 'reject':reject, 'this':this, 'arguments':arguments}, var)
                            var.registers(['resolve', 'context', 'reader', 'reject', 'canvas', 'img'])
                            var.put('canvas', var.get('document').callprop('createElement', Js('canvas')))
                            var.put('context', var.get('canvas').callprop('getContext', Js('2d')))
                            var.put('img', var.get('Image').create())
                            @Js
                            def PyJs_anonymous_16_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers([])
                                var.get('canvas').put('width', var.get('img').get('width'))
                                var.get('canvas').put('height', var.get('img').get('height'))
                                var.get('context').callprop('drawImage', var.get('img'), Js(0.0), Js(0.0), var.get('img').get('width'), var.get('img').get('height'))
                                var.get('resolve')(var.get('context').callprop('getImageData', Js(0.0), Js(0.0), var.get('img').get('width'), var.get('img').get('height')))
                            PyJs_anonymous_16_._set_name('anonymous')
                            var.get('img').callprop('addEventListener', Js('load'), PyJs_anonymous_16_)
                            @Js
                            def PyJs_anonymous_17_(e, this, arguments, var=var):
                                var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                                var.registers(['e'])
                                var.get('reject')(var.get('e'))
                            PyJs_anonymous_17_._set_name('anonymous')
                            var.get('img').callprop('addEventListener', Js('error'), PyJs_anonymous_17_)
                            var.put('reader', var.get('FileReader').create())
                            @Js
                            def PyJs_anonymous_18_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers([])
                                var.get('img').put('src', var.get('reader').get('result'))
                            PyJs_anonymous_18_._set_name('anonymous')
                            var.get('reader').callprop('addEventListener', Js('load'), PyJs_anonymous_18_)
                            @Js
                            def PyJs_anonymous_19_(e, this, arguments, var=var):
                                var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                                var.registers(['e'])
                                var.get('reject')(var.get('e'))
                            PyJs_anonymous_19_._set_name('anonymous')
                            var.get('reader').callprop('addEventListener', Js('error'), PyJs_anonymous_19_)
                            var.get('reader').callprop('readAsDataURL', var.get('file'))
                        PyJs_anonymous_15_._set_name('anonymous')
                        return var.get('Promise').create(PyJs_anonymous_15_)
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        return var.get('_context4').callprop('abrupt', Js('return'), var.get('_context4').get('sent'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('end')):
                        SWITCHED = True
                        return var.get('_context4').callprop('stop')
                    SWITCHED = True
                    break
        PyJs_InlineNonPyName_14_._set_name('_callee4$')
        return var.get('regeneratorRuntime').callprop('wrap', PyJs_InlineNonPyName_14_, var.get('_callee4'), var.get(u"this"))
    PyJs__callee4_13_._set_name('_callee4')
    var.put('_ref4', var.get('_asyncToGenerator')(var.get('regeneratorRuntime').callprop('mark', PyJs__callee4_13_)))
    @Js
    def PyJs_loadImage_20_(_x2, this, arguments, var=var):
        var = Scope({'_x2':_x2, 'this':this, 'arguments':arguments, 'loadImage':PyJs_loadImage_20_}, var)
        var.registers(['_x2'])
        return var.get('_ref4').callprop('apply', var.get(u"this"), var.get('arguments'))
    PyJs_loadImage_20_._set_name('loadImage')
    return PyJs_loadImage_20_
PyJs_anonymous_12_._set_name('anonymous')
var.put('loadImage', PyJs_anonymous_12_())
@Js
def PyJs_anonymous_21_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['_ref5'])
    @Js
    def PyJs__callee5_22_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, '_callee5':PyJs__callee5_22_}, var)
        var.registers([])
        @Js
        def PyJs_InlineNonPyName_23_(_context5, this, arguments, var=var):
            var = Scope({'_context5':_context5, 'this':this, 'arguments':arguments, '_callee5$':PyJs_InlineNonPyName_23_}, var)
            var.registers(['_context5'])
            while Js(1.0):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('_context5').put('prev', var.get('_context5').get('next')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.get('_context5').put('next', Js(2.0))
                        return var.get('printer').callprop('raw', var.get('Uint8Array').create(Js([Js(29), Js(40), Js(69), Js(3), Js(0), Js(1), Js(73), Js(78)])))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.get('_context5').put('next', Js(4.0))
                        return var.get('printer').callprop('raw', var.get('Uint8Array').create(Js([Js(29), Js(40), Js(69), Js(4), Js(0), Js(5), Js(3), Js(2), Js(0)])))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                        SWITCHED = True
                        var.get('_context5').put('next', Js(6.0))
                        return var.get('printer').callprop('raw', var.get('Uint8Array').create(Js([Js(29), Js(40), Js(69), Js(4), Js(0), Js(2), Js(79), Js(85), Js(84)])))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('end')):
                        SWITCHED = True
                        return var.get('_context5').callprop('stop')
                    SWITCHED = True
                    break
        PyJs_InlineNonPyName_23_._set_name('_callee5$')
        return var.get('regeneratorRuntime').callprop('wrap', PyJs_InlineNonPyName_23_, var.get('_callee5'), var.get(u"this"))
    PyJs__callee5_22_._set_name('_callee5')
    var.put('_ref5', var.get('_asyncToGenerator')(var.get('regeneratorRuntime').callprop('mark', PyJs__callee5_22_)))
    @Js
    def PyJs_set58mm_24_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'set58mm':PyJs_set58mm_24_}, var)
        var.registers([])
        return var.get('_ref5').callprop('apply', var.get(u"this"), var.get('arguments'))
    PyJs_set58mm_24_._set_name('set58mm')
    return PyJs_set58mm_24_
PyJs_anonymous_21_._set_name('anonymous')
var.put('set58mm', PyJs_anonymous_21_())
@Js
def PyJs_anonymous_25_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['_ref6'])
    @Js
    def PyJs__callee6_26_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, '_callee6':PyJs__callee6_26_}, var)
        var.registers([])
        @Js
        def PyJs_InlineNonPyName_27_(_context6, this, arguments, var=var):
            var = Scope({'_context6':_context6, 'this':this, 'arguments':arguments, '_callee6$':PyJs_InlineNonPyName_27_}, var)
            var.registers(['_context6'])
            while Js(1.0):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('_context6').put('prev', var.get('_context6').get('next')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.get('_context6').put('next', Js(2.0))
                        return var.get('printer').callprop('raw', var.get('Uint8Array').create(Js([Js(29), Js(40), Js(69), Js(3), Js(0), Js(1), Js(73), Js(78)])))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.get('_context6').put('next', Js(4.0))
                        return var.get('printer').callprop('raw', var.get('Uint8Array').create(Js([Js(29), Js(40), Js(69), Js(4), Js(0), Js(5), Js(3), Js(6), Js(0)])))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                        SWITCHED = True
                        var.get('_context6').put('next', Js(6.0))
                        return var.get('printer').callprop('raw', var.get('Uint8Array').create(Js([Js(29), Js(40), Js(69), Js(4), Js(0), Js(2), Js(79), Js(85), Js(84)])))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('end')):
                        SWITCHED = True
                        return var.get('_context6').callprop('stop')
                    SWITCHED = True
                    break
        PyJs_InlineNonPyName_27_._set_name('_callee6$')
        return var.get('regeneratorRuntime').callprop('wrap', PyJs_InlineNonPyName_27_, var.get('_callee6'), var.get(u"this"))
    PyJs__callee6_26_._set_name('_callee6')
    var.put('_ref6', var.get('_asyncToGenerator')(var.get('regeneratorRuntime').callprop('mark', PyJs__callee6_26_)))
    @Js
    def PyJs_set80mm_28_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'set80mm':PyJs_set80mm_28_}, var)
        var.registers([])
        return var.get('_ref6').callprop('apply', var.get(u"this"), var.get('arguments'))
    PyJs_set80mm_28_._set_name('set80mm')
    return PyJs_set80mm_28_
PyJs_anonymous_25_._set_name('anonymous')
var.put('set80mm', PyJs_anonymous_25_())
@Js
def PyJs_anonymous_29_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['_ref7'])
    @Js
    def PyJs__callee7_30_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, '_callee7':PyJs__callee7_30_}, var)
        var.registers(['devices'])
        pass
        @Js
        def PyJs_InlineNonPyName_31_(_context7, this, arguments, var=var):
            var = Scope({'_context7':_context7, 'this':this, 'arguments':arguments, '_callee7$':PyJs_InlineNonPyName_31_}, var)
            var.registers(['_context7'])
            while Js(1.0):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('_context7').put('prev', var.get('_context7').get('next')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.get('_context7').put('next', Js(2.0))
                        return var.get('navigator').get('usb').callprop('getDevices')
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('devices', var.get('_context7').get('sent'))
                        if (var.get('devices').get('length')<Js(1.0)).neg():
                            var.get('_context7').put('next', Js(6.0))
                            break
                        var.get('showMessage')(Js('No paired device found. Click "pair" to pair a new printer.'))
                        return var.get('_context7').callprop('abrupt', Js('return'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                        SWITCHED = True
                        var.put('printer', var.get('Escpos').get('Usb').create(var.get('devices').get('0')))
                        var.get('_context7').put('next', Js(9.0))
                        return var.get('printer').callprop('setup')
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
                        SWITCHED = True
                        var.get('showMessage')(((((Js('Connected to ')+var.get('devices').get('0').get('productName'))+Js(' ('))+var.get('devices').get('0').get('serialNumber'))+Js(')')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('end')):
                        SWITCHED = True
                        return var.get('_context7').callprop('stop')
                    SWITCHED = True
                    break
        PyJs_InlineNonPyName_31_._set_name('_callee7$')
        return var.get('regeneratorRuntime').callprop('wrap', PyJs_InlineNonPyName_31_, var.get('_callee7'), var.get(u"this"))
    PyJs__callee7_30_._set_name('_callee7')
    var.put('_ref7', var.get('_asyncToGenerator')(var.get('regeneratorRuntime').callprop('mark', PyJs__callee7_30_)))
    @Js
    def PyJs_init_32_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'init':PyJs_init_32_}, var)
        var.registers([])
        return var.get('_ref7').callprop('apply', var.get(u"this"), var.get('arguments'))
    PyJs_init_32_._set_name('init')
    return PyJs_init_32_
PyJs_anonymous_29_._set_name('anonymous')
var.put('init', PyJs_anonymous_29_())
@Js
def PyJs_anonymous_33_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['_ref8'])
    @Js
    def PyJs__callee8_34_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, '_callee8':PyJs__callee8_34_}, var)
        var.registers(['device'])
        pass
        @Js
        def PyJs_InlineNonPyName_35_(_context8, this, arguments, var=var):
            var = Scope({'_context8':_context8, 'this':this, 'arguments':arguments, '_callee8$':PyJs_InlineNonPyName_35_}, var)
            var.registers(['_context8'])
            while Js(1.0):
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('_context8').put('prev', var.get('_context8').get('next')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                        SWITCHED = True
                        var.get('_context8').put('next', Js(2.0))
                        return var.get('navigator').get('usb').callprop('requestDevice', Js({'filters':Js([])}))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                        SWITCHED = True
                        var.put('device', var.get('_context8').get('sent'))
                        var.put('printer', var.get('Escpos').get('Usb').create(var.get('device')))
                        var.get('_context8').put('next', Js(6.0))
                        return var.get('printer').callprop('setup')
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                        SWITCHED = True
                        var.get('showMessage')(((((Js('Connected to ')+var.get('device').get('productName'))+Js(' ('))+var.get('device').get('serialNumber'))+Js(')')))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('end')):
                        SWITCHED = True
                        return var.get('_context8').callprop('stop')
                    SWITCHED = True
                    break
        PyJs_InlineNonPyName_35_._set_name('_callee8$')
        return var.get('regeneratorRuntime').callprop('wrap', PyJs_InlineNonPyName_35_, var.get('_callee8'), var.get(u"this"))
    PyJs__callee8_34_._set_name('_callee8')
    var.put('_ref8', var.get('_asyncToGenerator')(var.get('regeneratorRuntime').callprop('mark', PyJs__callee8_34_)))
    @Js
    def PyJs_pair_36_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'pair':PyJs_pair_36_}, var)
        var.registers([])
        return var.get('_ref8').callprop('apply', var.get(u"this"), var.get('arguments'))
    PyJs_pair_36_._set_name('pair')
    return PyJs_pair_36_
PyJs_anonymous_33_._set_name('anonymous')
var.put('pair', PyJs_anonymous_33_())
var.get('require')(Js('core-js/stable'))
var.get('require')(Js('regenerator-runtime/runtime'))
pass
pass
var.put('$', var.get('document').get('querySelector').callprop('bind', var.get('document')))
var.put('printer', PyJsComma(Js(0.0), Js(None)))
pass
var.get('$')(Js('#button-pair')).callprop('addEventListener', Js('click'), var.get('pair'))
var.get('$')(Js('#button-print-text')).callprop('addEventListener', Js('click'), var.get('printText'))
var.get('$')(Js('#button-cut')).callprop('addEventListener', Js('click'), var.get('cut'))
var.get('$')(Js('#button-print-image')).callprop('addEventListener', Js('click'), var.get('printImage'))
var.get('$')(Js('#button-58mm')).callprop('addEventListener', Js('click'), var.get('set58mm'))
var.get('$')(Js('#button-80mm')).callprop('addEventListener', Js('click'), var.get('set80mm'))
var.get('init')()
pass
