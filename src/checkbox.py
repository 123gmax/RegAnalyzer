from PyQt5.QtWidgets import *


# Actions to be taken when change in check box detected
def CheckBox_N_Change(MainWindow):
    new_val = 0
    for i in range(0, 32):
        obj = getattr(MainWindow, "checkBox_{}".format(i + 1))
        state = obj.checkState()
        if state:
            new_val = (new_val | (1 << i))
    return new_val


def TickCheckBox(MainWindow, index):
    obj = getattr(MainWindow, "checkBox_{}".format(index))
    obj.setChecked(True)


def UnTickCheckBox(MainWindow, index):
    obj = getattr(MainWindow, "checkBox_{}".format(index))
    obj.setChecked(False)


if __name__ == "__main__":
    print("This is not a main file!")
