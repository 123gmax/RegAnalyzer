from PyQt5.QtWidgets import *


def UpdateClick(MainWindow, value=0):
    temp_val = 0
    mask = 0
    MsBitPosition, LsBitPosition = GetBitPosition(MainWindow)
    valueToUpdate = GetValueToUpdate(MainWindow)
    if (LsBitPosition is not None) and (valueToUpdate is not None) and (MsBitPosition is not None):
        update_size = MsBitPosition - LsBitPosition
        for i in range(0, update_size + 1):
            mask = mask | (1 << i)
        valueToUpdate = valueToUpdate & mask  # Take only those bits which fit in specified space
        mask = mask << LsBitPosition  # Position the bit
        mask = (~mask) & (0xFFFFFFFF)  # Prepare mask
        value = value & mask  # Apply mask
        value = value | (valueToUpdate << LsBitPosition)
    return value


# TODO : Get the value entered, for now hex only
def GetValueToUpdate(MainWindow):
    value = None
    if MainWindow.Temp_Val.text() != '':
        value = int(MainWindow.Temp_Val.text(), 16)
    return value


def GetBitPosition(MainWindow):
    LsBit_Pos = None
    MsBit_Pos = None
    if (MainWindow.BitPosition_Msbit.text() != '') and (MainWindow.BitPosition_Lsbit.text() != ''):
        MsBit_Pos = int(MainWindow.BitPosition_Msbit.text(), 10)
        LsBit_Pos = int(MainWindow.BitPosition_Lsbit.text(), 10)

    return MsBit_Pos, LsBit_Pos


def BitFieldValue(MainWindow, value=0):
    mask = 0
    temp_val = 0
    MsBitPosition, LsBitPosition = GetBitPosition(MainWindow)
    if (LsBitPosition is not None) and (MsBitPosition is not None):
        BitCount = MsBitPosition - LsBitPosition
        for i in range(0, BitCount + 1):
            mask = mask | (1 << i)
        mask = mask << LsBitPosition
        temp_val = (value & mask) >> LsBitPosition
    return temp_val


if __name__ == "__main__":
    print("This is not a main file!")
