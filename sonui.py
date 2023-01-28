import sys
import numpy as np
import folium
import io
import pandas as pd
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore  import pyqtSlot
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QDialog , QApplication , QHBoxLayout, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5.QtWebEngineWidgets import QWebEngineView



class pusay(QDialog):
	def __init__(self):
		super(pusay,self).__init__()
		
		

		loadUi("tam.ui",self)

		self.setWindowTitle("Pusay")
		
		self.logic = 0
		self.value = 1,
		self.SHOWKAMERA.clicked.connect(self.onClicked)
		self.SHOWGPS.clicked.connect(self.displayMap)
		

		self.KALK.clicked.connect(self.otonom_kalkis)
		self.IN.clicked.connect(self.otonom_inis)
		self.SEYIR.clicked.connect(self.seyir)
		self.KILIT.clicked.connect(self.kilit)
		self.KAMIKAZE.clicked.connect(self.kamikaze)


	@pyqtSlot()
	def onClicked(self):
		
		cap =cv2.VideoCapture(0)
		
		while(cap.isOpened()):
			ret, frame=cap.read()

			if ret==True:
				self.displayImage(frame,1)
				cv2.waitKey()
				
			else:
				print('not found')

		cap.release()
		self.TEXT.setText('Kameraya bağlanıldı...')
		cv2.destroyAllWindows()



	def displayMap(self):

		lay = QVBoxLayout(self)
		self.setLayout(lay)

		# Make an empty map
		m = folium.Map(location=[37.85833541891159,27.858269004327532], tiles="OpenStreetMap", zoom_start=15)

		# Show the map
		m
		

		data = pd.DataFrame({
   			'lon':[37.85833541891159, 37.857387614460706, 37.862552475419825, 37.857243696790526,  37.85681211874349, 37.86032278471753],
   			'lat':[27.858269004327532, 27.862529310115992, 27.855825452481305, 27.86291412369107, 27.85600359208963, 27.84944944772177],
   			'name':['Pusay', 'Algan', 'Metu', 'Kapsul', 'Anatek', 'Koustech'],
			'color':['green', 'red', 'red', 'red', 'red', 'red']
   			
		}, dtype=str)

		data

		for i in range(0,len(data)):
			folium.Marker(
				location=[data.iloc[i]['lon'], data.iloc[i]['lat']],
				popup=data.iloc[i]['name'],
				tooltip=data.iloc[i]['name'],
				icon=folium.Icon(icon='plane', icon_color=data.iloc[i]['color'])

			).add_to(m)
		
		m
	


		veri = io.BytesIO()
		m.save(veri, close_file=False)

		
		self.web.setHtml(veri.getvalue().decode())
		self.TEXT.setText('Haritaya bağlanıldı')
		



		
		

	
	def displayImage(self,img,window=1):
		qformat=QImage.Format_Indexed8
		if len(img.shape)==3:
			if(img.shape[2])==4:
				qformat=QImage.Format_RGBA888
			else:
				qformat=QImage.Format_RGB888
		img = QImage(img,img.shape[1],img.shape[0],qformat)
		img = img.rgbSwapped()
		self.KAMERA.setPixmap(QPixmap.fromImage(img))
		self.KAMERA.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


	def otonom_kalkis(self):
		self.TEXT.setText('Otonom kalkış modu aktifleştirildi')

		self.KALK.setStyleSheet("border-radius : 10; background-color: green")

		self.IN.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.SEYIR.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KILIT.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KAMIKAZE.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")

	
	def otonom_inis(self):
		self.TEXT.setText('Otonom iniş modu aktifleştirildi')

		self.IN.setStyleSheet("border-radius : 10; background-color: green")

		self.KALK.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.SEYIR.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KILIT.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KAMIKAZE.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")

	def seyir(self):
		self.TEXT.setText('Seyir modu aktifleştirildi')

		self.SEYIR.setStyleSheet("border-radius : 10; background-color: green")

		self.IN.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KALK.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KILIT.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KAMIKAZE.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")

	def kilit(self):
		self.TEXT.setText('Otonom Kilitlenme modu aktifleştirildi')

		self.KILIT.setStyleSheet("border-radius : 10; background-color: green")

		self.IN.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KALK.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.SEYIR.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KAMIKAZE.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")


	def kamikaze(self):
		self.TEXT.setText('Otonom Kilitlenme modu aktifleştirildi')

		self.KAMIKAZE.setStyleSheet("border-radius : 10; background-color: green")

		self.IN.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KALK.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.SEYIR.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")
		self.KILIT.setStyleSheet("border-radius : 10; background-color: rgb(96, 96, 96)")	






		


        
app =  QApplication(sys.argv)
window=pusay()
window.show()
try:
	sys.exit(app.exec_())
except:
	print('excitng')