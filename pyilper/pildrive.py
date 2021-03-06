#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pyILPER 1.2.1 (python) for Linux
#
# An emulator for virtual HP-IL devices for the PIL-Box
# derived from ILPER 1.4.5 for Windows
# Copyright (c) 2008-2013   Jean-Francois Garnier
# C++ version (c) 2013 Christoph Gießelink
# Python Version (c) 2015 Joachim Siebold
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# Virtual drive tab object classes -------------------------------------------
#
# Changelog
# 24.09.2015 cg
# - expanded LIF filename filter with *.lif and *.LIF extention
# 29.11.2015 jsi
# - working directory is default when opening lif files
# - do not check lif medium version
# - invalid layout if all media information are zero
# - refresh dir list if drive has not been talker for nn seconds
# - use device lock instead of pausing PIL-Loop
# 01.12.2015 jsi
# - clear dirlist if illegal medium is mounted
# 18.12.2015 jsi
# - added dropdown command button in drive tab
# - added context menu for entries in directory listing
# 31.12.2015 jsi
# - add view option to context menu
# 03.01.2016 jsi
# - added label option to dropdown command menu
# - filename and drivetype controls are disabled if the drive is enabled
# - rename 'Help' menu entry to 'Manual'
# 05.01.2016 jsi
# - initialize filename an drivetype controls properly at program start
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 08.01.2016 jsi
# - introduced lifcore, refactoring
# - do not lock pildevice, if pyilper is disabled
# 10.01.2016 jsi
# - show tooltips for disabled controls in the drive tab
# 16.01.2016 jsi
# - revert disabling filename and drivetype controls if the drive is enabled
# - allow arbitrary disk layouts 
# 30.01.2016 jsi
# - enable file management controls only if a compatible version of the LIF
#   utilities is installed
# 31.01.2016 jsi
# - added workdir parameter to call of cls_lifview
# 19.02.2016 jsi:
# - added character set combo box to cls_tabdrive
# - put text in front of the combo boxes at the bottom of the tabs
# 05.04.2016 jsi:
# - issue warinings about invalid LIF headers only when mounting those files, hint by cg
# 04.12.2016 jsi
# - allow LIF directories not starting at record 2
# 04.02.2016 jsi
# - added missing argument to sortbyColumn (QT5 fix)
# 19.02.2017 jsi
# - font size of the directory listing of the LifDirWidget can now be 
#   configured. The row height is now properly adjusted to the font height
# 17.08.2017 jsi
# - set did to empty string instead of none
# 20.08.2017 jsi
# - add create barcode to context menu
# 28.08.2017 jsi
# - get papersize config parameter in the constructor of the tab widget
# 01.09.2017 jsi
# - added output directory list to pdf to tools
# 03.09.2017 jsi
# - register pildevice is now method of commobject
# 20.09.2017 jsi
# - make directory font size reconfigurable on runtime
# 28.10.2017 jsi
# - lifutils_installed is now variable of cls_pyilper
# 30.10.2017 jsi 
# - bugfix: close file in getMediumInfo
#
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import threading
import os
from .pilcore import *
from .pildevbase import cls_pildevbase
from .pilwidgets import cls_tabgeneric
from .pilconfig import PilConfigError, PILCONFIG
from .pilcharconv import CHARSET_HP71, charsets
from .lifutils import cls_LifFile,cls_LifDir,LifError, getLifInt, putLifInt
from .lifcore import *
from .lifexec import cls_lifpack, cls_lifpurge, cls_lifrename, cls_lifexport, cls_lifimport, cls_lifview, cls_liflabel, check_lifutils, cls_lifbarcode
from .pilpdf import cls_pdfprinter,cls_textItem


class cls_tabdrive(cls_tabgeneric):

   DEV_CASS=0
   DEV_DISK=1
   DEV_HDRIVE1=2

   deviceinfo= { }
   deviceinfo[DEV_CASS]=["",0x10]
   deviceinfo[DEV_DISK]=["HP9114B",0x10]
   deviceinfo[DEV_HDRIVE1]=["HDRIVE1",0x10]

   # Medium types
   MEDIUM_CASS=0
   MEDIUM_DISK=1
   MEDIUM_HDRIVE1=2
   MEDIUM_HDRIVE2=3
   MEDIUM_HDRIVE4=4
   MEDIUM_HDRIVE8=5
   MEDIUM_HDRIVE16=6
   MEDIUM_UNKNOWN= -1
   
   mediainfo= { }
   mediainfo[MEDIUM_CASS]=['HP82161A Cassette',2,1,256]
   mediainfo[MEDIUM_DISK]=['HP9114B double sided disk',77,2,16]
   mediainfo[MEDIUM_HDRIVE1]=['HDRIVE1 640K disk',80,2,16]
   mediainfo[MEDIUM_HDRIVE2]=['HDRIVE1 2MB disk',125,1,64]
   mediainfo[MEDIUM_HDRIVE4]=['HDRIVE1 4MB disk',125,2,64]
   mediainfo[MEDIUM_HDRIVE8]=['HDRIVE1 8MB disk',125,4,64]
   mediainfo[MEDIUM_HDRIVE16]=['HDRIVE1 16MB disk',125,8,64]
   mediainfo[MEDIUM_UNKNOWN]=['unknown',0,0,0]
   
   
   def __init__(self,parent,name):
      super().__init__(parent,name)
