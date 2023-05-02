import usb.core
import usb.util

def init_escpos():
    from escpos.printer import Usb
    p = Usb(idVendor=0x04b8, idProduct=0x0202)

    text = "Lorem ipsum dolor （中略） id est laborum."

    p.text(text)
    p.cut()


def init():
    # pyusbのチュートリアルから
    # https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst
    # find our device
    dev = usb.core.find(idVendor=0x04b8, idProduct=0x0202)

    # was it found?
    if dev is None:
        raise ValueError('Device not found')

    # set the active configuration. With no arguments, the first
    # configuration will be the active one
    dev.set_configuration()

    # get an endpoint instance
    cfg = dev.get_active_configuration()
    intf = cfg[(0,0)]

    ep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match = \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT)

    assert ep is not None

    # write the data
    # 1. testする
    ep.write('test')

    # 2. printerをpythonで書き直す
    # printer = new Escpos.Usb(devices[0]);
    # await printer.setup();
    # showMessage(`Connected to ${devices[0].productName} (${devices[0].serialNumber})`);

    # 3. jsのpair()を書き直す

### --js-- ### 
# async function init () {
#     const devices = await navigator.usb.getDevices();
#     if (devices.length < 1) {
#         showMessage('No paired device found. Click "pair" to pair a new printer.');
#         return;
#     }
#     printer = new Escpos.Usb(devices[0]);
#     await printer.setup();
#     showMessage(`Connected to ${devices[0].productName} (${devices[0].serialNumber})`);
# }

# async function pair () {
#     const device = await navigator.usb.requestDevice({filters: []});
#     printer = new Escpos.Usb(device);
#     await printer.setup();
#     showMessage(`Connected to ${device.productName} (${device.serialNumber})`);
# }

# init()
# pair()

init_escpos()