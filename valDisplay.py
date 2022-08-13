from PyQt5.QtWidgets import *
import checkbox
import partialUpdate


def HexVal_Edited(MainWindow):
    # print('Hex view change')
    new_val = 0
    if (MainWindow.RegHexVal.text()[2:] != '') and (MainWindow.RegHexVal.text()[0:1] != '0x'):
        new_val = int(MainWindow.RegHexVal.text(), 16)
    elif MainWindow.RegHexVal.text()[0:] != '':
        new_val = int(MainWindow.RegHexVal.text(), 16)

    return new_val


def DeciVal_Edited(MainWindow):
    new_val = 0
    if MainWindow.RegDeciVal.text() != '':
        new_val = int(MainWindow.RegDeciVal.text(), 10)
    return new_val


def Refresh_AllDisplay(MainWindow, value):
    MainWindow.RegHexVal.setText('0x' + '{0:0X}'.format(value))  # Hex display
    MainWindow.RegDeciVal.setText(str(value))  # Decimal display
    # Set the checkbox based on value
    for i in range(0, 32):
        isSet = 0
        isSet = (value) & (1 << i)
        if isSet:
            checkbox.TickCheckBox(MainWindow, i + 1)
        else:
            checkbox.UnTickCheckBox(MainWindow, i + 1)


# TODO : Allow display in binary too
def Show_BitFieldVal(MainWindow, value):
    MainWindow.Temp_Val.setText('{0:0x}'.format(value))  # Display in hex


# TODO : Retain label from click to click
def ReLabel(MainWindow):
    # Clear all label first
    for i in range(0, 32):
        obj = getattr(MainWindow, "label_{}".format(i + 33))  # Index for label start from 33
        obj.setText('')
    MsBitPosition, LsBitPosition = partialUpdate.GetBitPosition(MainWindow)
    x = 0
    if (LsBitPosition is not None) and (MsBitPosition is not None):
        for i in range(LsBitPosition, MsBitPosition + 1):
            obj = getattr(MainWindow, "label_{}".format(i + 33))
            obj.setText(str(x))
            x = x + 1


if __name__ == "__main__":
    print("This is not a main file!")