#
#     Set default values
#
      self.filename= PILCONFIG.get(self.name,"filename","")
      self.drivetype= PILCONFIG.get(self.name,"drivetype",self.DEV_HDRIVE1)
      self.charset= PILCONFIG.get(self.name,"charset",CHARSET_HP71)
      self.papersize=PILCONFIG.get("pyilper","papersize")

#
#     Build GUI 
#
      self.hbox1= QtWidgets.QHBoxLayout()
      self.lbltxt1=QtWidgets.QLabel("LIF Image File: ")
      self.lblFilename=QtWidgets.QLabel()
      self.butFilename=QtWidgets.QPushButton()
      self.butFilename.setText("change")
      self.hbox1.addWidget(self.lbltxt1)
      self.hbox1.addWidget(self.lblFilename)
      self.hbox1.addStretch(1)
      self.hbox1.addWidget(self.butFilename)
      self.hbox1.setContentsMargins(15,10,10,5)

      self.gbox = QtWidgets.QGroupBox()
      self.gbox.setFlat(True)
      self.gbox.setTitle("Drive Type")
      self.vbox2= QtWidgets.QVBoxLayout()
      self.radbutCass = QtWidgets.QRadioButton(self.gbox)
      self.radbutCass.setText("HP82161A")
      self.vbox2.addWidget(self.radbutCass)
      self.radbutDisk = QtWidgets.QRadioButton(self.gbox)
      self.radbutDisk.setText("HP9114A")
      self.radbutHdrive1 = QtWidgets.QRadioButton(self.gbox)
      self.vbox2.addWidget(self.radbutDisk)
      self.radbutHdrive1.setText("HDRIVE1")
      self.vbox2.addWidget(self.radbutHdrive1)
      self.gbox.setLayout(self.vbox2)
      self.gbox_buttonlist=[self.radbutCass, self.radbutDisk, self.radbutHdrive1]
      self.vbox3= QtWidgets.QVBoxLayout()
      self.vbox3.addWidget(self.gbox)
      self.vbox3.addStretch(1)

      self.vbox1= QtWidgets.QVBoxLayout()
      self.lifdir=cls_LifDirWidget(self,10,FONT,self.papersize)
      self.vbox1.addWidget(self.lifdir)

      self.hbox2= QtWidgets.QHBoxLayout()
      self.hbox2.addLayout(self.vbox1)
      self.hbox2.addLayout(self.vbox3)
      self.hbox2.setContentsMargins(10,3,10,3)

      self.hbox3= QtWidgets.QHBoxLayout()
      self.hbox3.addWidget(self.cbActive)
      self.hbox3.setContentsMargins(10,3,10,3)
#
#     Initialize file management tool bar
#
      self.tBar= QtWidgets.QToolBar()
      self.tBut= QtWidgets.QToolButton(self.tBar)
      self.menu= QtWidgets.QMenu(self.tBut)
      self.tBut.setMenu(self.menu)
      self.tBut.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
      self.actPack= self.menu.addAction("Pack")
      self.actImport= self.menu.addAction("Import")
      self.actLabel=self.menu.addAction("Label")
      self.actDirList=self.menu.addAction("Directory Listing")
      self.tBut.setText("Tools")
      self.tBut.setEnabled(False)
      self.hbox3.addWidget(self.tBut)
#
#     Initialize charset combo box
#
      self.lbltxtc=QtWidgets.QLabel("Charset ")
      self.comboCharset=QtWidgets.QComboBox()
      for txt in charsets:
         self.comboCharset.addItem(txt)
      self.hbox3.addWidget(self.lbltxtc)
      self.hbox3.addWidget(self.comboCharset)
      self.comboCharset.setEnabled(False)

      self.hbox3.addStretch(1)

      self.vbox= QtWidgets.QVBoxLayout()
      self.vbox.addLayout(self.hbox1)
      self.vbox.addLayout(self.hbox2)
      self.vbox.addLayout(self.hbox3)
      self.setLayout(self.vbox)
#
#     basic initialization
#
      self.lblFilename.setText(self.filename)
      self.butFilename.setEnabled(False)
      self.setDrivetypeChecked()
      for w in self.gbox_buttonlist:
         w.setEnabled(False)
      self.lblFilename.setText(self.filename)
      self.lifdir.setFileName(self.filename)
      self.comboCharset.setCurrentIndex(self.charset)

#
#     connect actions
#   
      self.radbutCass.clicked.connect(self.do_drivetypeChanged)
      self.radbutDisk.clicked.connect(self.do_drivetypeChanged)
      self.radbutHdrive1.clicked.connect(self.do_drivetypeChanged)
      self.butFilename.clicked.connect(self.do_filenameChanged)
      self.actPack.triggered.connect(self.do_pack)
      self.actImport.triggered.connect(self.do_import)
      self.actLabel.triggered.connect(self.do_label)
      self.actDirList.triggered.connect(self.do_dirlist)
      self.comboCharset.activated[str].connect(self.do_changeCharset)
#
#     create HPIL-device
#
      self.pildevice= cls_pildrive(isWINDOWS())

#
#     refresh timer
#
      self.timer=QtCore.QTimer()
      self.timer.timeout.connect(self.update_hdrive)
      self.update_pending= False
#
#     enable/disable GUI elements
#
      self.toggle_controls()
#
#     reconfigure
#
   def reconfigure(self):
      self.lifdir.reconfigure()

