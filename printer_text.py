# pip install pywin32, pillow

import win32print
import win32ui

printer_name = win32print.GetDefaultPrinter()  # You can specify a printer name here
hprinter = win32print.OpenPrinter(printer_name)
printer_info = win32print.GetPrinter(hprinter, 2)
pdc = win32ui.CreateDC()
pdc.CreatePrinterDC(printer_name)

pdc.StartDoc("Test Print")
pdc.StartPage()

# Choose font (optional)
font = win32ui.CreateFont({
    "name": "Tahoma",
    "height": 50,
    "weight": 700,
})
pdc.SelectObject(font)

# Draw the text at position (x=100, y=100)
pdc.TextOut(0, 0, "สวัสจ้าลุงวิศวกร")

pdc.EndPage()
pdc.EndDoc()
pdc.DeleteDC()
