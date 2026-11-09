"""Generate poster QR codes locally.
No installation needed. Light: purple/white; dark: white/purple.
"""
import argparse
from pathlib import Path
import struct
import zlib
from vendor.qrcodegen import QrCode, DataTooLongError


def png_chunk(kind, data):
    return (struct.pack('>I', len(data)) + kind + data
            + struct.pack('>I', zlib.crc32(kind + data) & 0xFFFFFFFF))


def save_png(qr, output, foreground, background):
    """Write an RGB PNG with integer scaling and a four-module quiet zone."""
    scale, border = 12, 4
    size = (qr.get_size() + border * 2) * scale
    pixels = bytearray()
    for y in range(-border, qr.get_size() + border):
        row = b'\x00' + b''.join(
            (foreground if qr.get_module(x, y) else background) * scale
            for x in range(-border, qr.get_size() + border))
        pixels.extend(row * scale)
    output.write_bytes(
        b'\x89PNG\r\n\x1a\n'
        + png_chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0))
        + png_chunk(b'IDAT', zlib.compress(pixels, 9))
        + png_chunk(b'IEND', b''))

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('url')
parser.add_argument('output', nargs='?', default='qr.png',
                    help='PNG filename in assets/qrcodes/ (default: qr.png)')
parser.add_argument('--mode', choices=['light', 'dark'], default='light')
args = parser.parse_args()
if args.output in ('.', '..') or '/' in args.output or '\\' in args.output:
    parser.error('Output must be a filename; QR codes are always saved in assets/qrcodes/')
if Path(args.output).suffix.lower() != '.png':
    parser.error('Output filename must end in .png')
output = Path(__file__).resolve().parents[1] / 'assets' / 'qrcodes' / args.output
output.parent.mkdir(parents=True, exist_ok=True)
foreground, background = ('#662E7D', '#FFFFFF') if args.mode == 'light' else ('#FFFFFF', '#662E7D')
try:
    qr = QrCode.encode_text(args.url, QrCode.Ecc.MEDIUM)
except DataTooLongError:
    parser.error('URL is too long for a QR code; use a shorter destination')
save_png(qr, output, bytes.fromhex(foreground[1:]), bytes.fromhex(background[1:]))
print(f"Saved QR code: {output}")