#
#     enable/disable
#
   def enable(self):
      super().enable()
      self.parent.commthread.register(self.pildevice,self.name)
      self.pildevice.setactive(PILCONFIG.get(self.name,"active"))
      did,aid= self.deviceinfo[self.drivetype]
      self.pildevice.setdevice(did,aid)
      status, tracks, surfaces, blocks= self.lifMediumCheck(self.filename,True)
      if not status:
         self.filename=""
         PILCONFIG.put(self.name,'filename',self.filename)
         try:
            PILCONFIG.save()
         except PilConfigError as e:
            reply=QtWidgets.QMessageBox.critical(self.parent.ui,'Error',e.msg+': '+e.add_msg,QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Ok)
      self.pildevice.sethdisk(self.filename,tracks,surfaces,blocks)
      self.lblFilename.setText(self.filename)
      self.lifdir.setFileName(self.filename)

   def disable(self):
      super().disable()
#     self.timer.stop()
#
#  enable/disable lif image file controls:
#  - change drive type
#  - change drive type
#  - tools teardown menu

   def toggle_active(self):
      self.toggle_controls()

   def toggle_controls(self):
      self.butFilename.setEnabled(True)
      for w in self.gbox_buttonlist:
         w.setEnabled(True)
      if self.active:
         self.tBut.setEnabled(False)
         self.comboCharset.setEnabled(False)
         self.tBut.setToolTip("To use this menu, please disable the device first")
      else:
         self.tBut.setToolTip("")
         if self.filename != "" and self.parent.lifutils_installed:
            self.tBut.setEnabled(True)
            self.comboCharset.setEnabled(True)
#
#  set drive type checked
#
   def setDrivetypeChecked(self):
      i=0
      for w in self.gbox_buttonlist:
         if i == self.drivetype:
            w.setChecked(True)
         else:
            w.setChecked(False)
         i+=1
#
#  becomes visible, activate update timer
#
   def becomes_visible(self):
      self.timer.start(REFRESH_RATE)
      return
#
#  becomes invisible, deactivate update timer
#
   def becomes_invisible(self):
      self.timer.stop()
      return
#
#  Callbacks
#
   def do_changeCharset(self,text):
      self.charset=self.comboCharset.findText(text)
      PILCONFIG.put(self.name,'charset',self.charset)

   def do_filenameChanged(self):
      flist= self.get_lifFilename()
      if flist is None:
         return
      status, tracks, surfaces, blocks= self.lifMediumCheck(flist[0],False)
      if status:
         self.filename=flist[0]
      else:
         self.filename=""
      PILCONFIG.put(self.name,'filename',self.filename)
      try:
         PILCONFIG.save()
      except PilConfigError as e:
         reply=QtWidgets.QMessageBox.critical(self.parent.ui,'Error',e.msg+': '+e.add_msg,QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Ok)

      if self.pildevice is not None:
         self.pildevice.setlocked(True)
         self.pildevice.sethdisk(self.filename,tracks,surfaces,blocks)
         self.pildevice.setlocked(False)
      self.lblFilename.setText(self.filename)
      self.lifdir.setFileName(self.filename)
      if self.filename=="":
         self.lifdir.clear()
      else:
         self.lifdir.refresh()
      self.toggle_controls()

   def do_drivetypeChanged(self):
      i=0
      for w in self.gbox_buttonlist:
         if w.isChecked():
            self.drivetype=i
            break
         i+=1
      PILCONFIG.put(self.name,'drivetype', self.drivetype)
#
#     remove filename
#
      if self.filename != "":
         self.filename=""
         PILCONFIG.put(self.name,'filename',self.filename)
         self.lblFilename.setText(self.filename)
         self.lifdir.clear()
         reply=QtWidgets.QMessageBox.warning(self.parent.ui,'Warning',"Drive type changed. You have to reopen the LIF image file",QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Ok)
      did,aid= self.deviceinfo[self.drivetype]
      try:
         PILCONFIG.save()
      except PilConfigError as e:
         reply=QtWidgets.QMessageBox.critical(self.parent.ui,'Error',e.msg+': '+e.add_msg,QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Ok)
      if self.pildevice is not None:
         self.pildevice.setlocked(True)
         self.pildevice.setdevice(did,aid)
         self.pildevice.setlocked(False)
      self.toggle_controls()

   def do_pack(self):
      cls_lifpack.exec(self.filename)
      self.lifdir.refresh()

   def do_import(self):
      workdir=PILCONFIG.get('pyilper','workdir')
      cls_lifimport.exec(self.filename, workdir)
      self.lifdir.refresh()

   def do_label(self):
      oldlabel=self.lifdir.getLabel()
      cls_liflabel.exec(self.filename, oldlabel)
      self.lifdir.refresh()

   def do_dirlist(self):
#
#     get medium summary, return if blank or no medium
#
      mediumsummary= self.lifdir.getMediumSummary()
      linebreak= mediumsummary.find("Label")
      if linebreak == -1:
         return
      mediuminfo= mediumsummary[:linebreak]
      labelinfo=mediumsummary[linebreak:]
#
#     get output file name
#
      flist= cls_pdfprinter.get_pdfFilename()
      if flist is None:
         return
      output_filename= flist[0]
