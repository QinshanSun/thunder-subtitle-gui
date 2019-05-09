import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, QVBoxLayout, \
    QGroupBox, QHBoxLayout, QLabel, QTableWidget
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = '字幕下载器'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.horizontal_group_box = QGroupBox()
        self.file_label = QLabel('选择文件:', self)
        self.file_input = QLineEdit(self)
        self.open_file_button = QPushButton("打开", self)
        self.result_table = QTableWidget()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_vertical_layout()
        self.show()

    def create_vertical_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_input)
        self.open_file_button.clicked.connect(self.open_file_name_dialog)
        layout.addWidget(self.open_file_button)
        self.horizontal_group_box.setLayout(layout)
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.horizontal_group_box)
        v_layout.addWidget(self.result_table)
        self.setLayout(v_layout)

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                   "All Files (*);;Python Files (*.py)", options=options)
        if file_name:
            print(file_name)
            #self.horizontal_group_box.findChildren(QLineEdit)[0].setText(file_name)
            self.file_input.setText(file_name)

    def open_file_names_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def save_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                   "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            print(file_name)


class file_dialog(object):

    def __init__(self):
        self.__file_label = QLabel('选择文件:')
        self.__file_path_input = QLineEdit(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
