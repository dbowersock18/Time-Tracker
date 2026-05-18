# Online Tutorials to generate GUI 
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window
        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        #Layout
        layout = QGridLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        #Widget Creation
        button = QPushButton("Press Me!")

        # Widget Customization
        # button.setStyleSheet("""
        #                     width: 100px;
        #                     height: 100px;
        #                     border: 4px solid blue;
        #                     border-radius: 50%;""") 
        
        # Test 2
        button.setStyleSheet("""
                            background-color: #e8f4ff;
                            border: 2px solid #64b5f6;
                            border-radius: 20px;
                            padding: 10px 24px;
                            font-size: 16px;
                            color: #1565c0;
                            """)

        #Add button to Layout
        layout.addWidget(button,2,2,alignment=Qt.AlignmentFlag.AlignCenter)
        
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("it clicked!")

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