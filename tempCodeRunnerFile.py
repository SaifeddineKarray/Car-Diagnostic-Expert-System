import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton , QCheckBox,QHBoxLayout
from PyQt5.QtGui import QPixmap
from expertSystem import CarDiagnostic

class MyInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.values = []
        self.result_label = QLabel("Result: (No result yet)")
        self.image_label = QLabel()
        self.init_ui()

    def init_ui(self):
        questions = ["Engine won't start: ", "Poor fuel economy: ", "Overheating: ", "Excessive exhaust smoke: ",
                     "Unusual noise: ", "Car vibrates: ", "Poor braking performance: "]
        # Create layout
        
        layout = QVBoxLayout()
        # Add the image label
        self.load_image("car-mechanics-repairing-car-3323969-2809554.png")  # Set the path to your image
        layout.addWidget(self.image_label)
        self.form=[]
        # Add 7 lines of text with checkboxes
        two_column_layout = QHBoxLayout()
        column1 = QVBoxLayout()
        for i in range(4):
            line_label = QLabel(questions[i])
            self.form.append(QCheckBox(""))
            question_layout = QHBoxLayout()
            question_layout.addWidget(line_label)
            question_layout.addWidget(self.form[i])
            column1.addLayout(question_layout)
        column2 = QVBoxLayout()
        for i in range(4,7):
            line_label = QLabel(questions[i])
            self.form.append(QCheckBox(""))
            question_layout = QHBoxLayout()
            question_layout.addWidget(line_label)
            question_layout.addWidget(self.form[i])
            column2.addLayout(question_layout)
        two_column_layout.addLayout(column1)
        two_column_layout.addLayout(column2)
        layout.addLayout(two_column_layout)
        # Add a submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_clicked)
        layout.addWidget(submit_button)
        # Add the result label
        result_layout = QHBoxLayout()
        result_layout.addStretch()
        result_layout.addWidget(self.result_label, alignment=Qt.AlignCenter)
        result_layout.addStretch()
        layout.addLayout(result_layout)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Symptom Checker")
        self.setGeometry(100, 100, 400, 300)

        # Show the window
        self.show()
    def load_image(self, path):
        pixmap = QPixmap(path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
    def submit_clicked(self):
        self.output = ""
        self.input = []
        for i in range(7):
            if self.form[i].isChecked() : 
                self.input.append("yes")
            else : 
                self.input.append("no")
        engine = CarDiagnostic(self.input)
        engine.reset()
        engine.run()
        self.result_label.setText("Result: "+ engine.result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = MyInterface()
    sys.exit(app.exec_())
