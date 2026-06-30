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

class ButtonCheckBox(QCheckBox):
    def __init__(self, label, *args, **kwargs):
    # def __init__(self, parent, label: str, button):
        super().__init__(label, *args, **kwargs)
        # super().__init__(parent, label, button)

        self.label = label
        # self.button = button

        # self.stateChanged.connect( self.input_action(button) )

    # def input_action(button):
    #     if self.setChecked == True:
    #         inputaction.press_button(button)

    #     if self.setChecked == False:
    #         inputaction.release_button(button)

def button_checkbox(parent, label: str, button, moveX: int, moveY: int):
    widget = QCheckBox(label, parent=parent)

    widget.move(moveX, moveY)

    widget.stateChanged.connect( lambda: input_action(button) ) 

    def input_action(button):
        if widget.setChecked == True:
            inputaction.press_button(button)

        if widget.setChecked == False:
           inputaction.release_button(button)

class ButtonWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window Initialization
        self.setFixedSize( QSize(400, 300) )
        self.setWindowTitle("TAS Input")

        self.testButtonCheck = button_checkbox(self, "A", inputaction.faceA, 20, 20)
        # self.testButtonCheck = ButtonCheckBox("A")

        self.show()



class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        # Window Initialization
        self.setFixedSize( QSize(400, 300) )
        self.setWindowTitle("TAS Input")

        self.show()

def main():
    inputaction.initialize_gamepad

    app = QApplication(sys.argv)
    window = ButtonWidget(None)

    sys.exit( app.exec() )

if __name__ == '__main__':
    main()