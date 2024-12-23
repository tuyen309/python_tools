import qrcode

def generate_qr(text, filename):
    img = qrcode.make(text)
    img.save(f"{filename}.png")  # Lưu dưới định dạng PNG

generate_qr('https://openweathermap.org/api/one-call-3', 'my_qr_code')