#
#     initialize pdf printer
#
      title="Directory listing of: "+self.filename
      pdfprinter=cls_pdfprinter(self.papersize,PDF_ORIENTATION_PORTRAIT, output_filename,title,True,1)
      pdfprinter.begin()

      model= self.lifdir.getModel()
      cols=6
      rows= self.lifdir.getRowCount()
      pdfprinter.print_item(cls_textItem(mediuminfo))
      pdfprinter.print_item(cls_textItem(labelinfo))
      pdfprinter.print_item(cls_textItem(self.lifdir.getDirSummary()))
      pdfprinter.print_item(cls_textItem("{:12} {:8} {:>6}/{:6} {:7} {:7}".format("Filename","Type","Size","Space","Date","Time")))
      for i in range (rows):
          line="{:12} {:8} {:>6}/{:6} {:7} {:7}".format(model.item(i,0).text().strip(), model.item(i,1).text().strip(), model.item(i,2).text().strip(), model.item(i,3).text().strip(), model.item(i,4).text(), model.item(i,5).text())
          pdfprinter.print_item(cls_textItem(line))
      pdfprinter.end()

#
#  Drive tab: refresh directory listing of medium
#
   def update_hdrive(self):
      if self.filename=="":
         return
      if self.pildevice is None:
         return
      tm=time.time()
      modified, timestamp= self.pildevice.ismodified()
      self.update_pending= self.update_pending or modified
      if self.update_pending:
         if tm - timestamp > NOT_TALKER_SPAN:
            self.refreshDirList()
            self.update_pending= False

   def refreshDirList(self):
      if self.filename=="":
         return
      self.pildevice.acquireaccesslock()
      self.lifdir.refresh()
      self.pildevice.releaseaccesslock()
#
#  enter lif filename
#
   def get_lifFilename(self):
      dialog=QtWidgets.QFileDialog()
      dialog.setWindowTitle("Select LIF Image File")
      dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
      dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
      dialog.setNameFilters( ["LIF Image File (*.dat *.DAT *.lif *.LIF)", "All Files (*)"] )
      dialog.setOptions(QtWidgets.QFileDialog.DontUseNativeDialog)
#     dialog.setDirectory(PILCONFIG.get('pyilper','workdir'))
      if dialog.exec():
         return dialog.selectedFiles() 
#
#  Check lif image file, returns status, tracks, surfaces, blocks 
#  If valid LIF1 medium and medium is compatible to device:
#     return True, tracks, surfaces, blocks of medium
#  else:
#     return False and default layout of device
#
   def lifMediumCheck(self,filename,quiet):
      defaultmedium= self.getDefaultMedium(self.drivetype)
      def_name, def_tracks, def_surfaces, def_blocks= self.mediainfo[defaultmedium]
      status, tracks, surfaces, blocks= self.getMediumInfo(filename)
      if status ==0: # medium info found
         return [True, tracks, surfaces, blocks]
      elif status==1: # file dos not exist or cannot be opened
            return [True, def_tracks, def_surfaces, def_blocks]
      elif status==2:
         if not quiet:
            reply=QtWidgets.QMessageBox.critical(self.parent.ui,'Error',"File does not contain a LIF type 1 medium.",QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Ok)
         return [False, def_tracks, def_surfaces, def_blocks]
      elif status==3:
         if not quiet:
            reply=QtWidgets.QMessageBox.warning(self.parent.ui,'Warning',"File does not contain a LIF type 1 medium with valid layout information. Using default layout of current drive type.",QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Ok)
         return [True, def_tracks, def_surfaces, def_blocks]
#
# get media info from lif header
#
   def getMediumInfo(self,filename):

#
#     read lif file header
#
      try:
         if isWINDOWS():
            fd= os.open(filename,os.O_RDONLY | os.O_BINARY)
         else:
            fd= os.open(filename,os.O_RDONLY)
      except OSError:
         return [1,0,0,0]   # file does not exist or cannot be opened
      try:
         b=os.read(fd,256)
         os.close(fd)
      except OSError:
         return [1,0,0,0]   # file read error
      if len(b) < 256:
         return [2,0,0,0]   # not lif type 1 file
#
#     do we have a LIF type 1 file
#
      lifmagic= getLifInt(b,0,2)
      dirstart=getLifInt(b,8,4)
#     if not(lifmagic == 0x8000 and dirstart == 2):
      if not(lifmagic == 0x8000):
         return [2,0,0,0] #  no lif type 1 file
#
#     get medium layout
#
      tracks= getLifInt(b,24,4)
      surfaces= getLifInt(b,28,4)
      blocks= getLifInt(b,32,4)
      if (tracks == surfaces) and (surfaces == blocks) :
         return [3,0,0,0] # no valid media layout information
      return [0, tracks, surfaces, blocks]


   def getDefaultMedium(self,device):
      if device== self.DEV_CASS:
         return self.MEDIUM_CASS
      if device== self.DEV_DISK:
         return self.MEDIUM_DISK
      if device== self.DEV_HDRIVE1:
         return self.MEDIUM_HDRIVE1
#
# LifDir Widget -----------------------------------------------------------
#
class TableModel(QtGui.QStandardItemModel):
    _sort_order = QtCore.Qt.AscendingOrder

    def sortOrder(self):
        return self._sort_order

    def sort(self, column, order):
         self._sort_order = order
         super().sort(column, order)

class DirTableView(QtWidgets.QTableView):

    def __init__(self,parent,papersize):
        super().__init__(parent)
        self.parent=parent
        self.papersize= papersize
