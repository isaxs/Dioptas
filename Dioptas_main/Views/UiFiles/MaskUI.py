# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mask.ui'
#
# Created: Thu Jul 24 16:41:50 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_xrs_mask_widget(object):
    def setupUi(self, xrs_mask_widget):
        xrs_mask_widget.setObjectName(_fromUtf8("xrs_mask_widget"))
        xrs_mask_widget.resize(712, 530)
        xrs_mask_widget.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(xrs_mask_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(8)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.splitter = QtGui.QSplitter(xrs_mask_widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.img_pg_layout = GraphicsLayoutWidget(self.layoutWidget)
        self.img_pg_layout.setObjectName(_fromUtf8("img_pg_layout"))
        self.verticalLayout.addWidget(self.img_pg_layout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pos_lbl = QtGui.QLabel(self.layoutWidget)
        self.pos_lbl.setObjectName(_fromUtf8("pos_lbl"))
        self.horizontalLayout.addWidget(self.pos_lbl)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.mask_rb = QtGui.QRadioButton(self.widget)
        self.mask_rb.setChecked(True)
        self.mask_rb.setObjectName(_fromUtf8("mask_rb"))
        self.horizontalLayout_3.addWidget(self.mask_rb)
        self.unmask_rb = QtGui.QRadioButton(self.widget)
        self.unmask_rb.setChecked(False)
        self.unmask_rb.setObjectName(_fromUtf8("unmask_rb"))
        self.horizontalLayout_3.addWidget(self.unmask_rb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setFrameShadow(QtGui.QFrame.Raised)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.circle_btn = QtGui.QPushButton(self.widget)
        self.circle_btn.setCheckable(True)
        self.circle_btn.setChecked(False)
        self.circle_btn.setFlat(True)
        self.circle_btn.setObjectName(_fromUtf8("circle_btn"))
        self.gridLayout.addWidget(self.circle_btn, 0, 0, 1, 1)
        self.rectangle_btn = QtGui.QPushButton(self.widget)
        self.rectangle_btn.setCheckable(True)
        self.rectangle_btn.setFlat(True)
        self.rectangle_btn.setObjectName(_fromUtf8("rectangle_btn"))
        self.gridLayout.addWidget(self.rectangle_btn, 0, 1, 1, 1)
        self.point_btn = QtGui.QPushButton(self.widget)
        self.point_btn.setCheckable(True)
        self.point_btn.setFlat(True)
        self.point_btn.setObjectName(_fromUtf8("point_btn"))
        self.gridLayout.addWidget(self.point_btn, 1, 0, 1, 1)
        self.point_size_sb = QtGui.QSpinBox(self.widget)
        self.point_size_sb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.point_size_sb.setMaximum(4000)
        self.point_size_sb.setProperty("value", 20)
        self.point_size_sb.setObjectName(_fromUtf8("point_size_sb"))
        self.gridLayout.addWidget(self.point_size_sb, 1, 1, 1, 1)
        self.polygon_btn = QtGui.QPushButton(self.widget)
        self.polygon_btn.setCheckable(True)
        self.polygon_btn.setFlat(True)
        self.polygon_btn.setObjectName(_fromUtf8("polygon_btn"))
        self.gridLayout.addWidget(self.polygon_btn, 2, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.below_thresh_txt = QtGui.QLineEdit(self.widget)
        self.below_thresh_txt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.below_thresh_txt.setObjectName(_fromUtf8("below_thresh_txt"))
        self.gridLayout_2.addWidget(self.below_thresh_txt, 1, 1, 1, 1)
        self.below_thresh_btn = QtGui.QPushButton(self.widget)
        self.below_thresh_btn.setFlat(True)
        self.below_thresh_btn.setObjectName(_fromUtf8("below_thresh_btn"))
        self.gridLayout_2.addWidget(self.below_thresh_btn, 1, 0, 1, 1)
        self.cosmic_btn = QtGui.QPushButton(self.widget)
        self.cosmic_btn.setFlat(True)
        self.cosmic_btn.setObjectName(_fromUtf8("cosmic_btn"))
        self.gridLayout_2.addWidget(self.cosmic_btn, 2, 0, 1, 2)
        self.above_thresh_txt = QtGui.QLineEdit(self.widget)
        self.above_thresh_txt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.above_thresh_txt.setObjectName(_fromUtf8("above_thresh_txt"))
        self.gridLayout_2.addWidget(self.above_thresh_txt, 0, 1, 1, 1)
        self.above_thresh_btn = QtGui.QPushButton(self.widget)
        self.above_thresh_btn.setFlat(True)
        self.above_thresh_btn.setObjectName(_fromUtf8("above_thresh_btn"))
        self.gridLayout_2.addWidget(self.above_thresh_btn, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.line_5 = QtGui.QFrame(self.widget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setSpacing(8)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.invert_mask_btn = QtGui.QPushButton(self.widget)
        self.invert_mask_btn.setFlat(True)
        self.invert_mask_btn.setObjectName(_fromUtf8("invert_mask_btn"))
        self.gridLayout_4.addWidget(self.invert_mask_btn, 0, 0, 1, 1)
        self.clear_mask_btn = QtGui.QPushButton(self.widget)
        self.clear_mask_btn.setFlat(True)
        self.clear_mask_btn.setObjectName(_fromUtf8("clear_mask_btn"))
        self.gridLayout_4.addWidget(self.clear_mask_btn, 0, 1, 1, 1)
        self.undo_btn = QtGui.QPushButton(self.widget)
        self.undo_btn.setFlat(True)
        self.undo_btn.setObjectName(_fromUtf8("undo_btn"))
        self.gridLayout_4.addWidget(self.undo_btn, 1, 0, 1, 1)
        self.redo_btn = QtGui.QPushButton(self.widget)
        self.redo_btn.setFlat(True)
        self.redo_btn.setObjectName(_fromUtf8("redo_btn"))
        self.gridLayout_4.addWidget(self.redo_btn, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.line_3 = QtGui.QFrame(self.widget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.widget1 = QtGui.QWidget(self.widget)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.fill_rb = QtGui.QRadioButton(self.widget1)
        self.fill_rb.setChecked(True)
        self.fill_rb.setObjectName(_fromUtf8("fill_rb"))
        self.horizontalLayout_4.addWidget(self.fill_rb)
        self.transparent_rb = QtGui.QRadioButton(self.widget1)
        self.transparent_rb.setObjectName(_fromUtf8("transparent_rb"))
        self.horizontalLayout_4.addWidget(self.transparent_rb)
        self.verticalLayout_2.addWidget(self.widget1)
        spacerItem1 = QtGui.QSpacerItem(228, 224, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(8)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.save_mask_btn = QtGui.QPushButton(self.widget)
        self.save_mask_btn.setFlat(True)
        self.save_mask_btn.setObjectName(_fromUtf8("save_mask_btn"))
        self.gridLayout_3.addWidget(self.save_mask_btn, 0, 0, 1, 2)
        self.load_mask_btn = QtGui.QPushButton(self.widget)
        self.load_mask_btn.setFlat(True)
        self.load_mask_btn.setObjectName(_fromUtf8("load_mask_btn"))
        self.gridLayout_3.addWidget(self.load_mask_btn, 1, 0, 1, 1)
        self.add_mask_btn = QtGui.QPushButton(self.widget)
        self.add_mask_btn.setFlat(True)
        self.add_mask_btn.setObjectName(_fromUtf8("add_mask_btn"))
        self.gridLayout_3.addWidget(self.add_mask_btn, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout_2.addWidget(self.splitter)

        self.retranslateUi(xrs_mask_widget)
        QtCore.QMetaObject.connectSlotsByName(xrs_mask_widget)

    def retranslateUi(self, xrs_mask_widget):
        xrs_mask_widget.setWindowTitle(_translate("xrs_mask_widget", "XRS - Suite Mask creation", None))
        self.pos_lbl.setText(_translate("xrs_mask_widget", "TextLabel", None))
        self.mask_rb.setText(_translate("xrs_mask_widget", "mask", None))
        self.unmask_rb.setText(_translate("xrs_mask_widget", "unmask", None))
        self.circle_btn.setText(_translate("xrs_mask_widget", "Circle", None))
        self.rectangle_btn.setText(_translate("xrs_mask_widget", "Rectangle", None))
        self.point_btn.setText(_translate("xrs_mask_widget", "Point", None))
        self.polygon_btn.setText(_translate("xrs_mask_widget", "Polygon", None))
        self.below_thresh_btn.setText(_translate("xrs_mask_widget", "Below Thresh", None))
        self.cosmic_btn.setText(_translate("xrs_mask_widget", "Cosmic Removal", None))
        self.above_thresh_btn.setText(_translate("xrs_mask_widget", "Above Thresh", None))
        self.invert_mask_btn.setText(_translate("xrs_mask_widget", "Invert", None))
        self.clear_mask_btn.setText(_translate("xrs_mask_widget", "Clear", None))
        self.undo_btn.setText(_translate("xrs_mask_widget", "undo", None))
        self.redo_btn.setText(_translate("xrs_mask_widget", "redo", None))
        self.fill_rb.setText(_translate("xrs_mask_widget", "Fill", None))
        self.transparent_rb.setText(_translate("xrs_mask_widget", "Transparent", None))
        self.save_mask_btn.setText(_translate("xrs_mask_widget", "Save Mask", None))
        self.load_mask_btn.setText(_translate("xrs_mask_widget", "Load Mask", None))
        self.add_mask_btn.setText(_translate("xrs_mask_widget", "Add Mask", None))

from pyqtgraph import GraphicsLayoutWidget