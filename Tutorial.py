# Online Tutorials to generate GUI 

from PyQt6.QtWidgets import QApplication, QWidget

# You need one (and only one) QApplication instance per application.
app = QApplication([])

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # Windows are hidden by default.

# Start the event loop.
app.exec()

print("test")
# Your application won't reach here until you exit and the event
# loop has stopped.