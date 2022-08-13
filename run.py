import sys
from PyQt5 import QtWidgets, uic

import reset
import set
import checkbox
import valDisplay
import shift
import partialUpdate

# Get the template file
UI_TEMPLATE = "./regview.ui"


class UI:
    def __init__(self):
        self.value = 0  # Initial register value
        self.MainWindow = uic.loadUi(UI_TEMPLATE)

        self.MainWindow.SET.clicked.connect(self.SET_Click)
        self.MainWindow.RESET.clicked.connect(self.RESET_Click)

        # Hex view initialization
        self.MainWindow.RegHexVal.setMaxLength(10)  # Maximum 10bytes in HEX value view
        self.MainWindow.RegHexVal.setText('0x' + '{0:0X}'.format(self.value))
        self.MainWindow.RegHexVal.returnPressed.connect(self.Hex_View)

        # Decimal view initialization
        self.MainWindow.RegDeciVal.setMaxLength(10)  # Maximum 10 bytes in decimal view (4294967295)
        self.MainWindow.RegDeciVal.setText(str(self.value))
        self.MainWindow.RegDeciVal.returnPressed.connect(self.Deci_View)
        # self.MainWindow.RegDeciVal.setInputMask('0000000000') # Characters 0-9 only

        # Shift lineedit field initialization
        self.MainWindow.ShiftBy.setMaxLength(2)
        self.MainWindow.ShiftBy.setText(str(0))
        # self.MainWindow.ShiftBy.setInputMask('99')

        # Shift buttons
        self.MainWindow.Shift_Left.clicked.connect(self.Shift_Left)
        self.MainWindow.Shift_Right.clicked.connect(self.Shift_Right)

        # Update button
        self.MainWindow.Update.clicked.connect(self.Update_Clicked)
        self.MainWindow.Get.clicked.connect(self.Get_Clicked)

        # Re-label button
        self.MainWindow.Label.clicked.connect(self.Label_Clicked)

        # Re-label field initially blank
        for i in range(0, 32):
            label_obj = getattr(self.MainWindow, "label_{}".format(i + 33))  # Index for label start from 33
            label_obj.setText('')

        # Check box initialization
        for i in range(0, 32):
            box_obj = getattr(self.MainWindow, "checkBox_{}".format(i + 1))
            box_obj.clicked.connect(self.Click_n)

        self.MainWindow.show()

    def Click_n(self):
        self.value = checkbox.CheckBox_N_Change(self.MainWindow)
        valDisplay.Refresh_AllDisplay(self.MainWindow, self.value)

    def SET_Click(self):
        self.value = set.SetButtonClick(self.MainWindow)

    def RESET_Click(self):
        self.value = reset.ResetButtonClick(self.MainWindow)

    def Hex_View(self):
        self.value = valDisplay.HexVal_Edited(self.MainWindow)
        valDisplay.Refresh_AllDisplay(self.MainWindow, self.value)

    def Deci_View(self):
        self.value = valDisplay.DeciVal_Edited(self.MainWindow)
        valDisplay.Refresh_AllDisplay(self.MainWindow, self.value)

    def Shift_Right(self):
        self.value = shift.ShiftRightClick(self.MainWindow, self.value)
        valDisplay.Refresh_AllDisplay(self.MainWindow, self.value)

    def Shift_Left(self):
        self.value = shift.ShiftLeftClick(self.MainWindow, self.value)
        valDisplay.Refresh_AllDisplay(self.MainWindow, self.value)

    def Update_Clicked(self):
        self.value = partialUpdate.UpdateClick(self.MainWindow, self.value)
        valDisplay.Refresh_AllDisplay(self.MainWindow, self.value)

    def Get_Clicked(self):
        value = partialUpdate.BitFieldValue(self.MainWindow, self.value)
        valDisplay.Show_BitFieldVal(self.MainWindow, value)

    def Label_Clicked(self):
        valDisplay.ReLabel(self.MainWindow)


if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    my_ui = UI()
    sys.exit(APP.exec())
