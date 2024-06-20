import qrcode

# Define the URL you want to encode
url = "https://www.harper-adams.ac.uk/community/988/community-fridge-pilot-project/"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the URL data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("website_qr_code.png")

print("QR code generated and saved as website_qr_code.png")
