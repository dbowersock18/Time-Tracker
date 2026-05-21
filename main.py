# Online Tutorials to generate GUI 
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout
from PyQt6 import uic
import json
from ProjectClass import ProjectClass

def get_json_project_data() -> dict:
    with open('data.json', 'r') as f:
        data_dict = json.load(f)
    return data_dict

def set_json_project_data(project : ProjectClass):
    data_dict = {
        "project_name" : project.name,
        "time" : project.time
    }
    with open('data.json', 'w') as f:
        json.dump(data_dict, f, indent=4)


class MainWindow(QMainWindow):
    #TODO: Import data into test projects
    data_dict = get_json_project_data()
    defaultProject = ProjectClass(data_dict["project_name"],data_dict["time"])
    count: int = 0
    timer : QTimer

    def __init__(self):
        super().__init__()
        uic.loadUi('QTDesignerTest.ui',self) #loads custom UI
        MainWindow.setWindowTitle(self,"Project Tracker!")
        # set up timer #
        self.timer = QTimer(self)
        self.timer.setInterval(1000) #fires every second
        self.timer.timeout.connect(self.update_display)
        # set up displays #
        self.lcdNumber.display(self.defaultProject.time)
        # set up buttons #
        self.pushButton.setCheckable(True)
        self.pushButton.toggled.connect(self.pushButtonToggled)

    def start_timer(self):
        self.count = 0
        self.timer.start()
        print("timer started")

    def stop_timer(self):
        self.timer.stop()
        print("timer stopped")
        self.defaultProject.time += self.count

    def pushButtonToggled(self):
        # Toggle function not working quite like I'd like
        self.textBrowser.clear()
        self.textBrowser.setText(self.defaultProject.name)
        isChecked = self.pushButton.isChecked()
        if (isChecked): self.start_timer()
        if not (isChecked): self.stop_timer()

    def update_display(self):
        print("fire")
        self.count += 1
        self.lcdNumber.display(self.defaultProject.time + self.count)

    def get_final_time(self):
        return self.defaultProject.time
    
    def upload_final_data(self):
        set_json_project_data(self.defaultProject)
        
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

    window.upload_final_data()

if __name__ == "__main__":
    main()