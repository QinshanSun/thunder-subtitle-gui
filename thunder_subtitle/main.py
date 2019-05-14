#!/usr/bin/env python3
# coding: utf-8
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, QVBoxLayout, \
    QGroupBox, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QIcon

from thunder_subtitle import thunder_subs
from thunder_subtitle.search import get_url


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
        self.result_table = QTableWidget(25, 5, self)
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
        self.result_table.setHorizontalHeaderLabels(['Rate', 'Votes', 'Language', 'Name', 'URL'])
        self.result_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.result_table.cellDoubleClicked.connect(self.down_load_subtitle)
        self.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        v_layout.addWidget(self.horizontal_group_box)
        v_layout.addWidget(self.result_table)
        self.setLayout(v_layout)

    def open_file_name_dialog(self):
        file_dialogue = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(file_dialogue, "选择文件", "",
                                                   "All Files (*);;Python Files (*.py)", options=options)
        if file_name:
            print(file_name)
            # self.horizontal_group_box.findChildren(QLineEdit)[0].setText(file_name)
            self.file_input.setText(file_name)
            cid = thunder_subs.cid_hash_file(file_name)
            info_list = thunder_subs.get_sub_info_list(cid, 1000)
            if info_list is not None:
                self.set_result_table(info_list)
            else:
                print("超过最大重试次数后仍然未能获得正确结果")
            return info_list

    def open_file_names_dialog(self):
        file_dialogue = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(file_dialogue, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def save_file_dialog(self):
        file_dialogue = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(file_dialogue, "QFileDialog.getSaveFileName()", "",
                                                   "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            print(file_name)

    def set_result_table(self, info_list):
        self.result_table.clearContents()
        info_list.sort(key=lambda x: x['rate'], reverse=True)
        for i, x in enumerate(info_list, start=0):
            rate_item = QTableWidgetItem(x['rate'])
            vote_item = QTableWidgetItem(str(x['svote']))
            lan_item = QTableWidgetItem(x['language'])
            name_item = QTableWidgetItem(x['sname'])
            url_item = QTableWidgetItem(x['surl'])
            self.result_table.setItem(i, 0, rate_item)
            self.result_table.setItem(i, 1, vote_item)
            self.result_table.setItem(i, 2, lan_item)
            self.result_table.setItem(i, 3, name_item)
            self.result_table.setItem(i, 4, url_item)

    def down_load_subtitle(self, p_x, p_y):
        print("double clicked")
        print(p_x)
        url_tem = self.result_table.item(p_x, 4)
        movie_file_path_wo_ext = self.file_input.text().rsplit('.', 1)[0]
        if url_tem is not None:
            print(url_tem.text())
            url = url_tem.text()
            data = get_url(url)
            sub_ext = url.rsplit('.', 1)[1]
            print(data)
            sub_file_path = movie_file_path_wo_ext + '.' + sub_ext
            with open(sub_file_path, 'wb') as f:
                f.write(data)
            print('Downloaded {}'.format(sub_file_path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
