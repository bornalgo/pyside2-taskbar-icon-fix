import ctypes
from PySide2 import QtWidgets
import sys
import os

# Constants for working with window icons
GCL_HICON = -14
WM_SETICON = 0x80
ICON_BIG = 1
ICON_SMALL = 0

# Load user32 DLL
user32 = ctypes.windll.user32

# Load the icon
icon_path = os.path.join(os.path.dirname(__file__), "../res/bal.ico")
hicon = user32.LoadImageW(0, icon_path, 1, 0, 0, 0x00000010)

# Check if the icon is loaded correctly
if not hicon:
    print("Failed to load icon")
    sys.exit(1)

# Create the PySide2 application
app = QtWidgets.QApplication(sys.argv)

# Create the main window
main_window = QtWidgets.QMainWindow()
main_window.setWindowTitle("Taskbar Icon Resetter (KB5051987 Fix)")

# Retrieve the window handle (HWND)
hwnd = main_window.winId()

# Set the icons for the window (both large and small)
user32.SendMessageW(hwnd, WM_SETICON, ICON_BIG, hicon)
user32.SendMessageW(hwnd, WM_SETICON, ICON_SMALL, hicon)

# Alternatively, set the icon at the class level (this can be helpful for consistency)
user32.SetClassLongPtrW(hwnd, GCL_HICON, hicon)

# Set the Application User Model ID (AppUserModelID) to ensure the taskbar icon is correctly displayed in Windows.
# Without this, Windows may group the application under a generic icon or fail to show the correct icon in the taskbar.
app_id = u"com.bornalgo.app"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

# Show the window
main_window.show()

# Start the application event loop
sys.exit(app.exec_())
