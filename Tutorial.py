# Online Tutorials to generate GUI 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def appRun(self):
        print("test App Run")
        
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