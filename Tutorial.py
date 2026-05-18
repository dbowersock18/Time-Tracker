# Online Tutorials to generate GUI 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('QTDesignerTest.ui',self)
        self.pushButton.clicked.connect(self.pushButtonClicked)

    def pushButtonClicked(self):
        print("Button clicked!")
        self.textBrowser.clear()
        self.textBrowser.setText("test")
        
def main():
    print("test main program")
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    # Create a Qt widget, which will be our window.
    window = MainWindow()
    window.show()  # Windows are hidden by default.

    # Start the event loop.
    app.exec()

    print("test program closing")
    # Your application won't reach here until you exit and the event
    # loop has stopped.

if __name__ == "__main__":
    main()