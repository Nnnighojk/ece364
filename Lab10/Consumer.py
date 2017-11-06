import sys

from PySide.QtGui import *
from BasicUI import *
import re


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.btnClear.clicked.connect(self.clear)
        self.components = [self.txtComponentName_1,self.txtComponentName_2,self.txtComponentName_3,self.txtComponentName_4,self.txtComponentName_5,self.txtComponentName_6,self.txtComponentName_7,self.txtComponentName_8,self.txtComponentName_9,self.txtComponentName_10,self.txtComponentName_11,self.txtComponentName_12,self.txtComponentName_13,self.txtComponentName_14,self.txtComponentName_15,self.txtComponentName_16,self.txtComponentName_17,self.txtComponentName_18,self.txtComponentName_19,self.txtComponentName_20]
        self.components_count = [self.txtComponentCount_1,self.txtComponentCount_2,self.txtComponentCount_3,self.txtComponentCount_4,self.txtComponentCount_5,self.txtComponentCount_6,self.txtComponentCount_7,self.txtComponentCount_8,self.txtComponentCount_9,self.txtComponentCount_10,self.txtComponentCount_11,self.txtComponentCount_12,self.txtComponentCount_13,self.txtComponentCount_14,self.txtComponentCount_15,self.txtComponentCount_16,self.txtComponentCount_17,self.txtComponentCount_18,self.txtComponentCount_19,self.txtComponentCount_20]
        self.btnSave.clicked.connect(self.save)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)
        self.txtStudentID.textChanged.connect(self.enable_save)
        self.txtStudentName.textChanged.connect(self.enable_save)
        self.chkGraduate.stateChanged.connect(self.enable_save)
        self.cboCollege.currentIndexChanged.connect(self.enable_save)
        for item in self.components:
            item.textChanged.connect(self.enable_save)
        for item in self.components_count:
            item.textChanged.connect(self.enable_save)


    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        with open(filePath, 'r') as myFile:
            line=myFile.readlines()
        expr = r"\"(?P<g1>true|false)\""
        m = re.search(expr, line[2], re.I)
        if m is not None:
            if (m.group("g1") == 'true' or m.group("g1") == 'True' ):
                self.chkGraduate.setChecked(True)
            else:
                self.chkGraduate.setChecked(False)

        expr = r">(?P<g2>[\w\s]+)<"
        m = re.search(expr, line[2], re.I)
        if m is not None:
            self.txtStudentName.setText(m.group("g2"))

        expr = r">(?P<g3>[0-9-]+)<"
        m = re.search(expr, line[3], re.I)
        if m is not None:
            self.txtStudentID.setText(m.group("g3"))


        expr = r">(?P<g4>[\w\s]+)<"
        m = re.search(expr, line[4], re.I)
        if m is not None:
            if (m.group("g4") == 'Industrial Engineering'):
                self.cboCollege.setCurrentIndex(5)
            if (m.group("g4") == 'Aerospace Engineering'):
                self.cboCollege.setCurrentIndex(1)
            if (m.group("g4") == 'Civil Engineering'):
                self.cboCollege.setCurrentIndex(2)
            if (m.group("g4") == 'Computer Engineering'):
                self.cboCollege.setCurrentIndex(3)
            if (m.group("g4") == 'Electrical Engineering'):
                self.cboCollege.setCurrentIndex(4)
            if (m.group("g4") == 'Mechinical Engineering'):
                self.cboCollege.setCurrentIndex(6)

        i = 5
        j = 0
        count = len(line) - 2
        while i < count:
            expr1 = r"name=\"(?P<name>[\w\d\s-]+)\""
            m1 = re.search(expr1, line[i], re.I)
            expr2 = r"count=\"(?P<count>[\w\d\s-]+)\""
            m2 = re.search(expr2, line[i], re.I)
            if (m1 and m2):
                self.components[j].setText(m1.group("name"))
                self.components_count[j].setText(m2.group("count"))
            j += 1
            i += 1


    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def save(self):
        s = str()
        s += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        s += ("<Content>\n")
        if self.chkGraduate.isChecked():
            grad = "true"
        else:
            grad = "false"
        colleges=["----","Aerospace Engineering","Civil Engineering","Computer Engineering","Electrical Engineering","Industrial Engineering","Mechanical Engineering"]
        s += "    <StudentName graduate=\"{}\">{}</StudentName>\n".format(grad,self.txtStudentName.text())
        s += "    <StudentID>{}</StudentID>\n".format(self.txtStudentID.text())
        s += "    <College>{}</College>\n".format(colleges[self.cboCollege.currentIndex()])
        s += "    <Components>\n"

        components_save = []
        counts_save = []
        for i in range(20):
            if len(self.components[i].text()):
                components_save.append(self.components[i].text())
                counts_save.append(self.components_count[i].text())
        for i in range(len(components_save)):
            s += "        <Component name=\"{}\" count=\"{}\" />\n".format(components_save[i],counts_save[i])

        s += "    </Components>\n"
        s += "</Content>"
        f = open('target.xml', 'w')
        f.write(s)



    def clear(self):
        self.txtStudentID.setText("")
        self.txtStudentName.setText("")
        self.chkGraduate.setChecked(False)
        self.cboCollege.setCurrentIndex(0)
        for item in self.components:
            item.setText("")
        for j in self.components_count:
            j.setText("")
        self.btnSave.setDisabled(True)
        self.btnLoad.setEnabled(True)


    def enable_save(self):
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(False)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
