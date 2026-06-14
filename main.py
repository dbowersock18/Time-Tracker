# Online Tutorials to generate GUI 
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout
from PyQt6 import uic
import json
from ProjectClass import Project
from PyQt6.QtGui import QIcon

def get_json_project_data() -> dict:
    with open('data.json', 'r') as f:
        data_dict = json.load(f)
    return data_dict

def set_json_project_data(data_dict : dict):
    data_dict_write = {}
    for key, project in data_dict.items():
        data_dict_write[key] = {
            "projectName" : project.name,
            "time" : project.time
        }
    
    with open('data.json', 'w') as f:
        json.dump(data_dict_write, f, indent=4)

class MainWindow(QMainWindow):
    data_dict_json = get_json_project_data()
    # creates a dictionary of Projects (Class) to keep track of 
    data_dict = {}
    for key, value in data_dict_json.items():
        project = Project(value["projectName"], value["time"])
        data_dict[key] = project
    timer : QTimer
    current_project = data_dict[next(iter(data_dict))]

    def __init__(self):
        default_name = self.current_project.name
        default_time = self.current_project.time
        super().__init__()
        uic.loadUi('QTDesignerTest.ui',self) #loads custom UI
        MainWindow.setWindowTitle(self,"Project Tracker!")
        # Set up smaller window
        self.second_window = self.SmallerWindow(self)
        # set up timer #
        self.timer = QTimer(self)
        self.timer.setInterval(1000) #fires every second
        self.timer.timeout.connect(self.update_display)
        # set up displays #
        self.lcdNumber.display(default_time)
        self.comboBox.setCurrentText(default_name)
        # set up buttons #
        self.pushButton.setCheckable(True)
        self.pushButton.toggled.connect(self.pushButtonToggled)
        # Setup ComboBox
        for keys in self.data_dict:
            self.comboBox.addItem(self.data_dict[keys].name)
        self.comboBox.textActivated.connect(self.on_selection_change)

    def resizeEvent(self, event):
        new_width = event.size().width()
        if new_width < 200:
            self.second_window.resize(100,50)
            self.second_window.show()
            self.hide() 
        
    def start_timer(self):
        self.timer.start()
        print("timer started")

    def stop_timer(self):
        self.timer.stop()
        print("timer stopped")

    def pushButtonToggled(self):
        # self.textBrowser.clear()
        isChecked = self.pushButton.isChecked()
        if (isChecked): self.start_timer()
        if not (isChecked): self.stop_timer()

    def on_selection_change(self, text): 
        self.current_project = self.data_dict[text]
        self.lcdNumber.display(self.current_project.time)

    def update_display(self):
        print("fire")
        self.current_project.time += 1
        self.lcdNumber.display(self.current_project.time)
    
    def project_close(self):
        set_json_project_data(self.data_dict)

    class SmallerWindow(QMainWindow):
    # Pass along the parent, the larger window, to never lose a reference to it!
        def __init__(self, parent):
            super().__init__()
            uic.loadUi('smaller_window.ui', self)
            self.parent = parent

        def resizeEvent(self, event):
            new_width = event.size().width()
            if new_width > 150:
                self.hide()
                self.parent.show()
        
def main():
    print("test main program")
    # You need one (and only one) QApplication instance per application.
    app = QApplication([])

    # Create a Qt widget, which will be our window.
    window = MainWindow()
    window.show()  # Windows are hidden by default.

    # Start the event loop.
    app.exec()

    # Your application won't reach here until you exit and the event
    # loop has stopped.
    print("test program closing \n")

    window.project_close()

if __name__ == "__main__":
    main()