#
#       context menu
#
    def contextMenuEvent(self, event):
        if self.parent.parent.active:
           event.accept()
           return
        if not self.parent.parent.parent.lifutils_installed:
           event.accept()
           return
        if self.selectionModel().selection().indexes():
            for i in self.selectionModel().selection().indexes():
                row, column = i.row(), i.column()
            model=self.parent.getModel()
            imagefile= self.parent.getFilename()
            liffilename=model.item(row,0).text()
            liffiletype=model.item(row,1).text()
            menu = QtWidgets.QMenu()
            exportAction = menu.addAction("Export")
            purgeAction = menu.addAction("Purge")
            renameAction = menu.addAction("Rename")
            ft=get_finfo_name(liffiletype)
#
#           view action
#
            viewAction= None
            if ft is not None:
               if get_finfo_type(ft)[1] != "":
                  viewAction= menu.addAction("View")
#
#           create barcode action
#
            barcodeAction= None
            if ft is not None:
               if ft== 0xE080 or ft== 0xE0D0:
                  barcodeAction= menu.addAction("Barcode")
            
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action is None:
               event.accept()
               return
            workdir=PILCONFIG.get('pyilper','workdir')
            charset=self.parent.parent.charset
            if action ==exportAction:
                cls_lifexport.exec(imagefile,liffilename,liffiletype,workdir)
            elif action== purgeAction:
                cls_lifpurge.exec(imagefile,liffilename)
                self.parent.refresh()
            elif action== renameAction:
                cls_lifrename.exec(imagefile,liffilename)
                self.parent.refresh()
            elif action== viewAction:
                cls_lifview.exec(imagefile, liffilename, liffiletype,workdir, charset)
            elif action== barcodeAction:
                cls_lifbarcode.exec(imagefile,liffilename,ft,self.papersize)
            event.accept()

class cls_LifDirWidget(QtWidgets.QWidget):

    def __init__(self,parent,rows,font_name,papersize):
        super().__init__(parent)
        self.parent=parent
        self.__papersize__=papersize
        self.__font_name__= font_name
        self.__font_size__= 13
        self.__table__ = DirTableView(self,self.__papersize__)  # Table view for dir
        self.__table__.setSortingEnabled(False)  # no sorting
        self.__table__.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#
#       switch off grid, no focus, no row selection
#
        self.__table__.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.__table__.setFocusPolicy(QtCore.Qt.NoFocus)
        self.__table__.setShowGrid(False)
        self.__columns__=6     # 5 rows for directory listing
        self.__rowcount__=0    # number of rows in table
        self.__filename__=""   # LIF filename
        self.__label__=""      # Label of lif file
        self.__model__ = TableModel(rows, self.__columns__, self.__table__)
#
#       populate header , set column size
#
        self.__model__.setHeaderData(0,QtCore.Qt.Horizontal,"File")
        self.__model__.setHeaderData(1,QtCore.Qt.Horizontal,"Type")
        self.__model__.setHeaderData(2,QtCore.Qt.Horizontal,"Size")
        self.__model__.setHeaderData(3,QtCore.Qt.Horizontal,"Space")
        self.__model__.setHeaderData(4,QtCore.Qt.Horizontal,"Date")
        self.__model__.setHeaderData(5,QtCore.Qt.Horizontal,"Time")
        self.__table__.setModel(self.__model__)
        self.__table__.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
#
#       handle click to header -> sorting
#
        self.__table__.horizontalHeader().sectionClicked.connect(
            self.handleSectionClicked)
#
#       no vertical header
#
        self.__table__.verticalHeader().setVisible(False)
        self.__table__.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
#
#       set font for directory listing, adjust row height
#
#       self.__font__= QtGui.QFont(self.__font_name__)
        self.__font__= QtGui.QFont()
#       self.__font__.setPixelSize(13)
#       metrics= QtGui.QFontMetrics(self.__font__)
#       self.__table__.verticalHeader().setDefaultSectionSize(metrics.height()+1)

#
#       add labels for text information (label, medium, directory)
#
        layout = QtWidgets.QVBoxLayout(self)
        self.__labelMedium__= QtWidgets.QLabel()
        self.__labelMedium__.setText("")
        layout.addWidget(self.__labelMedium__)
        self.__labelDir__= QtWidgets.QLabel()
        self.__labelDir__.setText("")
        layout.addWidget(self.__labelDir__)
        layout.addWidget(self.__table__)

        self.reconfigure()
#
#   reconfigure the font size of the directory list
#
    def reconfigure(self):
        self.__font_size__= PILCONFIG.get("pyilper","directorycharsize")
        self.__font__.setPixelSize(self.__font_size__)
        metrics= QtGui.QFontMetrics(self.__font__)
        self.__table__.verticalHeader().setDefaultSectionSize(metrics.height()+1)
        self.refresh()  

    def getModel(self):
        return(self.__model__)

    def getFilename(self):
        return(self.__filename__)

    def getLabel(self):
        return(self.__label__)

    def getRowCount(self):
        return(self.__rowcount__)

    def getMediumSummary(self):
        return(self.__labelMedium__.text())

    def getDirSummary(self):
        return(self.__labelDir__.text())
#
#   connect lif data file 
#
    def setFileName(self,filename):
        self.__filename__= filename
        self.refresh()

#
#   clear info
#
    def clear(self):
        self.__labelMedium__.setText("")
        self.__labelDir__.setText("")
        if self.__rowcount__==0:
           return
        self.__model__.removeRows(0, self.__rowcount__)
        self.__rowcount__=0
        return

