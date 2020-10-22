# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configSettingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from database.database import Database
from window.tipDig import ActionWarnException


class Ui_Dialog(QtCore.QObject):
    workspaceChanged = False
    workspaceDefaultChanged = False
    modelPathChanged = False
    modelPathDefaultChanged = False
    camParaPathChanged = False
    camParaPathDefaultChanged = False
    topInfoEmit = QtCore.pyqtSignal(str, str)
    closeEmit = QtCore.pyqtSignal()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(686, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("./source/icon/document.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_workspace = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_workspace.setReadOnly(True)
        self.lineEdit_workspace.setObjectName("lineEdit_workspace")
        self.horizontalLayout_4.addWidget(self.lineEdit_workspace)
        self.button_workspaceChangeFile = QtWidgets.QToolButton(self.groupBox_2)
        self.button_workspaceChangeFile.setObjectName("button_workspaceChangeFile")
        self.horizontalLayout_4.addWidget(self.button_workspaceChangeFile)
        self.button_workspaceDefault = QtWidgets.QPushButton(self.groupBox_2)
        self.button_workspaceDefault.setObjectName("button_workspaceDefault")
        self.horizontalLayout_4.addWidget(self.button_workspaceDefault)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_weightFile = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_weightFile.setInputMask("")
        self.lineEdit_weightFile.setText("")
        self.lineEdit_weightFile.setCursorPosition(0)
        self.lineEdit_weightFile.setDragEnabled(False)
        self.lineEdit_weightFile.setReadOnly(True)
        self.lineEdit_weightFile.setPlaceholderText("")
        self.lineEdit_weightFile.setObjectName("lineEdit_weightFile")
        self.horizontalLayout_5.addWidget(self.lineEdit_weightFile)
        self.button_weightChangeFile = QtWidgets.QToolButton(self.groupBox_2)
        self.button_weightChangeFile.setObjectName("button_weightChangeFile")
        self.horizontalLayout_5.addWidget(self.button_weightChangeFile)
        self.button_weightDefault = QtWidgets.QPushButton(self.groupBox_2)
        self.button_weightDefault.setObjectName("button_weightDefault")
        self.horizontalLayout_5.addWidget(self.button_weightDefault)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.lineEdit_camaraPara = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_camaraPara.setInputMask("")
        self.lineEdit_camaraPara.setText("")
        self.lineEdit_camaraPara.setCursorPosition(0)
        self.lineEdit_camaraPara.setDragEnabled(False)
        self.lineEdit_camaraPara.setReadOnly(True)
        self.lineEdit_camaraPara.setPlaceholderText("")
        self.lineEdit_camaraPara.setObjectName("lineEdit_camaraPara")
        self.horizontalLayout_9.addWidget(self.lineEdit_camaraPara)
        self.button_camaraPara = QtWidgets.QToolButton(self.groupBox_2)
        self.button_camaraPara.setObjectName("button_camaraPara")
        self.horizontalLayout_9.addWidget(self.button_camaraPara)
        self.button_camaraPara_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_camaraPara_2.setObjectName("button_camaraPara_2")
        self.horizontalLayout_9.addWidget(self.button_camaraPara_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./source/icon/bance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_CPU = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_CPU.setObjectName("radioButton_CPU")
        self.verticalLayout_2.addWidget(self.radioButton_CPU)
        self.radioButton_GPU = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_GPU.setObjectName("radioButton_GPU")
        self.verticalLayout_2.addWidget(self.radioButton_GPU)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.commandLinkButton_CUDA = QtWidgets.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_CUDA.setDefault(True)
        self.commandLinkButton_CUDA.setObjectName("commandLinkButton_CUDA")
        self.horizontalLayout_2.addWidget(self.commandLinkButton_CUDA)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./source/icon/CPU_GPU.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./source/icon/hore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_7.addWidget(self.checkBox)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("./source/icon/chat.png"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab_3)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout_7.addWidget(self.commandLinkButton)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./source/icon/sea.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_allDefault = QtWidgets.QPushButton(Dialog)
        self.button_allDefault.setObjectName("button_allDefault")
        self.horizontalLayout.addWidget(self.button_allDefault)
        self.button_saveChange = QtWidgets.QPushButton(Dialog)
        self.button_saveChange.setObjectName("button_saveChange")
        self.horizontalLayout.addWidget(self.button_saveChange)
        self.button_saveChangeAndExit = QtWidgets.QPushButton(Dialog)
        self.button_saveChangeAndExit.setObjectName("button_saveChangeAndExit")
        self.horizontalLayout.addWidget(self.button_saveChangeAndExit)
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout.addWidget(self.button_cancel)
        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        # 默认选项
        self.setOpenStatus()
        self.button_workspaceChangeFile.clicked.connect(self.actionChangeWorkspace)
        self.button_workspaceDefault.clicked.connect(self.actionDefaultWorkspace)
        self.button_weightChangeFile.clicked.connect(self.actionChangeModelPath)
        self.button_weightDefault.clicked.connect(self.actionDefaultModelPath)
        self.button_camaraPara.clicked.connect(self.actionChangeCamaraParaPath)
        self.button_camaraPara_2.clicked.connect(self.actionDefaultCamaraParaPath)
        self.radioButton_CPU.clicked.connect(self.actionCPU)
        self.radioButton_GPU.clicked.connect(self.actionGPU)
        self.commandLinkButton_CUDA.clicked.connect(self.actionCUDAConfig)
        self.checkBox.clicked.connect(self.actionSpeaker)
        self.commandLinkButton.clicked.connect(self.commonLinkToOnline)

        self.button_allDefault.clicked.connect(self.actionSetAllDefault)
        self.button_saveChange.clicked.connect(self.actionSaveChange)
        self.button_saveChangeAndExit.clicked.connect(self.actionSaveChangeAndExit)
        self.button_cancel.clicked.connect(self.actionCancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "参数设置"))
        self.label.setText(_translate("Dialog", "交通场景智能监控综合系统参数设置"))
        self.label_5.setText(_translate("Dialog", " 说明\n"
                                                  "\n"
                                                  " 1. 无特别指定，工作空间将作为所有处理结果的保存区域,\n"
                                                  " 会自动建立workspace文件，图像识别可以自定义另存；\n"
                                                  " 2. 模型文件为识别所需权重文件。\n"
                                                  "  "))
        self.groupBox_2.setTitle(_translate("Dialog", "路径设置"))
        self.label_4.setText(_translate("Dialog", "工作空间："))
        self.button_workspaceChangeFile.setText(_translate("Dialog", "..."))
        self.button_workspaceDefault.setText(_translate("Dialog", "默认"))
        self.label_6.setText(_translate("Dialog", "模型（权重文件）："))
        self.button_weightChangeFile.setText(_translate("Dialog", "..."))
        self.button_weightDefault.setText(_translate("Dialog", "默认"))
        self.label_10.setText(_translate("Dialog", "道路监控相机参数："))
        self.button_camaraPara.setText(_translate("Dialog", "..."))
        self.button_camaraPara_2.setText(_translate("Dialog", "默认"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "工作路径"))
        self.groupBox.setTitle(_translate("Dialog", "运行环境"))
        self.label_2.setText(_translate("Dialog", " 说明\n"
                                                  "\n"
                                                  " 1. 默认采用CPU环境运行；\n"
                                                  " 2. 如需采用GPU加速功能，需要另行配置CUDA。\n"
                                                  "  "))
        self.radioButton_CPU.setText(_translate("Dialog", "CPU（默认）"))
        self.radioButton_GPU.setText(_translate("Dialog", "GPU加速（需要配置CUDA）"))
        self.commandLinkButton_CUDA.setText(_translate("Dialog", "配置CUDA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "运行环境"))
        self.label_8.setText(_translate("Dialog", "系统语音："))
        self.checkBox.setText(_translate("Dialog", "开启"))
        self.commandLinkButton.setText(_translate("Dialog", "在线帮助文档"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "其他设置"))
        self.button_allDefault.setText(_translate("Dialog", "全部恢复默认"))
        self.button_saveChange.setText(_translate("Dialog", "保存修改"))
        self.button_saveChangeAndExit.setText(_translate("Dialog", "保存并关闭"))
        self.button_cancel.setText(_translate("Dialog", "取消"))

    def setOpenStatus(self):
        """
        打开设置时的状态
        :return:
        """
        self._sendTopEmit("V", "进入设置面板，提示：设置中每进行一次更改都将在本次生效。下次打开将恢复初始状态。如有需要固定设置的结果，更改后进行保存，可以将其持久化。")
        self.radioButton_CPU.setChecked(True)
        self.lineEdit_workspace.setText(Database.workspace)
        self.lineEdit_weightFile.setText(Database.modelPath)
        self.lineEdit_camaraPara.setText(Database.camParamPath)
        self.workspaceChanged = False
        self.workspaceDefaultChanged = False
        self.modelPathChanged = False
        self.modelPathDefaultChanged = False
        if Database.envir == "CPU":
            self.radioButton_CPU.setChecked(True)
        else:
            self.radioButton_GPU.setChecked(True)
        self.checkBox.setChecked(Database.speaker)

    def actionChangeWorkspace(self):
        getDir = QtWidgets.QFileDialog.getExistingDirectory(self.parent(), "选择工作空间", Database.workspace)
        if getDir != "":
            self.user_workspaceDir = getDir + "/workspace"
            if os.path.exists(self.user_workspaceDir) is False:  # 路径不存在，创建
                os.mkdir(self.user_workspaceDir)
            self.lineEdit_workspace.setText(self.user_workspaceDir)
            Database.workspace = self.user_workspaceDir
            # 设定动作状态，为全局保存作准备
            self.workspaceChanged = True
            self.workspaceDefaultChanged = False

    def actionDefaultWorkspace(self):
        self.lineEdit_workspace.setText(Database.default_workspace)
        Database.workspace = Database.default_workspace
        self.workspaceChanged = False
        self.workspaceDefaultChanged = True

    def actionChangeModelPath(self):
        path, type = QtWidgets.QFileDialog.getOpenFileName(self.parent(), "选择模型", Database.modelPath,
                                                           "All File(*);;h5(*.h5);;or5(*.or5);;")
        if path != "":
            self.lineEdit_weightFile.setText(path)
            Database.modelPath = path
            self.modelPathChanged = True

    def actionDefaultModelPath(self):
        self.lineEdit_weightFile.setText(Database.default_modelPath)
        Database.modelPath = Database.default_modelPath

    def actionChangeCamaraParaPath(self):
        path, type = QtWidgets.QFileDialog.getOpenFileName(self.parent(), "选择模型", Database.camParamPath,
                                                           "All File(*);;h5(*.h5);;or5(*.or5);;")
        if path != "":
            self.lineEdit_camaraPara.setText(path)
            Database.camParamPath = path
            self.camParaPathChanged = True

    def actionDefaultCamaraParaPath(self):
        self.lineEdit_camaraPara.setText(Database.default_camParamPath)
        Database.camParamPath = Database.default_camParamPath

    def actionCPU(self):
        Database.envir = "CPU"

    def actionGPU(self):  # 需要配置CUDA才能真正切换到GPU
        self._sendTopEmit("T", "当前选择GPU加速，请进行CUDA配置以生效")

    def actionCUDAConfig(self):
        # if self.radioButton_GPU.isChecked():
        #     Database.envir = "GPU"
        self._sendTopEmit("V", "该功能需要NVIDIA显卡的支持")
        self._sendTopEmit("T", "当前功能待开发")

    def actionSpeaker(self):
        if self.checkBox.isChecked():
            Database.speaker = 1
        else:
            Database.speaker = 0

    def actionSetAllDefault(self):
        """
        全部恢复默认
        :return:
        """
        tabIndex = self.tabWidget.currentIndex()
        database = Database()
        if tabIndex == 0:  # 路径设置
            self._sendTopEmit("I", "恢复默认文件路径")
            Database.workspace = Database.default_workspace
            Database.modelPath = Database.default_modelPath
            self.lineEdit_workspace.setText(Database.workspace)
            self.lineEdit_weightFile.setText(Database.modelPath)
            # 恢复json文件
            database.writeJsonKeyValue("workspace", Database.workspace)
            database.writeJsonKeyValue(key1="model", key2="modelPath", value=Database.default_modelPath)
            self._sendTopEmit("T", "写入json配置，完成默认工作路径恢复")

        elif tabIndex == 1:
            self._sendTopEmit("I", "恢复默认运行环境")
            Database.envir = Database.default_envir
            self.radioButton_CPU.setChecked(True)
            # 恢复json文件
            database.writeJsonKeyValue("envir", Database.envir)
            self._sendTopEmit("T", "写入json配置，完成默认运行环境恢复")
        else:
            self._sendTopEmit("I", "恢复默认其他设置")
            Database.speaker = Database.default_speaker
            self.checkBox.setChecked(False)
            # 恢复json文件
            database.writeJsonKeyValue("speaker", Database.default_speaker)
            self._sendTopEmit("T", "写入json配置，完成默认其他设置恢复")

    def actionSaveChange(self):
        self.saveChange()
        self._sendTopEmit("T", "已保存更改")

    def actionSaveChangeAndExit(self):
        self.saveChange()
        self._sendTopEmit("T", "已保存更改，退出设置")
        # 退出
        self.closeEmit.emit()

    def saveChange(self):
        tabIndex = self.tabWidget.currentIndex()
        database = Database()
        if tabIndex == 0:  # 路径设置
            if self.workspaceChanged or self.workspaceDefaultChanged:
                self._sendTopEmit("I", "保存更改工作空间...")
                # 修改json文件
                database.writeJsonKeyValue("workspace", Database.workspace)
            if self.modelPathChanged or self.modelPathDefaultChanged:
                self._sendTopEmit("I", "保存更改模型路径...")
                # 修改json文件
                database.writeJsonKeyValue(key1="model", key2="modelPath", value=Database.modelPath)
            if self.camParaPathChanged or self.camParaPathDefaultChanged:
                self._sendTopEmit("I", "保存更改相机参数...")
                # 修改json文件
                database.writeJsonKeyValue(key1="model", key2="camParamPath", value=Database.camParamPath)

            self._sendTopEmit("I", "写入json配置，完成工作空间持久性更改")

        elif tabIndex == 1:
            self._sendTopEmit("I", "保存更改运行环境...")
            # 修改json文件
            database.writeJsonKeyValue("envir", Database.envir)
            self._sendTopEmit("I", "写入json配置，完成默认更改")
        else:
            self._sendTopEmit("I", "保存其他设置的更改...")
            # 修改json文件
            database.writeJsonKeyValue("speaker", Database.speaker)
            self._sendTopEmit("I", "写入json配置，完成默认更改")

    def actionCancel(self):
        user_action = ActionWarnException(self.parent()).actionWarnException("R",
                                                                             "退出设置，所进行的修改如不保存，将只在\n本次使用生效，再次打开将恢复默认设置，\n")
        if user_action:
            self.closeEmit.emit()

    def _sendTopEmit(self, type, strInfo):
        self.topInfoEmit.emit(type, strInfo)

    def commonLinkToOnline(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(Database.onlineHelpLink))
