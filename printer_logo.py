import win32print
import win32ui
from PIL import Image, ImageWin, ImageOps

# Path to your PNG image
image_path = "uncle_logo.png"

# Load image with PIL
image = Image.open(image_path)

# Get default printer
printer_name = win32print.GetDefaultPrinter()
hprinter = win32print.OpenPrinter(printer_name)
printer_info = win32print.GetPrinter(hprinter, 2)

# Create printer device context
hDC = win32ui.CreateDC()
hDC.CreatePrinterDC(printer_name)
hDC.StartDoc("PNG Print Job")
hDC.StartPage()

# Convert image to RGB if it’s not
if image.mode != 'RGB':
    image = image.convert("RGB")

# Define scaling and position
printer_width = hDC.GetDeviceCaps(8)   # HORZRES
printer_height = hDC.GetDeviceCaps(10) # VERTRES

# Resize the image to fit within half the page
max_width = printer_width // 2
max_height = printer_height // 2
print(max_width,max_height)
image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

# Convert to a bitmap suitable for GDI
dib = ImageWin.Dib(image)
x = 230 # center of 80 mm. paper
y = 0
dib.draw(hDC.GetHandleOutput(), (x, y, x + image.width, y + image.height))

hDC.EndPage()
hDC.EndDoc()
hDC.DeleteDC()