#
#   read and display directory
#
    def refresh(self):
        if self.__filename__== "":
           return
        self.clear()
        try:
           lif=cls_LifFile()
           lif.set_filename(self.__filename__)
           lif.lifopen()
        except LifError:
           return
        lifdir= cls_LifDir(lif)
        lifdir.open()
        lifdir.rewind()
        dir_start, dir_length, no_tracks, no_surfaces, no_blocks, label, initdatetime=lif.getLifHeader()
        self.__label__= label
        totalblocks=no_tracks* no_surfaces* no_blocks
        totalbytes= totalblocks* 256
#
#       handle invalid values
#
        if no_tracks> 125 or no_surfaces>8 or no_blocks > 256 or \
           no_tracks==0   or no_surfaces==0 or no_blocks ==0:

           self.__labelMedium__.setText("Medium Layout: (invalid). Label: {:6s}, formatted: {:s}".format(label, initdatetime))
        else:
           self.__labelMedium__.setText("Medium Layout: ({}/{}/{}), Size: {} blocks ({} bytes). Label: {:6s}, formatted: {:s}".format(no_tracks,no_surfaces,no_blocks,totalblocks, totalbytes, label, initdatetime))
        self.__labelDir__.setText("Directory size: {} entries ({} used). Last block used: {}".format(dir_length*8, lifdir.num_entries, lifdir.lastblock))

#
#       populate directory listing
#
        while True:
            r= lifdir.getNextEntry()
            if r == []:
              break
            name, ftype_num, start_block, alloc_blocks, datetime, ftype, length= r
            x=[name,ftype ,"{:-8d}".format(length),"{:-8d}".format(alloc_blocks*256),datetime.split(sep=' ')[0],datetime.split(sep=' ')[1]]
            for column in range(self.__columns__):
                item = QtGui.QStandardItem(x[column])
                item.setFont(self.__font__)
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                self.__model__.setItem(self.__rowcount__, column, item)
            self.__rowcount__+=1
        lif.lifclose()
#
#       go to end of scroll area
#
        self.__table__.verticalScrollBar().setRange(0,10000)
        self.__table__.verticalScrollBar().setValue(10000)

#
#   handle click to header field and sort column
#
    def handleSectionClicked(self, index):
        if index >=4:  # not for date/time
           return
        if not self.__table__.isSortingEnabled():
           self.__table__.setSortingEnabled(True)
        self.__table__.sortByColumn(index,self.__model__.sortOrder())
        self.__table__.horizontalHeader().setSortIndicator(
                index, self.__table__.model().sortOrder())
        self.__table__.verticalScrollBar().setValue(0)
#
# HP-IL virtual disc class ---------------------------------------------------
#
# Initial release derived from ILPER 1.43 for Windows
#
# Changelog
#
# 09.02.2015 improvements and chages of ILPER 1.5 
# - renamed __fetat__ to __ilstate__ 
# - renamed __outdta__ to __outdata__ 
# - fixed increase of __ptout__ in __outdta__ (case 3: block)
# - delete zero __ptout__ in DDT section of do_cmd
# - inserte zero __ptout__ in SDA section of do_rdy
# - fixed __ilstate__ usage in do_cmd (LAD/SAD)
# 03.03.2015 windows i/o compatibility
# - rewritten: __rrec__, __wrec__, __format_disc__ to
# 11.03.2015 more improvements and changes of ILPER 1.5
# - fix first sector of LIF-Image
# - set pyhsical medium information, set id
# - not implemented: enable auto extended address switch
# 21.03.2015 more header fixes for HP-41
# 19.05.2015 getMediumInfo removed
# 30.05.2015 fixed error in handling AP, added getstatus
# 06.10.2015 jsi:
# - class statement syntax update
# 21.11.2015 jsi:
# - removed SSRQ/CSRQ approach
# 29.11.2015 jsi:
# - introduced talker activity timer
# - introduced device lock 
# 30.11.2015 jsi:
# - fixed idle timer mechanism
# - fixed header of HP82161 medium when formatted with an HP-71
# 02.12.2015 jsi:
# - fixed composition of the implementation byte array (4 byt int not byte!)
# - removed fix header of HP82161 medium when formatted with an HP-71 
# 19.02.2016 jsi
# - refactored and merged new Ildev base class of Christoph Giesselink
# - improved os detection
# 08.07.2016 jsi
# - refactoring: windows platform flag is constructor parameter now
#
# 19.09.2017 jsi
# - duplicate definition of getLifInt and putLifInt removed



class cls_pildrive(cls_pildevbase):

   def __init__(self, isWindows):
      super().__init__()

#
#     HP-IL data and variables
#
      self.__aid__ = 0x10         # accessory id = mass storage
      self.__defaddr__ = 2        # default address alter AAU
      self.__did__ = ""           # device id 
#
#     disk management variables
#
      self.__devl__ =0            # device listener
      self.__devt__ =0            # device talker
      self.__oc__ = 0             # byte pointer
      self.__pe__ = 0             # record pointer
      self.__pe0__=0
      self.__fpt__ = False        # flag pointer
      self.__flpwr__ = 0          # flag partial write
      self.__ptout__ = 0          # pointer out
      self.__modified__= False    # medium modification flag
      self.__tracks__= 0          # no of tracks of medium
      self.__surfaces__= 0        # no of surfaces of medium
      self.__blocks__= 0          # no of blocks of medium

      self.__lif__= bytearray(12) # device info
      self.__nbe__=0              # last record number
      self.__buf0__= bytearray(256) # buffer 0
      self.__buf1__= bytearray(256) # buffer 1
      self.__hdiscfile__= ""        # disc file
      self.__isactive__= False    # device active in loop
      self.__islocked__= False    # locked device
      self.__access_lock__= threading.Lock() 
      self.__timestamp__= time.time() # last time of beeing talker

      self.__isWindows__= isWindows # true, if Windows platform

