# Online Tutorials to generate GUI 
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout
from PyQt6 import uic
from ProjectClass import ProjectClass

class MainWindow(QMainWindow):
    #TODO: Import data into test projects
    defaultProject = ProjectClass("test project", 0)
    count: int = 0
    timer : QTimer

    def __init__(self):
        super().__init__()
        uic.loadUi('QTDesignerTest.ui',self)
        self.timer = QTimer(self)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.update_display)
        self.pushButton.clicked.connect(self.start_timer)
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButton_2.clicked.connect(self.pushButtonClicked2)
        self.pushButton_2.clicked.connect(self.stop_timer)

    def start_timer(self):
        self.timer.start()
        print("timer started")

    def stop_timer(self):
        self.timer.stop()
        print("timer stopped")
        print(self.count)
        self.defaultProject.time += self.count

    def pushButtonClicked(self):
        self.textBrowser.clear()
        self.textBrowser.setText(self.defaultProject.name)

    def pushButtonClicked2(self):
        self.textBrowser.setText("button 2 pressed")

    def update_display(self):
        print("fire")
        self.count = self.count + 1
        self.lcdNumber.display(self.count)

    def get_final_time(self):
        return self.defaultProject.time
        
def main():
    print("test main program")
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])
    
    # Create default Project 

    # Create a Qt widget, which will be our window.
    window = MainWindow()
    window.show()  # Windows are hidden by default.

    # Start the event loop.
    app.exec()

    # Your application won't reach here until you exit and the event
    # loop has stopped.
    print("test program closing \n")

    #TODO: ExportData
    print(window.get_final_time())

if __name__ == "__main__":
    main()