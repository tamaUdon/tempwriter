if (!window.Escpos) {
    window.Escpos = {};
}

Escpos.BinaryImage = class {
    constructor(width, height) {
        this.width = width;
        this.height = height;
        this.pixels = [];
        this.pixels.length = width * height;
        this.pixels.fill(0);
    }
    static DITHER = {
        THRESHOLDING: Symbol(),
        RANDOM: Symbol(),
        FLOYD_STEINBERG: Symbol(),
        JARVIS_JUDICE_AND_NINKE: Symbol(),
        FAN: Symbol(),
        SHIAU_FAN: Symbol(),
        SHIAU_FAN2: Symbol(),
        STUCKI: Symbol(),
        BURKES: Symbol(),
        SIERRA: Symbol(),
        TWO_ROW_SIERRA: Symbol(),
        SIERRA_LITE: Symbol(),
        ATKINSON: Symbol()
    };
    static fromImageData(imagedata, dither = Escpos.BinaryImage.DITHER.FLOYD_STEINBERG) {

        const img = new Escpos.BinaryImage(imagedata.width, imagedata.height);

        for (let i = 0; i < img.width * img.height * 4; i++) {
            let opacity = imagedata.data[i * 4 + 3] / 255;
            let v = 0;
            v += imagedata.data[i * 4 + 0];
            v += imagedata.data[i * 4 + 1];
            v += imagedata.data[i * 4 + 2];
            v = opacity * (v / 3) + (1 - opacity) * 255;
            img.pixels[i] = Math.floor(v);
        }

        if (dither === Escpos.BinaryImage.DITHER.THRESHOLDING) {
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] < 128 ? 1 : 0;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.RANDOM) {
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] < Math.floor(Math.random() * 255) ? 1 : 0;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.FLOYD_STEINBERG) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 16);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 7;
                img.pixels[i + img.width - 1] += quantErr * 3;
                img.pixels[i + img.width] += quantErr * 5;
                img.pixels[i + img.width + 1] += quantErr * 1;
            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.JARVIS_JUDICE_AND_NINKE) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 48);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 7;
                img.pixels[i + 2] += quantErr * 5;
                img.pixels[i + img.width - 2] += quantErr * 3;
                img.pixels[i + img.width - 1] += quantErr * 5;
                img.pixels[i + img.width + 0] += quantErr * 7;
                img.pixels[i + img.width + 1] += quantErr * 5;
                img.pixels[i + img.width + 2] += quantErr * 3;
                img.pixels[i + img.width * 2 - 2] += quantErr * 1;
                img.pixels[i + img.width * 2 - 1] += quantErr * 3;
                img.pixels[i + img.width * 2 + 0] += quantErr * 5;
                img.pixels[i + img.width * 2 + 1] += quantErr * 3;
                img.pixels[i + img.width * 2 + 2] += quantErr * 1;
            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.FAN) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 16);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 7;
                img.pixels[i + img.width - 2] += quantErr * 1;
                img.pixels[i + img.width - 1] += quantErr * 3;
                img.pixels[i + img.width + 0] += quantErr * 5;

            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.SHIAU_FAN) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 8);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 4;
                img.pixels[i + img.width - 2] += quantErr * 1;
                img.pixels[i + img.width - 1] += quantErr * 1;
                img.pixels[i + img.width + 0] += quantErr * 2;

            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.SHIAU_FAN2) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 16);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 8;
                img.pixels[i + img.width - 3] += quantErr * 1;
                img.pixels[i + img.width - 2] += quantErr * 1;
                img.pixels[i + img.width - 1] += quantErr * 2;
                img.pixels[i + img.width + 0] += quantErr * 4;

            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.STUCKI) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 42);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 8;
                img.pixels[i + 2] += quantErr * 4;
                img.pixels[i + img.width - 2] += quantErr * 2;
                img.pixels[i + img.width - 1] += quantErr * 4;
                img.pixels[i + img.width + 0] += quantErr * 8;
                img.pixels[i + img.width + 1] += quantErr * 4;
                img.pixels[i + img.width + 2] += quantErr * 2;
                img.pixels[i + img.width * 2 - 2] += quantErr * 1;
                img.pixels[i + img.width * 2 - 1] += quantErr * 2;
                img.pixels[i + img.width * 2 + 0] += quantErr * 4;
                img.pixels[i + img.width * 2 + 1] += quantErr * 2;
                img.pixels[i + img.width * 2 + 2] += quantErr * 1;
            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.BURKES) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 16);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 4;
                img.pixels[i + 2] += quantErr * 2;
                img.pixels[i + img.width - 2] += quantErr * 1;
                img.pixels[i + img.width - 1] += quantErr * 2;
                img.pixels[i + img.width + 0] += quantErr * 4;
                img.pixels[i + img.width + 1] += quantErr * 2;
                img.pixels[i + img.width + 2] += quantErr * 1;
            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.SIERRA) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 32);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 5;
                img.pixels[i + 2] += quantErr * 3;
                img.pixels[i + img.width - 2] += quantErr * 2;
                img.pixels[i + img.width - 1] += quantErr * 4;
                img.pixels[i + img.width + 0] += quantErr * 5;
                img.pixels[i + img.width + 1] += quantErr * 4;
                img.pixels[i + img.width + 2] += quantErr * 2;
                img.pixels[i + img.width * 2 - 1] += quantErr * 2;
                img.pixels[i + img.width * 2 + 0] += quantErr * 3;
                img.pixels[i + img.width * 2 + 1] += quantErr * 1;
            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.TWO_ROW_SIERRA) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 16);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 4;
                img.pixels[i + 2] += quantErr * 3;
                img.pixels[i + img.width - 2] += quantErr * 1;
                img.pixels[i + img.width - 1] += quantErr * 2;
                img.pixels[i + img.width + 0] += quantErr * 3;
                img.pixels[i + img.width + 1] += quantErr * 2;
                img.pixels[i + img.width + 2] += quantErr * 1;
            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.SIERRA_LITE) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 4);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 2;
                img.pixels[i + img.width - 1] += quantErr * 1;
                img.pixels[i + img.width + 0] += quantErr * 1;
            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        if (dither === Escpos.BinaryImage.DITHER.ATKINSON) {
            for (let i = 0; i < img.width * img.height; i++) {
                const oldPixel = img.pixels[i];
                const newPixel = oldPixel < 128 ? 0 : 255;
                const quantErr = Math.round((oldPixel - newPixel) / 8);
                img.pixels[i] = newPixel;
                img.pixels[i + 1] += quantErr * 1;
                img.pixels[i + 2] += quantErr * 1;
                img.pixels[i + img.width - 1] += quantErr * 1;
                img.pixels[i + img.width + 0] += quantErr * 1;
                img.pixels[i + img.width + 1] += quantErr * 1;
                img.pixels[i + img.width * 2] += quantErr * 1;
            }
            for (let i = 0; i < img.width * img.height; i++) {
                img.pixels[i] = img.pixels[i] === 255 ? 0 : 1;
            }
        }

        return img;

    }
    toRaster() {
        const data = [];
        const n = Math.ceil(this.width / 8);
        for (let y = 0; y < this.height; y++) {
            for (let x = 0; x < n; x++) {
                data[y * n + x] = 0;
                for (let b = 0; b < 8; b++) {
                    const i = x * 8 + b;
                    if (this.width <= i) {
                        break;
                    }
                    if (this.pixels[y * this.width + i] === 1) {
                        data[y * n + x] += (0x80 >> (b & 0x7));
                    }
                }
            }
        }
        return new Uint8ClampedArray(data);
    }
    toImageData() {
        const imagedata = new ImageData(this.width, this.height);
        for (let y = 0; y < this.height; y++) {
            for (let x = 0; x < this.width; x++) {
                const v = this.pixels[y * this.width + x] === 1 ? 0 : 255;
                imagedata.data[(y * this.width + x) * 4 + 0] = v;
                imagedata.data[(y * this.width + x) * 4 + 1] = v;
                imagedata.data[(y * this.width + x) * 4 + 2] = v;
                imagedata.data[(y * this.width + x) * 4 + 3] = 255;
            }
        }
        return imagedata;
    }
}