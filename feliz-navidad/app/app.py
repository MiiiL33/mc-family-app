from flask import Flask, render_template
import socket
import qrcode

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def get_local_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def print_qr(url: str) -> None:
    qr = qrcode.QRCode(border=1)
    qr.add_data(url)
    qr.make(fit=True)
    qr.print_ascii(invert=True)

if __name__ == "__main__":
    port = 8080
    ip = get_local_ip()
    url = f"http://{ip}:{port}"

    print("\n🎄 Feliz Navidad server is live 🎄")
    print(f"➡️  Open or share: {url}\n")
    print_qr(url)

    app.run(host="0.0.0.0", port=port)
