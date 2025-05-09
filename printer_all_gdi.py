'''
The Windows GDI (Graphics Device Interface) provides a wide range of methods to draw text, 
lines, shapes, and images to screens or printers. While Python’s pywin32 doesn't expose all 
native GDI functions, many are accessible through the win32ui, win32print, and win32gui modules.
'''

import win32print
import win32ui
import win32con
import win32api
from PIL import Image, ImageWin

def print_gdi_demo():
    # Load image
    image_path = "uncle_logo.png"
    image = Image.open(image_path).convert("RGB")

    # Get default printer name
    printer_name = win32print.GetDefaultPrinter()

    # Create printer DC (Device Context)
    dc = win32ui.CreateDC()
    dc.CreatePrinterDC(printer_name)

    # Start document
    dc.StartDoc("GDI Demo Print")
    dc.StartPage()

    # Set up font
    font = win32ui.CreateFont({
        "name": "Consolas",
        "height": 36,
        "weight": 700,
    })
    dc.SelectObject(font)

    # Draw text
    dc.TextOut(100, 100, "Hello from GDI and Python!")

    # Draw lines and shapes
    pen = win32ui.CreatePen(win32con.PS_SOLID, 5, win32api.RGB(255, 0, 0))  # red line
    dc.SelectObject(pen)
    dc.MoveTo((100, 200))
    dc.LineTo((500, 200))

    # Draw rectangle
    dc.Rectangle((100, 250, 300, 350))

    # Draw ellipse
    dc.Ellipse((350, 250, 550, 350))

    # Draw image (logo)
    printer_width = dc.GetDeviceCaps(8)   # HORZRES
    printer_height = dc.GetDeviceCaps(10) # VERTRES

    max_width = printer_width // 3
    max_height = printer_height // 3
    image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

    dib = ImageWin.Dib(image)
    x, y = 100, 400
    dib.draw(dc.GetHandleOutput(), (x, y, x + image.width, y + image.height))

    # End document
    dc.EndPage()
    dc.EndDoc()
    dc.DeleteDC()

if __name__ == "__main__":
    print_gdi_demo()
