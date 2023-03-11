if (!window.Escpos) {
    window.Escpos = {};
}

Escpos.Printer = class {
    constructor () {};
    static encodeSJIS (str) {
        const sjisBuffer = Encoding.convert((new TextEncoder()).encode(str), {
            from: 'UTF8',
            to: 'SJIS',
            type: 'arraybuffer'
        });
        return sjisBuffer;
    }
    async raw (data) {
        throw new Error('Not implemented');
    }
    async read (length) {
        throw new Error('Not implemented');
    }
    async text (str) {
        const encoder = new TextEncoder();
        await this.raw(encoder.encode(str));
    }
    async feed (n = 1) {
        // ESC d
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=17
        n = Math.round(n);
        n = Math.max(0, n);
        n = Math.min(255, n);
        await this.raw(new Uint8Array([0x1b, 0x64, n]));
    }
    async cut () {
        // GS V
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=87
        await this.feed(5);
        await this.raw(new Uint8Array([0x1d, 0x56, 0x00]));
    }
    async setUnderline (set, lineWidth = 1) {
        // ESC -
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=24
        // FS -
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=176
        if (![1, 2].includes(lineWidth)) {
            lineWidth = 1;
        }
        let n = lineWidth;
        if (!set) {
            n = 0;
        }
        await this.raw(new Uint8Array([0x1b, 0x2d, n]));
        await this.raw(new Uint8Array([0x1c, 0x2d, n]));
    }
    async setEmphasized (set) {
        // ESC E
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=25
        let n;
        if (set) {
            n = 1;
        } else {
            n = 0;
        }
        await this.raw(new Uint8Array([0x1b, 0x45, n]));
    }
    async setDoubled (set) {
        // ESC G
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=26
        let n;
        if (set) {
            n = 1;
        } else {
            n = 0;
        }
        await this.raw(new Uint8Array([0x1b, 0x47, n]));
    }
    async selectFont (fontName) {
        // ESC M
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=27
        // FS ( A <fn=48>
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=184
        const fontCode = ['A', 'B', 'C'].indexOf(fontName);
        if (fontCode === -1) {
            throw new Error('Invalid font specified');
        }
        await this.raw(new Uint8Array([0x1b, 0x4d, fontCode]));
        await this.raw(new Uint8Array([0x1c, 0x28, 0x41, 0x02, 0x00, 0x30, fontCode]));
    }
    async setUpsideDown (set) {
        // ESC {
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=33
        let n;
        if (set) {
            n = 1;
        } else {
            n = 0;
        }
        await this.raw(new Uint8Array([0x1b, 0x7b, n]));
    }
    async setFontSize (width, height, smooth = true) {
        // GS !
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=34
        // GS b
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=36
        if (!height) {
            height = width;
        }
        if (![1, 2, 3, 4, 5, 6, 7, 8].includes(width)) {
            throw new Error('Invalid width specified');
        }
        if (![1, 2, 3, 4, 5, 6, 7, 8].includes(height)) {
            throw new Error('Invalid height specified');
        }
        const n = 16 * (width - 1) + (height - 1);
        await this.raw(new Uint8Array([0x1d, 0x21, n]));
        let m;
        if (smooth) {
            m = 1;
        } else {
            m = 0;
        }
        await this.raw(new Uint8Array([0x1d, 0x62, m]));
    }
    async setInverted (set) {
        // GS B
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=35
        let n;
        if (set) {
            n = 1;
        } else {
            n = 0;
        }
        await this.raw(new Uint8Array([0x1d, 0x42, n]));
    }
    async selectKanjiCode (code) {
        // FS C
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=180
        const n = ['jis', 'sjis'].indexOf(code);
        if (n === -1) {
            throw new Error('Invalid code specified');
        }
        await this.raw(new Uint8Array([0x1c, 0x43, n]));
    }
    async enableKanjiMode () {
        // FS &
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=175
        await this.raw(new Uint8Array([0x1c, 0x26]));
    }
    async disableKanjiMode () {
        // FS .
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=177
        await this.raw(new Uint8Array([0x1c, 0x2e]));
    }
    async selectInternationalCharacter (n) {
        // ESC R
        // https://www.epson-biz.com/modules/ref_escpos_ja/index.php?content_id=29
        const validCodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 82];
        if (!validCodes.includes(n)) {
            throw new Error('Invalid code specified');
        }
        await this.raw(new Uint8Array([0x1b, 0x52, n]));
    }
}

Escpos.Usb = class extends Escpos.Printer {
    constructor (device) {
        super();
        this.device = device;
    }
    async setup () {
        await this.device.open();
        await this.device.selectConfiguration(this.device.configurations[0].configurationValue);
        await this.device.claimInterface(this.device.configuration.interfaces[0].interfaceNumber);
        await this.device.selectAlternateInterface(this.device.configuration.interfaces[0].interfaceNumber, {});
    }
    async raw (data) {
        await this.device.transferOut(1, data);
    }
    async read (length) {
        return new Uint8Array((await this.device.transferIn(2, length)).data.buffer);
    }
}