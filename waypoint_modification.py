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


class MainMenuForm(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setForm()
        
    def setForm(self):
        self.wpHomeLatLong=[0,0]
        self.wpBawahKananLatLong=[0,0]
        self.wpBawahKiriLatLong=[0,0]
        self.wpAtasKananLatLong=[0,0]
        self.wpAtasKiriLatLong=[0,0]


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
        self.generateMission1=QRadioButton("Mission 1")
        self.generateMission2=QRadioButton("Mission 2")
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
        self.VMenuLayout.addLayout(self.HMissionLayout,1)
        self.VMenuLayout.addLayout(self.HAltitude,1)
        self.VMenuLayout.addLayout(self.HChangeSpeed1,1)
        self.VMenuLayout.addLayout(self.HChangeSpeed2,1)
        
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
        self.VMenuLayout.addLayout(self.HTranslasi1,1)
        self.VMenuLayout.addLayout(self.HTranslasi2,1)
        
        # self.VMenuLayout.addWidget(self.setHome)

        self.home_rotasi=QLineEdit()
        self.textRotasi=QLabel("Rotasi")
        self.setRotasi=QPushButton("Set Rotasi")
        self.setRotasi.clicked.connect(self.setRotasiFun)
        self.setRotasi.setDisabled(True)
        self.HRotasi=QHBoxLayout()
        self.HRotasi.addWidget(self.textRotasi,1)
        self.HRotasi.addWidget(self.home_rotasi,1)
        self.VMenuLayout.addLayout(self.HRotasi,1)
        self.VMenuLayout.addWidget(self.widthText)
        self.VMenuLayout.addWidget(self.widthSlider)
        self.VMenuLayout.addWidget(self.lengthText)
        self.VMenuLayout.addWidget(self.lenghtSlider)
        self.VMenuLayout.addWidget(self.generateButton,1)
        # self.VMenuLayout.addWidget(self.setRotasi)
        self.VMenuLayout.addWidget(self.setLogo(),1)
    
    def GenerateWP(self):
        self.wpAltitude=int(self.Altitude.text())
        self.wpSpeedTrans=int(self.ChangeSpeed1.text())
        self.wpSpeedScan=int(self.ChangeSpeed2.text())
        self.wpLatitude=int(self.home_latitude.text())
        self.wpLongitude=int(self.home_longitude.text())
        self.wpMission=self.mission_selected
        self.wpPanjang=self.lenghtSlider.value()
        self.wpLebar=self.widthSlider.value()
        print(self.wpPanjang)
        print(self.wpLebar)
        if(self.wpMission==1):
            print("Mission 1")
        if(self.wpMission==2):
            print("Mission 2")
            self.createMission2()
    
    def createMission2(self):
        self.basicWPMission2()
        
    def basicWPMission2(self):
        self.consLatitudeLongitude=0.000089831
        self.wpHomeLatLong[0]=0.00000000
        self.wpHomeLatLong[1]=0.00000000
        self.wpBawahKananLatLong[0]=self.meterToLatLong(self.wpPanjang/2.0)
        self.wpBawahKananLatLong[1]=0.00000000
        self.wpAtasKananLatLong[0]=self.meterToLatLong(self.wpPanjang/2.0)
        self.wpAtasKananLatLong[1]=self.meterToLatLong(self.wpLebar)
        self.wpBawahKiriLatLong[0]=-self.meterToLatLong(self.wpPanjang/2.0)
        self.wpBawahKiriLatLong[1]=0.00000000
        self.wpAtasKiriLatLong[0]=-self.meterToLatLong(self.wpPanjang/2.0)
        self.wpAtasKiriLatLong[1]=self.meterToLatLong(self.wpLebar)
        with open('eggs.waypoints', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(["QGC WPL 110"])
            spamwriter.writerow([0,1,0,0,0,0,0,0,0,0,0,0])
            spamwriter.writerow([1,0,10,16,0,0,0,0,self.wpHomeLatLong[0],self.wpHomeLatLong[1],0,1])
            spamwriter.writerow([2,0,10,16,0,0,0,0,self.wpBawahKananLatLong[0],self.wpBawahKananLatLong[1],0,1])
            spamwriter.writerow([3,0,10,16,0,0,0,0,self.wpAtasKananLatLong[0],self.wpAtasKananLatLong[1],0,1])
            spamwriter.writerow([4,0,10,16,0,0,0,0,self.wpAtasKiriLatLong[0],self.wpAtasKiriLatLong[1],0,1])
            spamwriter.writerow([5,0,10,16,0,0,0,0,self.wpBawahKiriLatLong[0],self.wpBawahKiriLatLong[1],0,1])

            print("test")

                
    
    def meterToLatLong(self,delta):
        return self.consLatitudeLongitude*delta


    def setPanjang(self):
        self.panjangPath=self.lenghtSlider.value()
        self.lengthText.setText("Panjang Path : "+str(self.panjangPath)+"m")

    
    def setLebar(self):
        self.lebarPath=self.widthSlider.value()
        self.widthText.setText("Lebar Path : "+str(self.lebarPath)+"m")


    def optionMission(self,b):
        if b.text()=="Mission 1":
            self.mission_selected=1
        if b.text()=="Mission 2":
            self.mission_selected=2


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
        logo=QLabel()
        img_logo=QPixmap()
        img_logo.load("Ashwincarra.png")
        logo.setPixmap(img_logo.scaledToWidth(300))
        return logo
    def setMaps(self):
        self.view =QWebEngineView()
        self.view.load(QUrl.fromLocalFile(os.path.abspath('/home/hamz/Documents/GUI_TUBITAK_ASHWINCARRA/maps/dist/index.html')))
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

    def rotation(self,x,y,sudut):
        a=float(self.dataWaypoint[1][0])
        b=float(self.dataWaypoint[0][0])
        rad=(sudut*math.pi)/180
        x_rotasi=(((x-a)*math.cos(rad))-((y-b)*math.sin(rad)))+a
        y_rotasi=(((x-a)*math.sin(rad))+((y-b)*math.cos(rad)))+b
        return x_rotasi,y_rotasi

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ashwincarra Advance Waypoint")
        self.createMenu()
        self.mainMenu=MainMenuForm()
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.variabel_central_widget=QStackedWidget()
        self.variabel_central_widget.addWidget(self.mainMenu)
        self.variabel_central_widget.setCurrentWidget(self.mainMenu)
        self.setCentralWidget(self.variabel_central_widget)

    def createMenu(self):
        self.mainMenuButton=self.menuBar().addMenu("&Menu")
        self.mainMenuButton.addAction("&MainMenu",self.close)
        self.mainMenuButton.addAction("&Exit",self.close)




if __name__=="__main__":
    app=QApplication(sys.argv)
    vMainWindow=MainWindow()
    vMainWindow.show()
    sys.exit(app.exec_())


    

