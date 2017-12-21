# Use pyQt5 GUI to show figures of linear regression to analysis the correlations of SAT scores
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore 
from PyQt5 import QtWidgets
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import pandas as pd
import sqlite3

import satpkg.datapro as dp        #here
from sqlite_module import sqlpro  #here
    
class MatplotlibWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(111)        
        self.layoutVertical = QtWidgets.QVBoxLayout(self)        
        self.layoutVertical.addWidget(self.canvas)
        
               
class MyWindow(QtWidgets.QWidget):
    num = 0
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Save to SQLite")
        self.button1.clicked.connect(self.button1_clicked) 
        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setText("Read from SQLite")
        self.button2.clicked.connect(self.button2_clicked)
        
        self.lb = QtWidgets.QLabel(self)
        self.lb.setText('6018-2017 Project. Select from the drop down list to see figures and linear regression analysis results')
        
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItem("0. Dollars distribution")
        self.comboBox.addItem("1. Math distribution")
        self.comboBox.addItem("2. Verbal distribution")
        self.comboBox.addItem("3. Math Verbal distribution")
        self.comboBox.addItem("4. Dollars Box plots")
        self.comboBox.addItem("5. Math Box plots")
        self.comboBox.addItem("6. Verbal Box plots")
        self.comboBox.addItem("7. Pay - Verbal Linear Regression")
        self.comboBox.addItem("8. Dollars - Verbal Linear Regression")        
        self.comboBox.addItem("9. Math - Verbal Linear Regression")
        
        #self.comboBox.move(50, 250)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

        self.matplotlibWidget = MatplotlibWidget(self)
        self.layoutVertical = QtWidgets.QVBoxLayout(self) 
        self.layoutVertical.addWidget(self.lb)
        self.layoutVertical.addWidget(self.comboBox)
        self.layoutVertical.addWidget(self.matplotlibWidget)     
        self.layoutVertical.addWidget(self.button1)
        self.layoutVertical.addWidget(self.button2)
    
    @QtCore.pyqtSlot()
    def button1_clicked(self):          
        sqlite_file = 'states_sat.db'    
        table_name = 'sat_table'    
        sqlpro.save_to_sqlite(sqlite_file, table_name)   # here
    @QtCore.pyqtSlot()
    def button2_clicked(self):         
        sqlite_file = 'states_sat.db'    
        table_name = 'sat_table'   
        dataset=sqlpro.read_from_sqlite(sqlite_file, table_name)  # here

    def selectionchange(self,i):
        if i==0:            
            num_dict = dp.sat_data_dict()
            x = dp.histbox(num_dict, 'dollars')
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.hist(x, bins=50, normed=True, color='r', alpha=0.7, label='dollars')   
            self.matplotlibWidget.axis.set_xlabel('State spending on public education, in $1000s per student.')
            self.matplotlibWidget.axis.set_ylabel('Probability')
            self.matplotlibWidget.canvas.draw()   
            
        if i==1:   
            num_dict = dp.sat_data_dict()    #here
            x = dp.histbox(num_dict, 'SATM')   #here
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.hist(x, bins=50, normed=True, color='g', alpha=0.7, label='Math')     
            self.matplotlibWidget.axis.set_xlabel('Math')
            self.matplotlibWidget.axis.set_ylabel('Probability')
            self.matplotlibWidget.canvas.draw()   
            
        if i==2:            
            num_dict = dp.sat_data_dict()
            x = dp.histbox(num_dict, 'SATV')
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.hist(x, bins=50, normed=True, color='b', alpha=0.7, label='Math')     
            self.matplotlibWidget.axis.set_xlabel('Verbal')
            self.matplotlibWidget.axis.set_ylabel('Probability')
            self.matplotlibWidget.canvas.draw()
            
        if i==3:            
            num_dict = dp.sat_data_dict()           
            x2 = dp.histbox(num_dict, 'SATM')
            x3 = dp.histbox(num_dict, 'SATV')
            self.matplotlibWidget.axis.clear()            
            self.matplotlibWidget.axis.hist(x2, bins=50, color='r', alpha=0.6, label='Math')
            self.matplotlibWidget.axis.hist(x3, bins=50, color='b', alpha=0.6, label='Verbal')
            self.matplotlibWidget.axis.set_xlabel('Score')
            self.matplotlibWidget.axis.set_ylabel('Probability')
            self.matplotlibWidget.axis.legend()
            self.matplotlibWidget.canvas.draw()
            
        if i==4:
            num_dict = dp.sat_data_dict()
            x = dp.histbox(num_dict, 'dollars')
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.boxplot(x)   
            self.matplotlibWidget.axis.set_xlabel('State spending on public education, in $1000s per student')
            self.matplotlibWidget.axis.set_ylabel('$1000')
            self.matplotlibWidget.canvas.draw()
            
            
        if i==5:   
            num_dict = dp.sat_data_dict()
            x = dp.histbox(num_dict, 'SATM')
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.boxplot(x)   
            self.matplotlibWidget.axis.set_xlabel('Math')
            self.matplotlibWidget.axis.set_ylabel('Score')
            self.matplotlibWidget.canvas.draw()
            
        if i==6:
            num_dict = dp.sat_data_dict()
            x = dp.histbox(num_dict, 'SATV')
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.boxplot(x)   
            self.matplotlibWidget.axis.set_xlabel('Verbal')
            self.matplotlibWidget.axis.set_ylabel('Score')
            self.matplotlibWidget.canvas.draw()
            
        if i==7:  
            df = dp.sat_df()
            x,y=dp.scatterplt(df,'pay','SATV')
            num_dict = dp.sat_data_dict()
            x1,y1=dp.linear_re('pay','SATV', num_dict) 
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.scatter(x,y, color='g')  
            self.matplotlibWidget.axis.plot(x1,y1, color='r')
            self.matplotlibWidget.axis.set_xlabel('Average teacher salary in the state, in $1000s')
            self.matplotlibWidget.axis.set_ylabel('Verbal')            
            self.matplotlibWidget.canvas.draw()         

            
        if i==8:            
            df = dp.sat_df()
            x,y=dp.scatterplt(df,'dollars','SATV')
            num_dict = dp.sat_data_dict()
            x1,y1=dp.linear_re('dollars','SATV', num_dict) 
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.scatter(x,y, color='k')  
            self.matplotlibWidget.axis.plot(x1,y1, color='r')
            self.matplotlibWidget.axis.set_xlabel('State spending on public education, in $1000s per student')
            self.matplotlibWidget.axis.set_ylabel('Verbal') 
            self.matplotlibWidget.canvas.draw()                  

                           
        if i==9:            
            df = dp.sat_df()
            x,y=dp.scatterplt(df,'SATM','SATV')
            num_dict = dp.sat_data_dict()
            x1,y1=dp.linear_re('SATM','SATV', num_dict) 
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.scatter(x,y, color='b') 
            self.matplotlibWidget.axis.plot(x1,y1, color='r')   
            self.matplotlibWidget.axis.set_xlabel('Math')
            self.matplotlibWidget.axis.set_ylabel('Verbal')
            self.matplotlibWidget.canvas.draw()  

            
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.resize(888, 444)
    main.show()
    
    app.exec_()

if __name__ == '__main__':
    main()
