# project: qr code
# created: 12/10/2023

import qrcode

# creates a function that calls the qrcode class
def generate_qr(text):

  #outlines qr code format
  qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
  )

  # adds data to qr code and saves it as a png file
  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color = "black", back_color = "white")
  img.save("qrimage.png")

# asks for input of url and calls the function
url = input("Enter your url: ").strip()
generate_qr(url)
