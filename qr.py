import os
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_M
from PIL import Image

OUTPUT_DIR = Path("qr_output")
QR_SIZE_PX = 900
BORDER = 4
FOREGROUND = "black"
BACKGROUND = "white"

def make_qr(data: str, out_path: Path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=10,
        border=BORDER,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=FOREGROUND, back_color=BACKGROUND).convert("RGB")
    img = img.resize((QR_SIZE_PX, QR_SIZE_PX), Image.LANCZOS)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "PNG")

# ...existing code...
if __name__ == "__main__":
    base_url = f"file:///{Path(__file__).parent / 'page.html'}"  # Use local landing page as base URL

    for i in range(1, 25):  # 24 QR codes
        url = f"{base_url}?qr={i}"
        out_file = OUTPUT_DIR / f"qr_{i:02}.png"
        make_qr(url, out_file)

    print("✅ 24 QR codes generated in:", OUTPUT_DIR.resolve())
# ...existing code...
