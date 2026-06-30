from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,

    QCheckBox,
    QSlider,
    QSpinBox,
    QLabel
)

import sys

import inputaction

# class JoystickFrame()

class ButtonCheckBox(QCheckBox): # you should've seen my face when this finally worked
    def __init__(self, button, text, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.text = text

        self.button = button

        self.setText(self.text)

        self.stateChanged.connect( self.input_action )

    def input_action(self, state):
        if state == Qt.CheckState.Checked.value:
            inputaction.press_button(self.button)

        else:
            inputaction.release_button(self.button)

class ButtonWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window Initialization
        self.setFixedSize( QSize(400, 300) )
        self.setWindowTitle("TAS Input")

        self.testClassButtonCheck = ButtonCheckBox(inputaction.faceA, "A", self)
        self.testClassButtonCheck.move(50, 80)

        self.testClassButtonCheck = ButtonCheckBox(inputaction.faceB, "B", self)
        self.testClassButtonCheck.move(80, 50)

        self.testClassButtonCheck = ButtonCheckBox(inputaction.faceX, "X", self)
        self.testClassButtonCheck.move(20, 50)

        self.testClassButtonCheck = ButtonCheckBox(inputaction.faceY, "Y", self)
        self.testClassButtonCheck.move(50, 20)

        self.show()



class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        # Window Initialization
        self.setFixedSize( QSize(400, 300) )
        self.setWindowTitle("TAS Input")

        self.show()

def main():
    inputaction.initialize_gamepad()

    app = QApplication(sys.argv)
    window = ButtonWidget(None)

    sys.exit( app.exec() )

if __name__ == '__main__':
    main()