#
# public ------------
#

#
#  was image modified since last timestamp
#
   def ismodified(self):
      self.__access_lock__.acquire()
      if self.__modified__:
        self.__modified__= False
        self.__access_lock__.release()
        return (True, self.__timestamp__)
      else:
        self.__access_lock__.release()
        return (False, self.__timestamp__)
#
#  lock device
#
   def acquireaccesslock(self):
      self.__access_lock__.acquire()

#
#  release device
#
   def releaseaccesslock(self):
      self.__access_lock__.release()


#
#  set new filename (disk change) and medium information
#
   def sethdisk(self,filename,tracks,surfaces,blocks):
      self.__hdiscfile__= filename
      self.__tracks__= tracks
      self.__surfaces__= surfaces
      self.__blocks__= blocks
      self.__nbe__= tracks*surfaces*blocks
      k=0
      for i in (24,16,8,0):
         self.__lif__[k]= tracks >> i & 0xFF
         k+=1
      for i in (24,16,8,0):
         self.__lif__[k]= surfaces >> i & 0xFF
         k+=1
      for i in (24,16,8,0):
         self.__lif__[k]= blocks >> i & 0xFF
         k+=1
      return
#
# set aid and did of device
#
   def setdevice(self,did,aid):
      self.__aid__= aid
      if did== "":
         self.__did__= ""
      else:
         self.__did__=did
      self.__clear_device__()
      return
#
# private
#
#
# copy buffer 0 to buffer 1
#
   def __copybuf__(self):
      self.__oc__=0
      for i in range (256):
         self.__buf1__[i]= self.__buf0__[i]
      return

#
# exchange buffers
#
   def __exchbuf__(self):
      self.__oc__=0
      for i in range (256):
         x=self.__buf1__[i]
         self.__buf1__[i]= self.__buf0__[i]
         self.__buf0__[i]= x
      return
# 
# read one sector n* pe (256 bytes) into buf0
#
   def __rrec__(self):
      self.__access_lock__.acquire()
      if self.__islocked__:
         self.__access_lock__.release()
         self.__status__= 20   # no medium error
         return
      try:
         if self.__isWindows__:
            fd= os.open(self.__hdiscfile__,os.O_RDONLY | os.O_BINARY)
         else:
            fd= os.open(self.__hdiscfile__,os.O_RDONLY)
         os.lseek(fd,self.__pe__ * 256, os.SEEK_SET)
         b=os.read(fd,256)
         os.close(fd)
         l=len(b)
#        print("rrec record %d size %d" % (self.__pe__,l))
         for i in range (l):
            self.__buf0__[i]= b[i]
         if l < 256:
            for i in range(l,256):
               self.__buf0__[i]=0x00
      except OSError as e:
         self.__status__= 20
      self.__access_lock__.release()
      return

#
# fix the header if record 0 (LIF header) is written
#
   def __fix_header__(self):
#
#     LIF Version 1 header?
#

      if self.__buf0__[0x00]== 0x80 and self.__buf0__[0x01]== 0x00:
         tracks= getLifInt(self.__buf0__,24,4)
         surfaces=getLifInt(self.__buf0__,28,4)
         blocks=getLifInt(self.__buf0__,32,4)
#
#        wrong media size information (HP firmware bug)?
#
         if(tracks == surfaces and surfaces == blocks):
            putLifInt(self.__buf0__,24,4,self.__tracks__)
            putLifInt(self.__buf0__,28,4,self.__surfaces__)
            putLifInt(self.__buf0__,32,4,self.__blocks__)
#
#       LIF Version 1 fix (for HP41 initialized images)
#
         if self.__buf0__[0x14]!= 0x00 or self.__buf0__[0x15]!= 0x01:
            self.__buf0__[0x14]= 0x00 
            self.__buf0__[0x15]= 0x01
#
#       Fix garbage in label field (for HP41 initialized images)
#
         if self.__buf0__[0x02] != 0x20 and (self.__buf0__[0x02] < 0x41 or self.__buf0__[0x02] > 0x5A):
            for i in range(6):
               self.__buf0__[i+0x02]=0x20

#
#       directory length fix
#
            if self.__buf0__[0x12] & 0x40 != 0:
               self.__buf0__[0x12] &= ~0x40
         
      return
#
# write buffer 0 to one sector n* pe (256 bytes)
#
   def __wrec__(self):
      self.__access_lock__.acquire()
      if self.__islocked__:
         self.__access_lock__.release()
         self.__status__= 20 # no medium error
         return
      try:
         if self.__isWindows__:
            fd= os.open(self.__hdiscfile__, os.O_WRONLY | os.O_BINARY)
         else:
            fd= os.open(self.__hdiscfile__, os.O_WRONLY)
         try:
            os.lseek(fd,self.__pe__ * 256, os.SEEK_SET)
            if self.__pe__ == 0:
               self.__fix_header__()
#           print("wrec record %d" % (self.__pe__))
            os.write(fd,self.__buf0__)
            self.__modified__= True
            self.__timestamp__= time.time()
         except OSError as e:
            self.__status__= 24
         os.close(fd)
      except OSError as e:
         self.__status__= 29
      self.__access_lock__.release()
      return

