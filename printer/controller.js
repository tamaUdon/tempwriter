import "core-js/stable";
import "regenerator-runtime/runtime";

const $ = document.querySelector.bind(document);

let printer;

async function printText (txt) {
    await printer.selectKanjiCode('sjis');
    await printer.enableKanjiMode();
    await printer.selectInternationalCharacter(0x08); // JP
    const str = txt; //$('textarea').value + '\n';
    await printer.raw(new Uint8Array(Escpos.Printer.encodeSJIS(str)));
    await printer.disableKanjiMode();
}

async function cut () {
    await printer.cut();
}

async function printImage () {

    const inputFile = $('#input-file');

    if (inputFile.files.length < 1) {
        return;
    }

    const file = inputFile.files[0];
    const imagedata = await loadImage(file);

    if (!confirm(`The image you selected has width of ${imagedata.width}px. Print it anyway?`)) {
        return;
    }

    const img = Escpos.BinaryImage.fromImageData(imagedata, Escpos.BinaryImage.DITHER.SIERRA);

    const data = img.toRaster();
    const pL = (data.length + 10) % 256;
    const pH = Math.floor((data.length + 10) / 256);
    const m = 0x30;
    const fn = 0x70;
    const a = 0x30;
    const bx = 0x01;
    const by = 0x01;
    const c = 0x31;

    const xL = img.width % 256;
    const xH = Math.floor(img.width / 256);

    const yL = img.height % 256;
    const yH = Math.floor(img.height / 256);

    await printer.raw(new Uint8Array([
        0x1d, 0x28, 0x4c, pL, pH, m, fn, a, bx, by, c, xL, xH, yL, yH, ...data
    ]));

    await printer.raw(new Uint8Array([
        0x1d, 0x28, 0x4c, 0x02, 0x00, 0x30, 0x32
    ]));

}

async function loadImage (file) {
    return await new Promise((resolve, reject) => {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        const img = new Image();
        img.addEventListener('load', () => {
            canvas.width = img.width;
            canvas.height = img.height;
            context.drawImage(img, 0, 0, img.width, img.height);
            resolve(context.getImageData(0, 0, img.width, img.height));
        });
        img.addEventListener('error', (e) => {
            reject(e);
        });
        const reader = new FileReader();
        reader.addEventListener('load', () => {
            img.src = reader.result;
        });
        reader.addEventListener('error', (e) => {
            reject(e);
        });
        reader.readAsDataURL(file);
    });
}

async function set58mm () {
    // GS ( E fn=1
    await printer.raw(new Uint8Array([0x1d, 0x28, 0x45, 0x03, 0x00, 0x01, 0x49, 0x4e]));
    // use 50mm paper
    await printer.raw(new Uint8Array([0x1d, 0x28, 0x45, 0x04, 0x00, 0x05, 0x03, 0x02, 0x00]));
    // GS ( E fn=2
    await printer.raw(new Uint8Array([0x1d, 0x28, 0x45, 0x04, 0x00, 0x02, 0x4f, 0x55, 0x54]));
}

async function set80mm () {
    // GS ( E fn=1
    await printer.raw(new Uint8Array([0x1d, 0x28, 0x45, 0x03, 0x00, 0x01, 0x49, 0x4e]));
    // use 80mm paper
    await printer.raw(new Uint8Array([0x1d, 0x28, 0x45, 0x04, 0x00, 0x05, 0x03, 0x06, 0x00]));
    // GS ( E fn=2
    await printer.raw(new Uint8Array([0x1d, 0x28, 0x45, 0x04, 0x00, 0x02, 0x4f, 0x55, 0x54]));
}

function showMessage (m) {
    $('#message').textContent = m;
}

async function init () {
    const devices = await navigator.usb.getDevices();
    if (devices.length < 1) {
        showMessage('No paired device found. Click "pair" to pair a new printer.');
        return;
    }
    printer = new Escpos.Usb(devices[0]);
    await printer.setup();
    showMessage(`Connected to ${devices[0].productName} (${devices[0].serialNumber})`);
}

async function pair () {
    const device = await navigator.usb.requestDevice({filters: []});
    printer = new Escpos.Usb(device);
    await printer.setup();
    showMessage(`Connected to ${device.productName} (${device.serialNumber})`);
}


$('#button-pair').addEventListener('click', pair);
$('#button-print-text').addEventListener('click', printText);
$('#button-cut').addEventListener('click', cut);
$('#button-print-image').addEventListener('click', printImage);
$('#button-58mm').addEventListener('click', set58mm);
$('#button-80mm').addEventListener('click', set80mm);

init();