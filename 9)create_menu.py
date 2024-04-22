import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QAction, QWidget,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
    
        menubar = self.menuBar()
        file = menubar.addMenu("Dosya")
        edit = menubar.addMenu("Edit")

        open = QAction("Open",self)
        open.setShortcut("Ctrl+O")

        save = QAction("Save",self)
        save.setShortcut("Ctrl+S")

        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        file.addAction(open)
        file.addAction(save)
        file.addAction(exit)

        self.setWindowTitle("Create Menu")
        self.show()

        add = edit.addMenu("Add")

        page = QAction("Add Page",self)
        image = QAction("Add Image",self)

        add.addAction(page)
        add.addAction(image)

        exit.triggered.connect(self.close_up)
        file.triggered.connect(self.click)

    def close_up(self):
        qApp.quit()
    def click(self,action):
        if action.text() == "Open":
            print("Open command was run")
        elif action.text() == "Save":
            print("Save command was run")

object = QApplication(sys.argv)
menu = Menu()

sys.exit(object.exec())