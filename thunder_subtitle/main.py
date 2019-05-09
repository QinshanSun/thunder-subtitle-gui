import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, QVBoxLayout, \
    QGroupBox, QHBoxLayout, QLabel, QTableWidget
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.horizontal_group_box = QGroupBox()
        self.title = '字幕下载器'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.open_file_name_dialog()
        # self.open_file_names_dialog()
        # self.save_file_dialog()
        self.create_horizontal_layout()

        self.create_vertical_layout()
        self.show()

    def create_horizontal_layout(self):
        layout = QHBoxLayout()
        file_label = QLabel('选择文件:', self)
        layout.addWidget(file_label)
        file_input = QLineEdit(self)
        layout.addWidget(file_input)
        open_file_button = QPushButton("打开", self)
        open_file_button.clicked.connect(self.open_file_name_dialog)
        layout.addWidget(open_file_button)
        self.horizontal_group_box.setLayout(layout)

    def create_vertical_layout(self):
        layout = QVBoxLayout()
        result_table = QTableWidget()
        layout.addWidget(self.horizontal_group_box)
        layout.addWidget(result_table)
        self.setLayout(layout)

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                   "All Files (*);;Python Files (*.py)", options=options)
        if file_name:
            print(file_name)
            self.horizontal_group_box.findChildren(QLineEdit)[0].setText(file_name)

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
