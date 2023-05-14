import sys
from PySide6.QtGui import QIcon, Qt, QFont
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel, QLineEdit,
                               QMainWindow, QPlainTextEdit, QPushButton, QSpinBox, QVBoxLayout, QWidget, QTextEdit,
                               QFileDialog
                               )
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filip Mazur - editor")
        layout = QVBoxLayout()

        self.newFileBtn = QPushButton(self)
        self.newFileBtn.clicked.connect(self.createNewFile)
        self.newFileBtn.setIcon(QIcon('./pics/newFile.png'))
        layout.addWidget(self.newFileBtn)

        self.saveFileBtn = QPushButton(self)
        self.saveFileBtn.clicked.connect(self.saveFile)
        self.saveFileBtn.setIcon(QIcon('./pics/saveFile.png'))
        layout.addWidget(self.saveFileBtn)

        self.importFileBtn = QPushButton(self)
        self.importFileBtn.clicked.connect(self.importFile)
        self.importFileBtn.setIcon(QIcon('./pics/importFile.png'))
        layout.addWidget(self.importFileBtn)

        self.textEdit = QTextEdit()
        font = QFont('Times', 11)
        self.textEdit.setFont(font)
        layout.addWidget(self.textEdit)

        self.comboFontStyle = QComboBox()
        self.comboFontStyle.setObjectName("thecombo")
        self.comboFontStyle.addItems(["Times", "Segoe UI", "Script MT Bold", "Segoe Print"])
        self.comboFontStyle.currentTextChanged.connect(self.fontFamilyChange)
        layout.addWidget(self.comboFontStyle)

        self.comboColor = QComboBox()
        self.comboColor.setObjectName("thecombo")
        self.comboColor.addItems(["black", "yellow", "green", "red","blue"])
        self.comboColor.currentTextChanged.connect(self.colorChange)
        layout.addWidget(self.comboColor)

        self.sb = QSpinBox()
        self.sb.setRange(1, 99999)
        self.sb.setValue(11)
        self.sb.valueChanged.connect(self.fontSizeChange)
        layout.addWidget(self.sb)

        self.bold = QPushButton(self)
        self.bold.clicked.connect(lambda: self.textEdit.setFontWeight(700) if self.textEdit.fontWeight() == 400 else self.textEdit.setFontWeight(400))
        self.bold.setIcon(QIcon('./pics/bold.png'))
        layout.addWidget(self.bold)

        self.alignCenter = QPushButton(self)
        self.alignCenter.clicked.connect(lambda: self.textEdit.setAlignment(Qt.AlignCenter))
        self.alignCenter.setIcon(QIcon('./pics/alignCenter.png'))
        layout.addWidget(self.alignCenter)

        self.alignJustify = QPushButton(self)
        self.alignJustify.clicked.connect(lambda: self.textEdit.setAlignment(Qt.AlignJustify))
        self.alignJustify.setIcon(QIcon('./pics/alignJustify.png'))
        layout.addWidget(self.alignJustify)

        self.alignLeft = QPushButton(self)
        self.alignLeft.clicked.connect(lambda: self.textEdit.setAlignment(Qt.AlignLeft))
        self.alignLeft.setIcon(QIcon('./pics/alignLeft.png'))
        layout.addWidget(self.alignLeft)

        self.alignRight = QPushButton(self)
        self.alignRight.clicked.connect(lambda: self.textEdit.setAlignment(Qt.AlignRight))
        self.alignRight.setIcon(QIcon('./pics/alignRight.png'))
        layout.addWidget(self.alignRight)

        self.underline = QPushButton(self)
        self.underline.clicked.connect(lambda: self.textEdit.setFontUnderline(not self.textEdit.fontUnderline()))
        self.underline.setIcon(QIcon('./pics/underline.png'))
        layout.addWidget(self.underline)

        self.italic = QPushButton(self)
        self.italic.clicked.connect(lambda: self.textEdit.setFontItalic(not self.textEdit.fontItalic()))
        self.italic.setIcon(QIcon('./pics/italic.png'))
        layout.addWidget(self.italic)

        self.container = QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)

    def colorChange(self,value):
        self.textEdit.setTextColor(value)
        print(value)

    def fontFamilyChange(self,value):
        self.textEdit.setFontFamily(value)
        print(value)

    def fontSizeChange(self,value):
        self.textEdit.setFontPointSize(value)
        print(value)

    def createNewFile(self):
        self.textEdit.setText("")
        self.sb.setValue(11)
        self.comboColor.setCurrentIndex(0)
        self.comboFontStyle.setCurrentIndex(0)

    def saveFile(self):
        file, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")
        if not file:
            return

        text = self.textEdit.toHtml()

        try:
            with open(file, 'w') as f:
                f.write(text)
        except Exception as e:
            self.error(str(e))
        else:
            self.file = file
            self.setWindowTitle(self.file if self.file else "Not Saved")

    def importFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Proprietary FileFormat (*.txt)")
        try:
            with open(file, 'r') as f:
                text = f.read()
        except Exception as e:
            self.error(str(e))
        else:
            self.file = file
            self.textEdit.setText(text)
            self.setWindowTitle(self.file if self.file else "Not Saved")
app = QApplication(sys.argv)
app.setStyle("Fusion")
w = MainWindow()
w.show()
app.exec()