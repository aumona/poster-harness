"""Generate poster QR codes locally.
Install with: python3 -m pip install -r requirements.txt. Light: purple/white; dark: white/purple.
"""
import argparse
from pathlib import Path
import qrcode
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
qr = qrcode.QRCode(box_size=12, border=4)
qr.add_data(args.url)
qr.make(fit=True)
qr.make_image(fill_color=foreground, back_color=background).save(output)
print(f"Saved QR code: {output}")