#
# "format" a lif image file
#
   def __format_disc__(self):
      b= bytearray(256)
      for i in range (0, len(b)):
               b[i]= 0xFF

      self.__access_lock__.acquire()
      if self.__islocked__:
         self.__access_lock__.release()
         self.__status__= 20 # no medium error
         return
      try:
         if self.__isWindows__:
            fd= os.open(self.__hdiscfile__, os.O_WRONLY | os.O_BINARY |  os.O_TRUNC | os.O_CREAT, 0o644)
         else:
            fd= os.open(self.__hdiscfile__, os.O_WRONLY | os.O_TRUNC | os.O_CREAT, 0o644)
         for i in range(0,127):
            os.write(fd,b)
         os.close(fd)
         self.__timestamp__= time.time()
      except OSError:
         self.__status__= 29
      self.__access_lock__.release()
      return
#
#  private (overloaded) -------------------------
#
#  clear drive reset internal pointers
#
   def __clear_device__ (self):
      self.__fpt__= False
      self.__pe__ = 0    
      self.__oc__ = 0   
      self.__access_lock__.acquire()
      self.__modified__= False
      self.__access_lock__.release()

#
# receive data to disc according to DDL command
#
   def __indata__(self,n):

      if (self.__devl__== 0) or (self.__devl__== 2) or (self.__devl__==6):
         self.__buf0__[self.__oc__]= n & 255
         self.__oc__+=1
         if self.__oc__ > 255:
            self.__oc__= 0
            self.__wrec__()
            self.__pe__+=1
            if self.__flpwr__ != 0:
               self.__rrec__()
         else:
           if ( n & 0x200) !=0:
              self.__wrec__()  # END
              if self.__flpwr__ == 0:
                 self.__pe__+=1

      elif self.__devl__ == 1:
         self.__buf1__[self.__oc__] = n & 255
         self.__oc__+=1
         if self.__oc__ > 255:
            self.__oc__ =0

      elif self.__devl__== 3:
         self.__oc__= n & 255

      elif self.__devl__ == 4:
         n= n & 255
         if self.__fpt__:
            self.__pe0__= self.__pe0__ & 0xFF00
            self.__pe0__= self.__pe0__ | n
            if self.__pe0__ < self.__nbe__:
               self.__pe__= self.__pe0__
               self.__status__= 0
            else:
               self.__status__= 28
            self.__fpt__= False
         else:
            self.__pe0__= self.__pe0__ & 255
            self.__pe0__= self.__pe0__ | (n <<8)
            self.__fpt__= True
      return
#
# send data from disc according to DDT command
#
   def __outdata__(self,frame):
      if frame== 0x560 :   # initial SDA
         self.__ptout__=0

      if (self.__devt__== 0) or (self.__devt__==2): # send buffer 0, read
         frame= self.__buf0__[self.__oc__]
         self.__oc__+=1
         if self.__oc__ > 255:
            self.__oc__=0
            self.__rrec__()
            self.__pe__+=1

      elif self.__devt__== 1: # send buffer 1
         frame= self.__buf1__[self.__oc__]
         self.__oc__+=1
         if self.__oc__ > 255:
            self.__oc__=0
            self.__devt__= 15  # send EOT on the next SDA

      elif self.__devt__ == 3:  # send position
         if self.__ptout__ == 0:
            frame= self.__pe__ >> 8
            self.__ptout__+=1
         elif self.__ptout__ == 1:
            frame= self.__pe__ & 255
            self.__ptout__+=1
         elif self.__ptout__ == 2:
            frame=  self.__oc__ & 255
            self.__ptout__+=1
         else:
            frame = 0x540 # EOT

      elif self.__devt__==6: # send implementation
         if self.__ptout__ < 12:
            frame= self.__lif__[self.__ptout__]
            self.__ptout__+=1
         else:
            frame= 0x540 # EOT

      elif self.__devt__ == 7:  # send max record
         if self.__ptout__ == 0:
            frame= self.__nbe__ >> 8
            self.__ptout__+=1
         elif self.__ptout__ == 1:
            frame= self.__nbe__ & 255
            self.__ptout__+=1
         else:
            frame = 0x540 # EOT

      else:
         frame= 0x540

      return (frame)

#
#  extended DDL/DDT commands
#
   def __cmd_ext__(self,frame):
      n= frame & 0xff
      t= n >> 5

      if t == 5: # DDL
         n=n & 31
         if (self.__ilstate__ & 0xC0) == 0x80: # are we listener?
            self.__devl__= n & 0xFF
            if n== 1:
               self.__flpwr__=0
            elif n== 2:
               self.__oc__= 0
               self.__flpwr__=0
            elif n==4:
               self.__flpwr__=0
               self.__fpt__= False
            elif n==5:
               self.__format_disc__()
            elif n == 6:
               self.__flpwr__= 0x80
               self.__rrec__()
            elif n == 7:
               self.__fpt__= False
               self.__pe__ = 0
               self.__oc__ = 0
            elif n == 8:
               self.__wrec__()
               if self.__flpwr__ ==0:
                  self.__pe__+=1
            elif n == 9:
               self.__copybuf__()
            elif n == 10:
                self.__exchbuf__()

      elif t == 6: # DDT
         n= n& 31
         if (self.__ilstate__ & 0x40) == 0x40:
            self.__devt__= n & 0xFF
            if n== 0:
               self.__flpwr__=0
            elif n == 2:
               self.__rrec__()
               self.__oc__=0
               self.__flpwr__=0
               self.__pe__+=1
            elif n == 4:
               self.__exchbuf__()
      return(frame)
