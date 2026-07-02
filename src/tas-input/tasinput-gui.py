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

import inputaction as ia




# class JoystickFrame(QSlider):

class ButtonCheckBox(QCheckBox):
    def __init__(self, placeX: int, placeY: int, button, text, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.move(placeX, placeY)

        self.text = text

        self.button = button

        self.setText(self.text)

        self.stateChanged.connect( self.input_action )

    def input_action(self, state):
        if state == Qt.CheckState.Checked.value:
            ia.press_button(self.button)

        else:
            ia.release_button(self.button)

class ButtonWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window Initialization
        self.setFixedSize( QSize(400, 300) )
        self.setWindowTitle("TAS Input")

        # Widget Layout

        gapRow: int = 27

        buttonLayoutStart: int = 160

        menuButtonPosition: int = 190

        self.dPadDirections = self.four_button_checkbox_layout(
            self, 20, buttonLayoutStart,
            ia.thumbButtonLeft,  "L-Stick",
            ia.bumperLeft,  "LB",
            ia.dpadUp,      "D-Up",
            ia.dpadLeft,    "D-Left",
            ia.dpadDown,    "D-Down",
            ia.dpadRight,   "D-Right"
        )

        self.startButton = ButtonCheckBox(
            menuButtonPosition,
            buttonLayoutStart + gapRow,
            ia.menuStart, "Start",
            self
        )

        self.backButton = ButtonCheckBox(
            menuButtonPosition,
            ( buttonLayoutStart + int(gapRow * 2) ),
            ia.menuBack, "Back",
            self
        )

        self.faceButtons = self.four_button_checkbox_layout(
            self, 270, buttonLayoutStart,
            ia.thumbButtonRight,  "R-Stick",
            ia.bumperRight, "RB",
            ia.faceY, "Y",
            ia.faceX, "X",
            ia.faceA, "A",
            ia.faceB, "B"
        )

        self.show()

    # this, along with other custom widgets, has GOT to go to its own module if possible
    def four_button_checkbox_layout(
        self, parent,
        placeX: int, placeY: int,
        stickButton,    stickText: str,
        bumperButton,   bumperText: str,
        northButton,    northText: str,
        westButton,     westText: str,
        southButton,    southText: str,
        eastButton,     eastText: str
    ):
        gapColumn: int = 40
        gapRow: int = 27

        bumperButtonCheck = ButtonCheckBox(
            (placeX + gapColumn), placeY,
            bumperButton, bumperText,
            parent
        )

        northButtonCheck = ButtonCheckBox(
            (placeX + gapColumn), (placeY + gapRow),
            northButton, northText,
            parent
        )
        
        northButtonCheck = ButtonCheckBox(
            placeX, int(placeY + gapRow * 2),
            westButton, westText,
            parent
        )

        southButtonCheck = ButtonCheckBox(
            (placeX + gapColumn),
            ( placeY + int(gapRow * 3) ),
            southButton, southText,
            parent
        )

        northButtonCheck = ButtonCheckBox(
            (placeX + int(gapColumn * 2) ),
            ( placeY + int(gapRow * 2) ),
            eastButton, eastText,
            parent
        )

        stickButtonCheck = ButtonCheckBox(
            (placeX + gapColumn),
            ( placeY + int(gapRow * 4) ),
            stickButton, stickText,
            parent
        )



class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        # Window Initialization
        self.setFixedSize( QSize(400, 300) )
        self.setWindowTitle("TAS Input")

        self.show()

def main():
    ia.initialize_gamepad()

    app = QApplication(sys.argv)
    window = ButtonWidget(None)

    sys.exit( app.exec() )

if __name__ == '__main__':
    main()