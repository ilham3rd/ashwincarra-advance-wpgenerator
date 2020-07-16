import csv
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
import numpy as np
import json
import math


class Mission1Form(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.Mission1Type='B'
        self.setLogo()
        self.setForm()
    

    def GenerateWP(self):
  
        if(self.Mission1Type=='A'):
            self.basicWPMission1TipeA()
        if(self.Mission1Type=='B'):
            self.basicWPMission1TipeB()
        self.view.reload()
    
    
    def optionMission(self,b):
        if b.text()=="Tipe A":
            self.Mission1Type='A'
            # self.clearLayout()
            self.setMission1LayoutTipeA()
            print("Set Mission 1 Type A")
        if b.text()=="Tipe B":
            self.Mission1Type='B'
            self.clearLayout()
            self.setMission1LayoutTipeB()
            print("Set Mission 1 Type B")

    
    def setMission1LayoutTipeA(self):
        self.VMenuLayout.addLayout(self.HMissionLayout)
        self.VMenuLayout.addLayout(self.HAltitude)
        self.VMenuLayout.addLayout(self.HChangeSpeed1)
        self.VMenuLayout.addLayout(self.HChangeSpeed2)
        self.VMenuLayout.addLayout(self.HLatitudeHome)
        self.VMenuLayout.addLayout(self.HLongitudeHome)
        self.VMenuLayout.addLayout(self.HLatitudeRight)
        self.VMenuLayout.addLayout(self.HLongitudeRight)
        self.VMenuLayout.addLayout(self.HLatitudeWidth)
        self.VMenuLayout.addLayout(self.HLongitudeWidth)
        self.VMenuLayout.addLayout(self.HLatitudeCircle)
        self.VMenuLayout.addLayout(self.HLongitudeCircle)
        self.VMenuLayout.addLayout(self.HRadius)
        self.VMenuLayout.addWidget(self.generateButton)
        self.VMenuLayout.addWidget(self.logo)



    def setLogo(self):
        self.logo=QLabel()
        img_logo=QPixmap()
        img_logo.load("Ashwincarra.png")
        self.logo.setPixmap(img_logo.scaledToWidth(300))
    
    def setForm(self):
        self.wpHomeLatLong=[0,0]
        self.wpBawahKananLatLong=[0,0]
        self.wpBawahKiriLatLong=[0,0]
        self.wpAtasKananLatLong=[0,0]
        self.wpAtasKiriLatLong=[0,0]
        self.wpSplineKanan=[0,0]
        self.wpSplineKiri=[0,0]
        self.wpCenterBawah=[0,0]
        self.wpCenterKiri=[0,0]
        self.wpCenterAtas=[0,0]
        self.wpCenterKanan=[0,0]

        self.generateButton=QPushButton("Generate Waypoint")
        self.generateButton.clicked.connect(self.GenerateWP)

        self.generateMission1=QRadioButton("Tipe A")
        self.generateMission2=QRadioButton("Tipe B")
        self.generateMission1.toggled.connect(lambda:self.optionMission(self.generateMission1))
        self.generateMission2.toggled.connect(lambda:self.optionMission(self.generateMission2))
        
        self.HMissionLayout=QHBoxLayout()
        self.HMissionLayout.addWidget(self.generateMission1)
        self.HMissionLayout.addWidget(self.generateMission2)

        self.HLatitudeHome=QHBoxLayout()
        self.HLatitudeHomeText=QLabel("Latitude Home")
        self.HLatitudeHomeLine=QLineEdit()
        self.HLatitudeHome.addWidget(self.HLatitudeHomeText,1)
        self.HLatitudeHome.addWidget(self.HLatitudeHomeLine,1)

        self.HLongitudeHome=QHBoxLayout()
        self.HLongitudeHomeText=QLabel("Longitude Home")
        self.HLongitudeHomeLine=QLineEdit()
        self.HLongitudeHome.addWidget(self.HLongitudeHomeText,1)
        self.HLongitudeHome.addWidget(self.HLongitudeHomeLine,1)

        self.HLatitudeRight=QHBoxLayout()
        self.HLatitudeRightText=QLabel("Latitude Right")
        self.HLatitudeRightLine=QLineEdit()
        self.HLatitudeRight.addWidget(self.HLatitudeRightText,1)
        self.HLatitudeRight.addWidget(self.HLatitudeRightLine,1)

        self.HLongitudeRight=QHBoxLayout()
        self.HLongitudeRightText=QLabel("Longitude Right")
        self.HLongitudeRightLine=QLineEdit()
        self.HLongitudeRight.addWidget(self.HLongitudeRightText,1)
        self.HLongitudeRight.addWidget(self.HLongitudeRightLine,1)

        self.HLongitudeWidth=QHBoxLayout()
        self.HLongitudeWidthText=QLabel("Longitude Width")
        self.HLongitudeWidthLine=QLineEdit()
        self.HLongitudeWidth.addWidget(self.HLongitudeWidthText,1)
        self.HLongitudeWidth.addWidget(self.HLongitudeWidthLine,1)

        self.HLatitudeWidth=QHBoxLayout()
        self.HLatitudeWidthText=QLabel("Latitude Width")
        self.HLatitudeWidthLine=QLineEdit()
        self.HLatitudeWidth.addWidget(self.HLatitudeWidthText,1)
        self.HLatitudeWidth.addWidget(self.HLatitudeWidthLine,1)

        self.HLongitudeCircle=QHBoxLayout()
        self.HLongitudeCircleText=QLabel("Longitude Circle")
        self.HLongitudeCircleLine=QLineEdit()
        self.HLongitudeCircle.addWidget(self.HLongitudeCircleText,1)
        self.HLongitudeCircle.addWidget(self.HLongitudeCircleLine,1)


        self.HLatitudeCircle=QHBoxLayout()
        self.HLatitudeCircleText=QLabel("Latitude Circle")
        self.HLatitudeCircleLine=QLineEdit()
        self.HLatitudeCircle.addWidget(self.HLatitudeCircleText,1)
        self.HLatitudeCircle.addWidget(self.HLatitudeCircleLine,1)

        self.HAltitude=QHBoxLayout()
        self.HChangeSpeed1=QHBoxLayout()
        self.HChangeSpeed2=QHBoxLayout()
        self.Altitude=QLineEdit()

        self.textAltitude=QLabel("Altitude (m)")
        self.HAltitude.addWidget(self.textAltitude,1) 
        self.HAltitude.addWidget(self.Altitude,1)

        self.textChangeSpeed1=QLabel("Speed Translasi (m/s)")
        self.ChangeSpeed1=QLineEdit()
        self.HChangeSpeed1.addWidget(self.textChangeSpeed1,1)
        self.HChangeSpeed1.addWidget(self.ChangeSpeed1,1)


        self.textChangeSpeed2=QLabel("Speed Scanning (m/s)")
        self.ChangeSpeed2=QLineEdit()
        self.HChangeSpeed2.addWidget(self.textChangeSpeed2,1)
        self.HChangeSpeed2.addWidget(self.ChangeSpeed2,1)

        self.radiusText=QLabel("Spline Radius (m)")
        self.radius=QLineEdit()
        self.home_rotasi=QLineEdit()
        self.HRadius=QHBoxLayout()
        self.HRadius.addWidget(self.radiusText,1)
        self.HRadius.addWidget(self.radius,1)

        
        self.HLayout=QHBoxLayout()
        self.VMenuLayout=QVBoxLayout()
        self.HLayout.addWidget(self.setMaps())
        self.HMenu=QWidget()
        self.HMenu.setMaximumWidth(320)
        self.HMenu.setLayout(self.VMenuLayout)
        self.HLayout.addWidget(self.HMenu)


        self.setMission1LayoutTipeA()
        self.setLayout(self.HLayout)

    def setMaps(self):
        self.view =QWebEngineView()
        self.view.load(QUrl.fromLocalFile(os.path.abspath('index.html')))
        return self.view

    def basicWPMission1TipeA(self):
        self.wpAltitude=float(self.Altitude.text())
        self.wpSpeedTrans=float(self.ChangeSpeed1.text())
        self.wpSpeedScan=float(self.ChangeSpeed2.text())
        self.wpHomeLat=float(self.HLatitudeHomeLine.text())
        self.wpHomeLon=float(self.HLongitudeHomeLine.text())
        self.wpRightLat=float(self.HLatitudeRightLine.text())
        self.wpRightLon=float(self.HLongitudeRightLine.text())
        self.wpWidthLat=float(self.HLatitudeWidthLine.text())
        self.wpWidthLon=float(self.HLongitudeWidthLine.text())
        self.wpCircleLon=float(self.HLongitudeCircleLine.text())
        self.wpCircleLat=float(self.HLatitudeCircleLine.text())
        self.consLatitudeLongitude=0.0000089831
        self.wpRadius=float(self.radius.text())*self.consLatitudeLongitude
        self.wpHomeLatLong[0]=self.wpHomeLon
        self.wpHomeLatLong[1]=self.wpHomeLat
        self.wpBawahKananLatLong[0]=self.wpRightLon
        self.wpBawahKananLatLong[1]=self.wpRightLat
        self.wpBawahKiriLatLong[0]=2*self.wpHomeLon-self.wpRightLon
        self.wpBawahKiriLatLong[1]=2*self.wpHomeLat-self.wpRightLat
        self.rumusAtas=self.wpWidthLat-self.wpRightLat-(self.wpWidthLon*((self.wpRightLat-self.wpHomeLat)/(self.wpRightLon-self.wpHomeLon)))+(self.wpRightLon*((self.wpHomeLon-self.wpRightLon)/(self.wpRightLat-self.wpHomeLat)))
        self.rumusBawah=((self.wpHomeLon-self.wpRightLon)/(self.wpRightLat-self.wpHomeLat))-((self.wpRightLat-self.wpHomeLat)/(self.wpRightLon-self.wpHomeLon))
        self.wpAtasKananLatLong[0]=self.rumusAtas/self.rumusBawah
        self.wpAtasKananLatLong[1]=((self.wpRightLat-self.wpHomeLat)/(self.wpRightLon-self.wpHomeLon))*(self.wpAtasKananLatLong[0]-self.wpWidthLon)+self.wpWidthLat

        self.wpAtasKiriLatLong[0]=self.wpAtasKananLatLong[0]+(self.wpBawahKiriLatLong[0]-self.wpBawahKananLatLong[0])
        self.wpAtasKiriLatLong[1]=self.wpAtasKananLatLong[1]+(self.wpBawahKiriLatLong[1]-self.wpBawahKananLatLong[1])
        self.gradientSplineKanan=(self.wpAtasKananLatLong[0]-self.wpBawahKananLatLong[0])/(self.wpBawahKananLatLong[1]-self.wpAtasKananLatLong[1])
        self.gradientSplineKiri=(self.wpAtasKiriLatLong[0]-self.wpBawahKiriLatLong[0])/(self.wpBawahKiriLatLong[1]-self.wpAtasKiriLatLong[1])
        if(self.wpAtasKananLatLong[0]>self.wpAtasKiriLatLong[0]):
            self.wpSplineKiri[0]=((((self.wpAtasKiriLatLong[0]+self.wpBawahKiriLatLong[0])/2)*math.sqrt(self.gradientSplineKiri**2+1))-self.wpRadius)/(math.sqrt(self.gradientSplineKiri**2+1))
            self.wpSplineKiri[1]=self.gradientSplineKiri*(self.wpSplineKiri[0]-((self.wpAtasKiriLatLong[0]+self.wpBawahKiriLatLong[0])/2))+((self.wpAtasKiriLatLong[1]+self.wpBawahKiriLatLong[1])/2)

            self.wpSplineKanan[0]=((((self.wpAtasKananLatLong[0]+self.wpBawahKananLatLong[0])/2)*math.sqrt(self.gradientSplineKanan**2+1))+self.wpRadius)/(math.sqrt(self.gradientSplineKanan**2+1))
            self.wpSplineKanan[1]=self.gradientSplineKanan*(self.wpSplineKanan[0]-((self.wpAtasKananLatLong[0]+self.wpBawahKananLatLong[0])/2))+((self.wpAtasKananLatLong[1]+self.wpBawahKananLatLong[1])/2)
        elif(self.wpAtasKananLatLong[0]<self.wpAtasKiriLatLong[0]):

            self.wpSplineKiri[0]=((((self.wpAtasKiriLatLong[0]+self.wpBawahKiriLatLong[0])/2)*math.sqrt(self.gradientSplineKiri**2+1))+self.wpRadius)/(math.sqrt(self.gradientSplineKiri**2+1))
            self.wpSplineKiri[1]=self.gradientSplineKiri*(self.wpSplineKiri[0]-((self.wpAtasKiriLatLong[0]+self.wpBawahKiriLatLong[0])/2))+((self.wpAtasKiriLatLong[1]+self.wpBawahKiriLatLong[1])/2)

            self.wpSplineKanan[0]=((((self.wpAtasKananLatLong[0]+self.wpBawahKananLatLong[0])/2)*math.sqrt(self.gradientSplineKanan**2+1))-self.wpRadius)/(math.sqrt(self.gradientSplineKanan**2+1))
            self.wpSplineKanan[1]=self.gradientSplineKanan*(self.wpSplineKanan[0]-((self.wpAtasKananLatLong[0]+self.wpBawahKananLatLong[0])/2))+((self.wpAtasKananLatLong[1]+self.wpBawahKananLatLong[1])/2)
            
        #Index 0 = Longitude, Index 1 = Latitude
        #Latitude = Y, Longitude = X
        self.gradientSplineKanan=self.wpAtasKananLatLong[0]-self.wpBawahKananLatLong[0]
        self.wpLength=math.sqrt(((self.wpHomeLat-self.wpRightLat)**2)+((self.wpHomeLon-self.wpRightLon)**2))/self.consLatitudeLongitude
        self.gradientM1=(self.wpAtasKananLatLong[1]-self.wpAtasKiriLatLong[1])/(self.wpAtasKananLatLong[0]-self.wpAtasKiriLatLong[0])
        self.gradientM2=(self.wpAtasKiriLatLong[0]-self.wpAtasKananLatLong[0])/(self.wpAtasKananLatLong[1]-self.wpAtasKiriLatLong[1])
        self.wpCenterBawah[0]=(self.gradientM1*self.wpAtasKiriLatLong[0]-self.gradientM2*self.wpCircleLon+self.wpCircleLat-self.wpAtasKiriLatLong[1])/(self.gradientM1-self.gradientM2)
        self.wpCenterBawah[1]=self.gradientM2*(self.wpCenterBawah[0]-self.wpCircleLon)+self.wpCircleLat
        self.radiusCircle=math.sqrt((self.wpCenterBawah[0]-self.wpCircleLon)**2+(self.wpCenterBawah[1]-self.wpCircleLat)**2)
        self.wpCenterAtas[0]=(-self.radiusCircle+self.wpCircleLon*(math.sqrt(self.gradientM2**2+1)))/(math.sqrt(self.gradientM2**2+1))
        self.wpCenterAtas[1]=self.gradientM2*(self.wpCenterAtas[0]-self.wpCircleLon)+self.wpCircleLat
        
        if(self.wpBawahKiriLatLong[0]>self.wpBawahKananLatLong[0]):
            self.wpCenterKiri[0]=(self.radiusCircle+self.wpCircleLon*(math.sqrt(self.gradientM1**2+1)))/(math.sqrt(self.gradientM1**2+1))
            self.wpCenterKiri[1]=self.gradientM1*(self.wpCenterKiri[0]-self.wpCircleLon)+self.wpCircleLat
            self.wpCenterKanan[0]=(-self.radiusCircle+self.wpCircleLon*(math.sqrt(self.gradientM1**2+1)))/(math.sqrt(self.gradientM1**2+1))
            self.wpCenterKanan[1]=self.gradientM1*(self.wpCenterKiri[0]-self.wpCircleLon)+self.wpCircleLat
        
        
        elif(self.wpBawahKiriLatLong[0]<self.wpBawahKananLatLong[0]):
            self.wpCenterKiri[0]=(-self.radiusCircle+self.wpCircleLon*(math.sqrt(self.gradientM1**2+1)))/(math.sqrt(self.gradientM1**2+1))
            self.wpCenterKiri[1]=self.gradientM1*(self.wpCenterKiri[0]-self.wpCircleLon)+self.wpCircleLat
            self.wpCenterKanan[0]=(self.radiusCircle+self.wpCircleLon*(math.sqrt(self.gradientM1**2+1)))/(math.sqrt(self.gradientM1**2+1))
            self.wpCenterKanan[1]=self.gradientM1*(self.wpCenterKiri[0]-self.wpCircleLon)+self.wpCircleLat
        

        
        with open('datawp_dump.csv','w',newline='')as file:
            fieldname=['11','Aerial']
            writer =csv.DictWriter(file,fieldnames=fieldname)
            writer.writeheader()
            writer.writerow({'11': self.wpHomeLatLong[0],'Aerial':self.wpHomeLatLong[1]})
            writer.writerow({'11': self.wpBawahKananLatLong[0],'Aerial':self.wpBawahKananLatLong[1]})
            writer.writerow({'11': self.wpBawahKiriLatLong[0],'Aerial':self.wpBawahKiriLatLong[1]})
            writer.writerow({'11': self.wpAtasKananLatLong[0],'Aerial':self.wpAtasKananLatLong[1]})
            writer.writerow({'11': self.wpAtasKiriLatLong[0],'Aerial':self.wpAtasKiriLatLong[1]})
            writer.writerow({'11': self.wpSplineKanan[0],'Aerial':self.wpSplineKanan[1]})
            writer.writerow({'11': self.wpSplineKiri[0],'Aerial':self.wpSplineKiri[1]})
            writer.writerow({'11': self.wpCenterBawah[0],'Aerial':self.wpCenterBawah[1]})
            writer.writerow({'11': self.wpCenterAtas[0],'Aerial':self.wpCenterAtas[1]})
            writer.writerow({'11': self.wpCenterKiri[0],'Aerial':self.wpCenterKiri[1]})
            writer.writerow({'11': self.wpCenterKanan[0],'Aerial':self.wpCenterKanan[1]})
            print(self.wpCenterBawah[0])
            print(self.wpCenterBawah[1])
        



        
    

class Mission2Form(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.Mission2Type='B'
        self.setLogo()
        self.setForm()
    
    def setMission2LayoutTipeB(self):
        self.logo.show()
        self.widthText.show()
        self.widthSlider.show()
        self.lengthText.show()
        self.lenghtSlider.show()
        self.generateButton.show()
        self.home_latitude.show()
        self.textLatitude.show()
        self.home_longitude.show()
        self.textLongitude.show()
        self.radiusText.show()
        self.radius.show()
        self.home_rotasi.show()
        self.textRotasi.show()


        self.VMenuLayout.addLayout(self.HMissionLayout,1)
        self.VMenuLayout.addLayout(self.HAltitude,1)
        self.VMenuLayout.addLayout(self.HChangeSpeed1,1)
        self.VMenuLayout.addLayout(self.HChangeSpeed2,1)
        self.VMenuLayout.addLayout(self.HTranslasi1,1)
        self.VMenuLayout.addLayout(self.HTranslasi2,1)
        self.VMenuLayout.addLayout(self.HRadius,1)
        self.VMenuLayout.addLayout(self.HRotasi,1)
        self.VMenuLayout.addWidget(self.widthText)
        self.VMenuLayout.addWidget(self.widthSlider)
        self.VMenuLayout.addWidget(self.lengthText)
        self.VMenuLayout.addWidget(self.lenghtSlider)
        self.VMenuLayout.addWidget( self.generateButton,1)
        # self.VMenuLayout.addWidget(self.setRotasi)
        self.VMenuLayout.addWidget(self.logo,1)
    
    def setMission2LayoutTipeA(self):
        self.radiusText.show()
        self.radius.show()
        self.logo.show()
        self.generateButton.show()
        self.HLatitudeHomeLine.show()
        self.HLatitudeHomeText.show()
        self.HLongitudeHomeLine.show()
        self.HLongitudeHomeText.show()
        self.HLatitudeRightLine.show()
        self.HLatitudeRightText.show()
        self.HLongitudeRightLine.show()
        self.HLongitudeRightText.show()
        self.HLatitudeTakeLine.show()
        self.HLatitudeTakeText.show()
        self.HLongitudeTakeLine.show()
        self.HLongitudeTakeText.show()
        
        
        self.VMenuLayout.addLayout(self.HMissionLayout,1)
        self.VMenuLayout.addLayout(self.HAltitude,1)
        self.VMenuLayout.addLayout(self.HChangeSpeed1,1)
        self.VMenuLayout.addLayout(self.HChangeSpeed2,1)
        self.VMenuLayout.addLayout(self.HLatitudeHome,1)
        self.VMenuLayout.addLayout(self.HLongitudeHome,1)
        self.VMenuLayout.addLayout(self.HLatitudeRight,1)
        self.VMenuLayout.addLayout(self.HLongitudeRight,1)
        self.VMenuLayout.addLayout(self.HLatitudeTake,1)
        self.VMenuLayout.addLayout(self.HLongitudeTake,1)
        self.VMenuLayout.addLayout(self.HRadius,1)
        self.VMenuLayout.addWidget(self.generateButton,1)
        self.VMenuLayout.addWidget(self.logo,1)
        
    
    def clearLayout(self):
        self.HMissionLayout.setParent(None)
        self.HAltitude.setParent(None)
        self.HChangeSpeed1.setParent(None)
        self.HChangeSpeed2.setParent(None)
        self.HTranslasi1.setParent(None)
        self.HTranslasi2.setParent(None)
        self.HRadius.setParent(None)
        self.widthText.setParent(None)
        self.widthSlider.setParent(None)
        self.lenghtSlider.setParent(None)
        self.lengthText.setParent(None)
        self.lenghtSlider.setParent(None)
        self.generateButton.setParent(None)
        self.logo.setParent(None)
        self.HRotasi.setParent(None)
        self.logo.hide()
        self.widthText.hide()
        self.widthSlider.hide()
        self.lengthText.hide()
        self.lenghtSlider.hide()
        self.generateButton.hide()
        self.textLatitude.hide()
        self.home_latitude.hide()
        self.textLongitude.hide()
        self.home_longitude.hide()
        self.radiusText.hide()
        self.radius.hide()
        self.home_rotasi.hide()
        self.textRotasi.hide()
        self.HLatitudeHomeLine.hide()
        self.HLatitudeHome.setParent(None)
        self.HLatitudeHomeText.hide()
        self.HLongitudeHomeLine.hide()
        self.HLongitudeHomeText.hide()
        self.HLongitudeHome.setParent(None)

        self.HLatitudeRightLine.hide()
        self.HLatitudeRight.setParent(None)
        self.HLatitudeRightText.hide()
        self.HLongitudeRightLine.hide()
        self.HLongitudeRightText.hide()
        self.HLongitudeRight.setParent(None)

        self.HLatitudeTakeLine.hide()
        self.HLatitudeTake.setParent(None)
        self.HLatitudeTakeText.hide()
        self.HLongitudeTakeLine.hide()
        self.HLongitudeTakeText.hide()
        self.HLongitudeTake.setParent(None)

    def setForm(self):
        self.wpHomeLatLong=[0,0]
        self.wpBawahKananLatLong=[0,0]
        self.wpBawahKiriLatLong=[0,0]
        self.wpAtasKananLatLong=[0,0]
        self.wpAtasKiriLatLong=[0,0]
        self.wpSplineKanan=[0,0]
        self.wpSplineKiri=[0,0]
        self.wpPickLatLong=[0,0]
        self.wpPojokLatLong=[0,0]
        self.wpTakeLatLong=[0,0]
        

        self.HLatitudeHome=QHBoxLayout()
        self.HLatitudeHomeText=QLabel("Latitude Home")
        self.HLatitudeHomeLine=QLineEdit()
        self.HLatitudeHome.addWidget(self.HLatitudeHomeText,1)
        self.HLatitudeHome.addWidget(self.HLatitudeHomeLine,1)

        self.HLongitudeHome=QHBoxLayout()
        self.HLongitudeHomeText=QLabel("Longitude Home")
        self.HLongitudeHomeLine=QLineEdit()
        self.HLongitudeHome.addWidget(self.HLongitudeHomeText,1)
        self.HLongitudeHome.addWidget(self.HLongitudeHomeLine,1)

        self.HLatitudeRight=QHBoxLayout()
        self.HLatitudeRightText=QLabel("Latitude Right")
        self.HLatitudeRightLine=QLineEdit()
        self.HLatitudeRight.addWidget(self.HLatitudeRightText,1)
        self.HLatitudeRight.addWidget(self.HLatitudeRightLine,1)

        self.HLongitudeRight=QHBoxLayout()
        self.HLongitudeRightText=QLabel("Longitude Right")
        self.HLongitudeRightLine=QLineEdit()
        self.HLongitudeRight.addWidget(self.HLongitudeRightText,1)
        self.HLongitudeRight.addWidget(self.HLongitudeRightLine,1)
       

        self.HLatitudeTake=QHBoxLayout()
        self.HLatitudeTakeText=QLabel("Latitude Take Water")
        self.HLatitudeTakeLine=QLineEdit()
        self.HLatitudeTake.addWidget(self.HLatitudeTakeText,1)
        self.HLatitudeTake.addWidget(self.HLatitudeTakeLine,1)

        self.HLongitudeTake=QHBoxLayout()
        self.HLongitudeTakeText=QLabel("Longitude Take Water")
        self.HLongitudeTakeLine=QLineEdit()
        self.HLongitudeTake.addWidget(self.HLongitudeTakeText,1)
        self.HLongitudeTake.addWidget(self.HLongitudeTakeLine,1)
       
        self.HLayout=QHBoxLayout()
        self.VMenuLayout=QVBoxLayout()
        self.HMissionLayout=QHBoxLayout()
        self.HLayout.addWidget(self.setMaps())
        self.HMenu=QWidget()
        self.HMenu.setMaximumWidth(320)
        # self.VMenuLayout.addWidget(self.setLogo(),1)
        self.HMenu.setLayout(self.VMenuLayout)
        self.HLayout.addWidget(self.HMenu)
        self.setLayout(self.HLayout)
        
        
        #Radio Button
        self.generateMission1=QRadioButton("Tipe A")
        self.generateMission2=QRadioButton("Tipe B")
        self.generateMission1.toggled.connect(lambda:self.optionMission(self.generateMission1))
        self.generateMission2.toggled.connect(lambda:self.optionMission(self.generateMission2))
        
        self.HMissionLayout.addWidget(self.generateMission1)
        self.HMissionLayout.addWidget(self.generateMission2)



        #Set Button

        self.HAltitude=QHBoxLayout()
        self.HChangeSpeed1=QHBoxLayout()
        self.HChangeSpeed2=QHBoxLayout()
        self.Altitude=QLineEdit()

        self.textAltitude=QLabel("Altitude (m)")
        self.HAltitude.addWidget(self.textAltitude,1) 
        self.HAltitude.addWidget(self.Altitude,1)

        self.textChangeSpeed1=QLabel("Speed Translasi (m/s)")
        self.ChangeSpeed1=QLineEdit()
        self.HChangeSpeed1.addWidget(self.textChangeSpeed1,1)
        self.HChangeSpeed1.addWidget(self.ChangeSpeed1,1)


        self.textChangeSpeed2=QLabel("Speed Scanning (m/s)")
        self.ChangeSpeed2=QLineEdit()
        self.HChangeSpeed2.addWidget(self.textChangeSpeed2,1)
        self.HChangeSpeed2.addWidget(self.ChangeSpeed2,1)





        self.lenghtSlider=QSlider(Qt.Horizontal)
        self.widthSlider=QSlider(Qt.Horizontal)
        self.widthSlider.setValue(5)
        self.HButton=QHBoxLayout()
        
        self.readButton=QPushButton("Read File")
        self.readButton.clicked.connect(self.readWP)
        self.writeButton=QPushButton("Write File")
        self.writeButton.clicked.connect(self.writeWP)
        self.HButton.addWidget(self.readButton)
        self.HButton.addWidget(self.writeButton)
        self.widthText=QLabel("Lebar Path : 5m")
        self.widthSlider.setMinimum(5)
        self.widthSlider.setMaximum(50)
        self.lenghtSlider.setMinimum(5)
        self.lenghtSlider.setMaximum(130)
        self.lenghtSlider.valueChanged.connect(self.setPanjang)
        self.widthSlider.valueChanged.connect(self.setLebar)
        self.lengthText=QLabel("Panjang Path : 5m")
        self.generateButton=QPushButton("Generate Waypoint")
        self.generateButton.clicked.connect(self.GenerateWP)

        # self.VMenuLayout.addLayout(self.HButton)
        

        self.home_latitude=QLineEdit()
        self.home_longitude=QLineEdit()
        self.setHome=QPushButton("Set Home")
        self.setHome.clicked.connect(self.setHomeFun)
        self.setHome.setDisabled(True)
        self.HTranslasi1=QHBoxLayout()
        self.HTranslasi2=QHBoxLayout()
        self.textLongitude=QLabel("Longitude")
        self.textLatitude=QLabel("Latitude")
        self.HTranslasi1.addWidget(self.textLongitude,1)
        self.HTranslasi1.addWidget(self.home_longitude,1)
        self.HTranslasi2.addWidget(self.textLatitude,1)
        self.HTranslasi2.addWidget(self.home_latitude,1)



        self.radiusText=QLabel("Spline Radius (m)")
        self.radius=QLineEdit()
        self.home_rotasi=QLineEdit()
        self.HRadius=QHBoxLayout()
        self.HRadius.addWidget(self.radiusText,1)
        self.HRadius.addWidget(self.radius,1)
        self.textRotasi=QLabel("Rotasi")
        self.setRotasi=QPushButton("Set Rotasi")
        self.setRotasi.clicked.connect(self.setRotasiFun)
        self.setRotasi.setDisabled(True)
        self.HRotasi=QHBoxLayout()
        self.HRotasi.addWidget(self.textRotasi,1)
        self.HRotasi.addWidget(self.home_rotasi,1)        
        self.setMission2LayoutTipeB()

    def GenerateWP(self):
  
        if(self.Mission2Type=='A'):
            self.basicWPMission2TipeA()
        if(self.Mission2Type=='B'):
            self.basicWPMission2TipeB()
        self.view.reload()
    
    def basicWPMission2TipeA(self):
        self.wpAltitude=float(self.Altitude.text())
        self.wpSpeedTrans=float(self.ChangeSpeed1.text())
        self.wpSpeedScan=float(self.ChangeSpeed2.text())
        self.wpHomeLat=float(self.HLatitudeHomeLine.text())
        self.wpHomeLon=float(self.HLongitudeHomeLine.text())
        self.wpRightLat=float(self.HLatitudeRightLine.text())
        self.wpRightLon=float(self.HLongitudeRightLine.text())
        self.wpTakeLat=float(self.HLatitudeTakeLine.text())
        self.wpTakeLon=float(self.HLongitudeTakeLine.text())
        self.consLatitudeLongitude=0.0000089831
        self.wpRadius=float(self.radius.text())*self.consLatitudeLongitude
        self.wpHomeLatLong[0]=self.wpHomeLon
        self.wpHomeLatLong[1]=self.wpHomeLat
        self.wpBawahKananLatLong[0]=self.wpRightLon
        self.wpBawahKananLatLong[1]=self.wpRightLat
        self.wpBawahKiriLatLong[0]=2*self.wpHomeLon-self.wpRightLon
        self.wpBawahKiriLatLong[1]=2*self.wpHomeLat-self.wpRightLat
        self.rumusAtas=self.wpTakeLat-self.wpRightLat-(self.wpTakeLon*((self.wpRightLat-self.wpHomeLat)/(self.wpRightLon-self.wpHomeLon)))+(self.wpRightLon*((self.wpHomeLon-self.wpRightLon)/(self.wpRightLat-self.wpHomeLat)))
        self.rumusBawah=((self.wpHomeLon-self.wpRightLon)/(self.wpRightLat-self.wpHomeLat))-((self.wpRightLat-self.wpHomeLat)/(self.wpRightLon-self.wpHomeLon))
        self.wpAtasKananLatLong[0]=self.rumusAtas/self.rumusBawah
        self.wpAtasKananLatLong[1]=((self.wpRightLat-self.wpHomeLat)/(self.wpRightLon-self.wpHomeLon))*(self.wpAtasKananLatLong[0]-self.wpTakeLon)+self.wpTakeLat
        self.wpTakeLatLong[0]=self.wpTakeLon
        self.wpTakeLatLong[1]=self.wpTakeLat
        self.wpAtasKiriLatLong[0]=self.wpAtasKananLatLong[0]+(self.wpBawahKiriLatLong[0]-self.wpBawahKananLatLong[0])
        self.wpAtasKiriLatLong[1]=self.wpAtasKananLatLong[1]+(self.wpBawahKiriLatLong[1]-self.wpBawahKananLatLong[1])
        self.gradientSplineKanan=(self.wpAtasKananLatLong[0]-self.wpBawahKananLatLong[0])/(self.wpBawahKananLatLong[1]-self.wpAtasKananLatLong[1])
        self.gradientSplineKiri=(self.wpAtasKiriLatLong[0]-self.wpBawahKiriLatLong[0])/(self.wpBawahKiriLatLong[1]-self.wpAtasKiriLatLong[1])
        if(self.wpAtasKananLatLong[0]>self.wpAtasKiriLatLong[0]):
            self.wpSplineKiri[0]=((((self.wpAtasKiriLatLong[0]+self.wpBawahKiriLatLong[0])/2)*math.sqrt(self.gradientSplineKiri**2+1))-self.wpRadius)/(math.sqrt(self.gradientSplineKiri**2+1))
            self.wpSplineKiri[1]=self.gradientSplineKiri*(self.wpSplineKiri[0]-((self.wpAtasKiriLatLong[0]+self.wpBawahKiriLatLong[0])/2))+((self.wpAtasKiriLatLong[1]+self.wpBawahKiriLatLong[1])/2)

            self.wpSplineKanan[0]=((((self.wpAtasKananLatLong[0]+self30.wpBawahKananLatLong[0])/2)*math.sqrt(self.gradientSplineKanan**2+1))+self.wpRadius)/(math.sqrt(self.gradientSplineKanan**2+1))
            self.wpSplineKanan[1]=self.gradientSplineKanan*(self.wpSplineKanan[0]-((self.wpAtasKananLatLong[0]+self.wpBawahKananLatLong[0])/2))+((self.wpAtasKananLatLong[1]+self.wpBawahKananLatLong[1])/2)
        elif(self.wpAtasKananLatLong[0]<self.wpAtasKiriLatLong[0]):

            self.wpSplineKiri[0]=((((self.wpAtasKiriLatLong[0]+self.wpBawahKiriLatLong[0])/2)*math.sqrt(self.gradientSplineKiri**2+1))+self.wpRadius)/(math.sqrt(self.gradientSplineKiri**2+1))
            self.wpSplineKiri[1]=self.gradientSplineKiri*(self.wpSplineKiri[0]-((self.wpAtasKiriLatLong[0]+self.wpBawahKiriLatLong[0])/2))+((self.wpAtasKiriLatLong[1]+self.wpBawahKiriLatLong[1])/2)

            self.wpSplineKanan[0]=((((self.wpAtasKananLatLong[0]+self.wpBawahKananLatLong[0])/2)*math.sqrt(self.gradientSplineKanan**2+1))-self.wpRadius)/(math.sqrt(self.gradientSplineKanan**2+1))
            self.wpSplineKanan[1]=self.gradientSplineKanan*(self.wpSplineKanan[0]-((self.wpAtasKananLatLong[0]+self.wpBawahKananLatLong[0])/2))+((self.wpAtasKananLatLong[1]+self.wpBawahKananLatLong[1])/2)
            
        #Index 0 = Longitude, Index 1 = Latitude
        #Latitude = Y, Longitude = X
        self.gradientSplineKanan=self.wpAtasKananLatLong[0]-self.wpBawahKananLatLong[0]
        self.wpLength=math.sqrt(((self.wpHomeLat-self.wpRightLat)**2)+((self.wpHomeLon-self.wpRightLon)**2))/self.consLatitudeLongitude

        


        print(self.wpLength)
        with open('datawp_dump.csv','w',newline='')as file:
            fieldname=['8','Aerial']
            writer =csv.DictWriter(file,fieldnames=fieldname)
            writer.writeheader()
            writer.writerow({'8': self.wpHomeLatLong[0],'Aerial':self.wpHomeLatLong[1]})
            writer.writerow({'8': self.wpBawahKananLatLong[0],'Aerial':self.wpBawahKananLatLong[1]})
            writer.writerow({'8': self.wpBawahKiriLatLong[0],'Aerial':self.wpBawahKiriLatLong[1]})
            writer.writerow({'8': self.wpTakeLatLong[0],'Aerial':self.wpTakeLatLong[1]})
            writer.writerow({'8': self.wpAtasKananLatLong[0],'Aerial':self.wpAtasKananLatLong[1]})
            writer.writerow({'8': self.wpAtasKiriLatLong[0],'Aerial':self.wpAtasKiriLatLong[1]})
            writer.writerow({'8': self.wpSplineKanan[0],'Aerial':self.wpSplineKanan[1]})
            writer.writerow({'8': self.wpSplineKiri[0],'Aerial':self.wpSplineKiri[1]})
        
        with open('Mission2.waypoints', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(["QGC WPL 110"])
            spamwriter.writerow([0,1,0,16,0,0,0,0,self.wpHomeLatLong[1],self.wpHomeLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([1,0,10,178,self.wpSpeedTrans,self.wpSpeedTrans,0,0,0,0,0,1]) #Do Change Speed Translasi
            spamwriter.writerow([2,0,10,16,0,0,0,0,self.wpHomeLatLong[1],self.wpHomeLatLong[0],3,1])
            spamwriter.writerow([3,0,10,16,0,0,0,0,self.wpBawahKananLatLong[1],self.wpBawahKananLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([4,0,10,178,self.wpSpeedTrans+0.3,self.wpSpeedTrans+0.3,0,0,0,0,0,1]) #Do Change Speed Spline
            spamwriter.writerow([5,0,10,82,0,0,0,0,self.wpSplineKanan[1],self.wpSplineKanan[0],self.wpAltitude,1])
            spamwriter.writerow([6,0,10,82,0,0,0,0,self.wpAtasKananLatLong[1],self.wpAtasKananLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([7,0,10,16,0,0,0,0,self.wpPickLatLong[1],self.wpPickLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([8,0,10,16,0,0,0,0,self.wpAtasKiriLatLong[1],self.wpAtasKiriLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([9,0,10,178,self.wpSpeedTrans+0.8,self.wpSpeedTrans+0.8,0,0,0,0,0,1]) #Do Change Speed Spline
            spamwriter.writerow([10,0,10,82,0,0,0,0,self.wpSplineKiri[1],self.wpSplineKiri[0],self.wpAltitude,1])
            spamwriter.writerow([11,0,10,82,0,0,0,0,self.wpBawahKiriLatLong[1],self.wpBawahKiriLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([12,0,10,16,0,0,0,0,self.wpHomeLatLong[1],self.wpHomeLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([13,0,10,16,0,0,0,0,self.wpBawahKananLatLong[1],self.wpBawahKananLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([14,0,10,178,self.wpSpeedTrans+1.1,self.wpSpeedTrans+1.1,0,0,0,0,0,1]) #Do Change Speed Translasi
            spamwriter.writerow([15,0,10,82,0,0,0,0,self.wpSplineKanan[1],self.wpSplineKanan[0],self.wpAltitude,1])
            spamwriter.writerow([16,0,10,82,0,0,0,0,self.wpAtasKananLatLong[1],self.wpAtasKananLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([17,0,10,16,0,0,0,0,self.wpPickLatLong[1],self.wpPickLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([18,0,10,93,0.1,0,0,0,0,0,0,1]) # Delay
            spamwriter.writerow([19,0,10,178,self.wpSpeedScan,self.wpSpeedScan+0.8,0,0,0,0,0,1]) #Do Change Speed Spline
            spamwriter.writerow([20,0,10,16,0,0,0,0,self.wpAtasKiriLatLong[1],self.wpAtasKiriLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([21,0,10,178,self.wpSpeedTrans+1,self.wpSpeedTrans+1,0,0,0,0,0,1]) #Do Change Speed Translasi
            spamwriter.writerow([22,0,10,82,0,0,0,0,self.wpSplineKiri[1],self.wpSplineKiri[0],self.wpAltitude,1])
            spamwriter.writerow([23,0,10,82,0,0,0,0,self.wpBawahKiriLatLong[1],self.wpBawahKiriLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([24,0,10,16,0,0,0,0,self.wpHomeLatLong[1],self.wpHomeLatLong[0],3,1])

            
            

    def basicWPMission2TipeB(self):
        self.wpAltitude=float(self.Altitude.text())
        self.wpSpeedTrans=float(self.ChangeSpeed1.text())
        self.wpSpeedScan=float(self.ChangeSpeed2.text())
        self.wpLatitude=float(self.home_latitude.text())
        self.wpLongitude=float(self.home_longitude.text())
        self.wpPanjang=self.lenghtSlider.value()
        self.wpLebar=self.widthSlider.value()
        self.wpRadius=float(self.radius.text())
        self.wpRotasi=float(self.home_rotasi.text())

        self.consLatitudeLongitude=0.0000089831
        self.wpHomeLatLong[0]=self.wpLongitude
        self.wpHomeLatLong[1]=self.wpLatitude

        self.wpSplineKanan[1]=self.wpLatitude+self.meterToLatLong(self.wpLebar/2.0)
        self.wpSplineKanan[0]=self.wpLongitude+self.meterToLatLong((self.wpPanjang+self.wpRadius)/2)
        self.wpSplineKiri[1]=self.wpLatitude+self.meterToLatLong(self.wpLebar/2.0)
        self.wpSplineKiri[0]=self.wpLongitude-self.meterToLatLong((self.wpPanjang+self.wpRadius)/2)
        self.wpBawahKananLatLong[0]=self.wpLongitude+self.meterToLatLong(self.wpPanjang/2.0)
        self.wpBawahKananLatLong[1]=self.wpLatitude
        self.wpAtasKananLatLong[0]=self.wpLongitude+self.meterToLatLong(self.wpPanjang/2.0)
        self.wpAtasKananLatLong[1]=self.wpLatitude+self.meterToLatLong(self.wpLebar)
        self.wpBawahKiriLatLong[0]=self.wpLongitude-self.meterToLatLong(self.wpPanjang/2.0)
        self.wpBawahKiriLatLong[1]=self.wpLatitude
        self.wpAtasKiriLatLong[0]=self.wpLongitude-self.meterToLatLong(self.wpPanjang/2.0)
        self.wpAtasKiriLatLong[1]=self.wpLatitude+self.meterToLatLong(self.wpLebar)
        self.wpPickLatLong[1]=self.wpLatitude+self.meterToLatLong(self.wpLebar)
        self.wpPickLatLong[0]=self.wpLongitude

        self.wpBawahKananLatLong[1],self.wpBawahKananLatLong[0]=self.rotation(self.wpBawahKananLatLong[1],self.wpBawahKananLatLong[0],self.wpRotasi)
        self.wpAtasKananLatLong[1],self.wpAtasKananLatLong[0]=self.rotation(self.wpAtasKananLatLong[1],self.wpAtasKananLatLong[0],self.wpRotasi)
        self.wpBawahKiriLatLong[1],self.wpBawahKiriLatLong[0]=self.rotation(self.wpBawahKiriLatLong[1],self.wpBawahKiriLatLong[0],self.wpRotasi)
        self.wpAtasKiriLatLong[1],self.wpAtasKiriLatLong[0]=self.rotation(self.wpAtasKiriLatLong[1],self.wpAtasKiriLatLong[0],self.wpRotasi)
        self.wpSplineKanan[1],self.wpSplineKanan[0]=self.rotation(self.wpSplineKanan[1],self.wpSplineKanan[0],self.wpRotasi)
        self.wpSplineKiri[1],self.wpSplineKiri[0]=self.rotation(self.wpSplineKiri[1],self.wpSplineKiri[0],self.wpRotasi)
        self.wpPickLatLong[1],self.wpPickLatLong[0]=self.rotation(self.wpPickLatLong[1],self.wpPickLatLong[0],self.wpRotasi)


        #Rotasi

        with open('Mission2.waypoints', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(["QGC WPL 110"])
            spamwriter.writerow([0,1,0,16,0,0,0,0,self.wpHomeLatLong[1],self.wpHomeLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([1,0,10,178,self.wpSpeedTrans,self.wpSpeedTrans,0,0,0,0,0,1]) #Do Change Speed Translasi
            spamwriter.writerow([2,0,10,16,0,0,0,0,self.wpHomeLatLong[1],self.wpHomeLatLong[0],3,1])
            spamwriter.writerow([3,0,10,16,0,0,0,0,self.wpBawahKananLatLong[1],self.wpBawahKananLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([4,0,10,178,self.wpSpeedTrans+0.3,self.wpSpeedTrans+0.3,0,0,0,0,0,1]) #Do Change Speed Spline
            spamwriter.writerow([5,0,10,82,0,0,0,0,self.wpSplineKanan[1],self.wpSplineKanan[0],self.wpAltitude,1])
            spamwriter.writerow([6,0,10,82,0,0,0,0,self.wpAtasKananLatLong[1],self.wpAtasKananLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([7,0,10,16,0,0,0,0,self.wpPickLatLong[1],self.wpPickLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([8,0,10,16,0,0,0,0,self.wpAtasKiriLatLong[1],self.wpAtasKiriLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([9,0,10,178,self.wpSpeedTrans+0.8,self.wpSpeedTrans+0.8,0,0,0,0,0,1]) #Do Change Speed Spline
            spamwriter.writerow([10,0,10,82,0,0,0,0,self.wpSplineKiri[1],self.wpSplineKiri[0],self.wpAltitude,1])
            spamwriter.writerow([11,0,10,82,0,0,0,0,self.wpBawahKiriLatLong[1],self.wpBawahKiriLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([12,0,10,16,0,0,0,0,self.wpHomeLatLong[1],self.wpHomeLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([13,0,10,16,0,0,0,0,self.wpBawahKananLatLong[1],self.wpBawahKananLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([14,0,10,178,self.wpSpeedTrans+1.1,self.wpSpeedTrans+1.1,0,0,0,0,0,1]) #Do Change Speed Translasi
            spamwriter.writerow([15,0,10,82,0,0,0,0,self.wpSplineKanan[1],self.wpSplineKanan[0],self.wpAltitude,1])
            spamwriter.writerow([16,0,10,82,0,0,0,0,self.wpAtasKananLatLong[1],self.wpAtasKananLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([17,0,10,16,0,0,0,0,self.wpPickLatLong[1],self.wpPickLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([18,0,10,93,0.1,0,0,0,0,0,0,1]) # Delay
            spamwriter.writerow([19,0,10,178,self.wpSpeedScan,self.wpSpeedScan+0.8,0,0,0,0,0,1]) #Do Change Speed Spline
            spamwriter.writerow([20,0,10,16,0,0,0,0,self.wpAtasKiriLatLong[1],self.wpAtasKiriLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([21,0,10,178,self.wpSpeedTrans+1,self.wpSpeedTrans+1,0,0,0,0,0,1]) #Do Change Speed Translasi
            spamwriter.writerow([22,0,10,82,0,0,0,0,self.wpSplineKiri[1],self.wpSplineKiri[0],self.wpAltitude,1])
            spamwriter.writerow([23,0,10,82,0,0,0,0,self.wpBawahKiriLatLong[1],self.wpBawahKiriLatLong[0],self.wpAltitude,1])
            spamwriter.writerow([24,0,10,16,0,0,0,0,self.wpHomeLatLong[1],self.wpHomeLatLong[0],3,1])

        with open('datawp_dump.csv','w',newline='')as file:
            fieldname=['8','Aerial']
            writer =csv.DictWriter(file,fieldnames=fieldname)
            writer.writeheader()
            writer.writerow({'8': self.wpHomeLatLong[0],'Aerial':self.wpHomeLatLong[1]})
            writer.writerow({'8': self.wpBawahKananLatLong[0],'Aerial':self.wpBawahKananLatLong[1]})
            writer.writerow({'8': self.wpSplineKanan[0],'Aerial':self.wpSplineKanan[1]})
            writer.writerow({'8': self.wpAtasKananLatLong[0],'Aerial':self.wpAtasKananLatLong[1]})
            writer.writerow({'8': self.wpPickLatLong[0],'Aerial':self.wpPickLatLong[1]})
            writer.writerow({'8': self.wpAtasKiriLatLong[0],'Aerial':self.wpAtasKiriLatLong[1]})
            writer.writerow({'8': self.wpSplineKiri[0],'Aerial':self.wpSplineKiri[1]})
            writer.writerow({'8': self.wpBawahKiriLatLong[0],'Aerial':self.wpBawahKiriLatLong[1]})
            self.view.reload()
      
    def rotation(self,x,y,sudut):
        a=self.wpHomeLatLong[1]
        b=self.wpHomeLatLong[0]
        rad=(sudut*math.pi)/180
        x_rotasi=(((x-a)*math.cos(rad))-((y-b)*math.sin(rad)))+a
        y_rotasi=(((x-a)*math.sin(rad))+((y-b)*math.cos(rad)))+b
        return x_rotasi,y_rotasi

   

    
    def meterToLatLong(self,delta):
        return self.consLatitudeLongitude*delta





    def setPanjang(self):
        self.panjangPath=self.lenghtSlider.value()
        self.lengthText.setText("Panjang Path : "+str(self.panjangPath)+"m")

    
    def setLebar(self):
        self.lebarPath=self.widthSlider.value()
        self.widthText.setText("Lebar Path : "+str(self.lebarPath)+"m")


    def optionMission(self,b):
        if b.text()=="Tipe A":
            self.Mission2Type='A'
            self.clearLayout()
            self.setMission2LayoutTipeA()
            print("Set Mission 2 Type A")
        if b.text()=="Tipe B":
            self.Mission2Type='B'
            self.clearLayout()
            self.setMission2LayoutTipeB()
            print("Set Mission 2 Type B")

    def setHomeFun(self):
        self.translasiDump()
    def setRotasiFun(self):
        index =np.size(self.dataWaypoint,1)
        i=1
        degre=float(self.home_rotasi.text())
        for i in range(index):
            if(i>0):
                latitude_rotasi,longitude_rotasi=self.rotation(float(self.dataWaypoint[1][i]),float(self.dataWaypoint[0][i]),degre)
                self.dataWaypoint[1][i]=latitude_rotasi
                self.dataWaypoint[0][i]=longitude_rotasi
        with open('datawp_dump.csv','w',newline='')as file:
            fieldname=['latitude','longitude']
            writer =csv.DictWriter(file,fieldnames=fieldname)
            writer.writeheader()
            for i in range (index):
                writer.writerow({'latitude': self.dataWaypoint[0][i],'longitude':self.dataWaypoint[1][i]})
        self.view.reload()
        
    def readWP(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Waypoint Files(*.waypoints)")
        self.readWaypoint(self.fname[0])



    def setLogo(self):
        self.logo=QLabel()
        img_logo=QPixmap()
        img_logo.load("Ashwincarra.png")
        self.logo.setPixmap(img_logo.scaledToWidth(300))
    def setMaps(self):
        self.view =QWebEngineView()
        self.view.load(QUrl.fromLocalFile(os.path.abspath('index.html')))
        return self.view

    def readWaypoint(self,file_location):
        with open(file_location) as csv_file:
            csv_reader=csv.reader(csv_file,delimiter='\t')
            line_count=0
            latitude=[]
            longitude=[]
            self.row0=[]
            self.row1=[]
            self.row2=[]
            self.row3=[]
            self.row4=[]
            self.row5=[]
            self.row6=[]
            self.row7=[]
            self.row10=[]
            self.row11=[]
            for row in csv_reader:
                if line_count==0:
                    line_count+=1
                else:
                    self.row0.append(row[0])
                    self.row1.append(row[1])
                    self.row2.append(row[2])
                    self.row3.append(row[3])
                    self.row4.append(row[4])
                    self.row5.append(row[5])
                    self.row6.append(row[6])
                    self.row7.append(row[7])
                    self.row10.append(row[10])
                    self.row11.append(row[11])


                    latitude.append(row[9])
                    longitude.append(row[8])
                    
                    line_count+=1
            self.dataWaypoint=np.array([latitude,longitude])
               
            print(self.dataWaypoint)
            print(np.size(self.dataWaypoint,1))
            index =np.size(self.dataWaypoint,1)
            self.setHome.setDisabled(False)
            self.setRotasi.setDisabled(False)
            self.home_latitude.setText(self.dataWaypoint[1][0])
            self.home_longitude.setText(self.dataWaypoint[0][0])

        with open('datawp_dump.csv','w',newline='')as file:
                fieldname=['latitude','longitude']
                writer =csv.DictWriter(file,fieldnames=fieldname)
                writer.writeheader()
                for i in range (index):
                    writer.writerow({'latitude': self.dataWaypoint[0][i],'longitude':self.dataWaypoint[1][i]})
        self.view.reload()

    def writeWP(self):
        index =np.size(self.dataWaypoint,1)
        with open('eggs.waypoints', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(["QGC WPL 110"])
            for i in range (index):
                spamwriter.writerow([self.row0[i],self.row1[i],self.row2[i],self.row3[i],self.row4[i],self.row5[i],self.row6[i],self.row7[i],self.dataWaypoint[1][i],self.dataWaypoint[0][i],self.row10[i],self.row11[i]])
            
    def translasiDump(self):
        index =np.size(self.dataWaypoint,1)
        deltaLatitude=float(self.home_latitude.text())- float(self.dataWaypoint[1][0])
        deltaLongitude=float(self.home_longitude.text())-float(self.dataWaypoint[0][0])
        with open('datawp_dump.csv','w',newline='')as file:
            fieldname=['latitude','longitude']
            writer =csv.DictWriter(file,fieldnames=fieldname)
            writer.writeheader()
            for i in range (index):
                writer.writerow({'latitude': float(self.dataWaypoint[0][i])+deltaLongitude,'longitude':float(self.dataWaypoint[1][i])+deltaLatitude})
                self.dataWaypoint[0][i]=float(self.dataWaypoint[0][i])+deltaLongitude
                self.dataWaypoint[1][i]=float(self.dataWaypoint[1][i])+deltaLatitude
        self.view.reload()


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ashwincarra Advance Waypoint")
        self.createMenu()
        self.mainMission2=Mission2Form()
        self.mainMission1=Mission1Form()
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.variabel_central_widget=QStackedWidget()
        # self.variabel_central_widget.addWidget(self.mainMission2)
        self.variabel_central_widget.addWidget(self.mainMission1)
        self.variabel_central_widget.setCurrentWidget(self.mainMission1)
        self.setCentralWidget(self.variabel_central_widget)

    def createMenu(self):
        self.mainMenuButton=self.menuBar().addMenu("&Mission 1")
        self.mainMenuButton=self.menuBar().addMenu("&Mission 2")
       




if __name__=="__main__":
    app=QApplication(sys.argv)
    vMainWindow=MainWindow()
    vMainWindow.show()
    sys.exit(app.exec_())


    

