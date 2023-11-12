import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton


class MyInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.values = []
        self.init_ui()

    def init_ui(self):
        questions = ["Engine won't start: ", "Poor fuel economy: ", "Overheating: ", "Excessive exhaust smoke: ",
                     "Unusual noise: ", "Car vibrates: ", "Poor braking performance: "]
        # Create layout
        layout = QVBoxLayout()
        self.radios=[]
        # Add 8 lines of text with radio button
        for i in range(7):
            line_label = QLabel(questions[i])
            self.radio_yes = QRadioButton("Yes", self)
            self.radio_no = QRadioButton("No", self)
            self.radios.append([self.radio_yes,self.radio_no])
            layout.addWidget(line_label)
            layout.addWidget(self.radios[i][0])
            layout.addWidget(self.radios[i][1])

        # Add a submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_clicked)
        layout.addWidget(submit_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Symptom Checker")
        self.setGeometry(100, 100, 400, 300)

        # Show the window
        self.show()

    def submit_clicked(self):
        for i in range(7):
            print(self.radios[i].isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = MyInterface()
    sys.exit(app.exec_())

print("Values:", interface.values)  # Access the values list outside the class
