#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# pyILPER 
#
# Python platform dependent classes and constants
# Copyright (c) 2016 J. Siebold
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
# pyILPER support and constants  ---------------------------------------------------
#
# Changelog
# 08.07.16 - jsi:
# - initial release
# 25.07.2016 - jsi
# - set version to "production"
# 21.08.2016 - jsi
# - set version to 1.3.5 development
# 13.10.2016 - jsi
# - device tab constants and dictionary added
# 18.10.2016 - jsi
# - set version number to 1.4.0 development
# 23.10.2016 - jsi
# - EMU7470_VERSION added
# 25.10.2016 - jsi
# - decode_version moved from lifexec.py
# 26.10.2016 - jsi
# - version 1.4.0 beta1
# 04.11.2016 - jsi
# - version 1.4.0 beta2
# 01.01.2016 - jsi
# - version 1.4.0
# 07.01.2016 - jsi
# - add encode version function
# 03.01.2016 - jsi
# - version - 1.5.0beta1 development
# 16.03.2017 - jsi
# - version - 1.5.0 production
# 01.08.2017 - jsi
# - device HP82162A added
# 10.08.2017 jsi
# - version 1.6.0 development
# 11.08.2017 jsi
# - catch error in decode_version if no version information exists
# 18.08.2017 jsi
# - Tab name plotter renamed to HP7470A
# 21.08.2017 jsi
# - PDF and barcode constants added
# 31.08.2017 jsi
# - parameter TERMINAL_MINIMUM_ROWS added
# 03.09.2017 jsi
# - communication mode constants moved from pyilpermain.py
# 06.09.2017 jsi
# - restructured, assemble_frame and disassemble_frame added
# 07.09.2017 jsi
# - timeout constants for TCP, socket and pipe communication added
# 01.10.2017 jsi
# - 1.6.0 beta1
# 12.11.2017 jsi
# - 1.6.0 beta3
# 13.11.2017 jsi
# - make USE8BITS change depending on data returned by the PIL-Box
#
import platform
#
# Program constants --------------------------------------------------
#
# General constants:
#
PRODUCTION= False     # Production/Development Version
VERSION="1.6.0b3"       # pyILPR version number
CONFIG_VERSION="2"    # Version number of pyILPER config file, must be string
#
# Communication modes and classes
#
MODE_PILBOX=0         # connect to PIL-Box
MODE_TCPIP=1          # connect to virtual HP-IL over TCP/IP
MODE_SOCKET=2         # conect via Unix domain socket

#
# PIL-Box communication
#
USE8BITS= True        # use 8 bit data transfer to PIL-Box
TMOUTCMD=1            # time out for PIL-Box commands
TMOUTFRM=0.05         # time out for HP-IL frames

#
# TCP/IP, socket and pipe communication
#
COMTMOUTREAD=0.1      # time out for read
COMTMOUTACK=1         # time out for receiving an acknowledge
COMTMOUTWRITE=1       # tine out for write

#
# Drive tab - directory listing
#
REFRESH_RATE=1000     # period to check whether a drive was altered and is idle
NOT_TALKER_SPAN=3     # time (s) a drive must be inactive to be concidered as idle
#
# Terminal tab
#
UPDATE_TIMER=25                 # Poll timer (ms) for terminal output queue
CURSOR_BLINK=500                # 500 ms cursor blink rate
CURSOR_BLINK_INTERVAL= CURSOR_BLINK / UPDATE_TIMER


TERMINAL_MINIMUM_ROWS=24        # cant get beyond that

#
# predefined baudrates
# the list controlles the baudrates that are supported by the application:
# - the first list element sets the text in the combobox
# - the second list element is the baud rate, a value of 0 means auto baud detection
# the baudrates must be defined in ascending order
BAUDRATES= [ ["Auto", 0], ["9600", 9600 ] , [ "115200", 115200 ], ["230400", 230400]]

#
# plotter tab, required version of emu7470
#
EMU7470_VERSION=900

#
# if Development Version append string to VERSION and "d" to config file name
#
if not PRODUCTION:
   VERSION=VERSION+" (Development)"
   CONFIG_VERSION= CONFIG_VERSION+"d"
#
# Min, Max Values for font sizes. Note: MIN value means: automatic!!
#
MIN_TERMCHAR_SIZE=14
MAX_TERMCHAR_SIZE=20
MIN_DIRCHAR_SIZE=12
MAX_DIRCHAR_SIZE=18
#
# Tab types
#
TAB_SCOPE=0
TAB_PRINTER=1
TAB_DRIVE=2
TAB_TERMINAL=3
TAB_PLOTTER=4
TAB_HP82162A=5
#
TAB_NAMES={TAB_SCOPE:'Scope',TAB_PRINTER:'Printer',TAB_DRIVE:'Drive',TAB_TERMINAL:'Terminal',TAB_PLOTTER:'HP7470A',TAB_HP82162A:'HP82162A'}
#
# PDF Constants in 1/10 mm
#
PDF_MARGINS=100   
PDF_FORMAT_A4=0
PDF_FORMAT_LETTER=1
PDF_ORIENTATION_PORTRAIT=0
PDF_ORIENTATION_LANDSCAPE=1
#
# Barcode Constants in 1/10 mm
#
BARCODE_HEIGHT=100
BARCODE_NARROW_W= 5
BARCODE_WIDE_W= 10
BARCODE_SPACING= 5

#
# utility functions --------------------------------------------------------------
#
#  get platform
#
def isLINUX():
   return platform.system()=="Linux"
def isWINDOWS():
   return platform.system()=="Windows"
def isMACOS():
   return platform.system()=="Darwin"
#
# Standard FONT
#
if isLINUX():
   FONT="Monospace"
else:
   FONT="Courier New"
#
# decode version number of lifutils or emu7470
#
def decode_version(version_number):
   if version_number==0:
      return "(unknown)"
   version=str(version_number)
   major=int(version[0])
   minor=int(version[1:3])
   subversion=int(version[3:5])
   return "{:d}.{:d}.{:d}".format(major,minor,subversion)

def encode_version(version_string):
   v=version_string.split(".")
   major="".join(filter(lambda x: x.isdigit(),v[0]))
   minor="".join(filter(lambda x: x.isdigit(),v[1]))
   subversion="".join(filter(lambda x: x.isdigit(),v[2]))
   return int(major)*10000+ int(minor)*100 + int(subversion)
#
#  assemble frame from low and high byte according to 7- oder 8-bit format
#
def assemble_frame(hbyt,lbyt):
   global USE8BITS
   if( lbyt & 0x80 ):
      USE8BITS= True
      return ((hbyt & 0x1E) << 6) + (lbyt & 0x7F)
   else:
      USE8BITS= False
      return ((hbyt & 0x1F) << 6) + (lbyt & 0x3F)
#
#  disassemble frame from low and high byte according to 7- oder 8-bit format
#

def disassemble_frame(frame):
    if not USE8BITS :
       hbyt = ((frame >> 6) & 0x1F) | 0x20
       lbyt = (frame & 0x3F) | 0x40
    else:
       hbyt = ((frame >> 6) & 0x1E) | 0x20
       lbyt = (frame & 0x7F) | 0x80
    return(hbyt,lbyt)

