from PyQt5.QtWidgets import *


# Actions to be taken when RESET button is clicked
def ResetButtonClick(MainWindow):
    # print('RESET clicked')
    val = 0
    # Set all click box to zero
    for i in range(0, 32):
        obj = getattr(MainWindow, "checkBox_{}".format(i + 1))
        obj.setChecked(False)

    # Set both Hex and Decimal view to MIN value
    MainWindow.RegDeciVal.setText(str(val))
    MainWindow.RegHexVal.setText('0x'+'{0:0X}'.format(val))

    return val


if __name__ == "__main__":
    print("This is not a main file!")
