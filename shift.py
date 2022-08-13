from PyQt5.QtWidgets import *


# Actions to be taken when Shift Left button is clicked
def ShiftLeftClick(MainWindow, value=0):
    new_value = value
    if MainWindow.ShiftBy.text() != '':
        LShiftBy = int(MainWindow.ShiftBy.text(), 10)
        if LShiftBy >= 0:
            new_value = new_value << LShiftBy

        new_value = new_value & 0xFFFFFFFF  # Make sure shift doesn't exceed beyond 32bit

    return new_value


def ShiftRightClick(MainWindow, value=0):
    new_value = value
    if MainWindow.ShiftBy.text() != '':
        RShiftBy = int(MainWindow.ShiftBy.text(), 10)
        if RShiftBy >= 0:
            new_value = new_value >> RShiftBy

    return new_value


if __name__ == "__main__":
    print("This is not a main file!")
