import scipy
import matplotlib.pyplot as pl
import numpy as np
import string
import math
import matplotlib.pyplot as plt
import csv
import sqlite3

from sqlite3 import Error
from tkinter import *
from tkinter.ttk import *
from numpy.random import randint
from numpy.random import normal
from numpy.random import rayleigh
from pandas import DataFrame
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def TkinterGui():
    root = Tk()
    root.title("Simulação de Alunos")

    childWindows = []

    ####################################################################################################################################################################################
    EntryNumHomeworks = Entry(root, width=50)

    EntryMaxScore = Entry(root, width=50)
    EntryMaxEffort = Entry(root, width=50)
    EntryMaxEfficiency = Entry(root, width=50)
    EntryMaxPerformance = Entry(root, width=50)

    EntryTotalFailBonus = Entry(root,width=50)
    EntrySuccessBonus = Entry(root,width=50)
    EntryFailBonus = Entry(root,width=50)
    EntryRedoBonus = Entry(root,width=50)

    EntryEffortTemp = Entry(root,width=50)
    EntryPerformanceTemp = Entry(root,width=50)
    EntryEfficiencyTemp = Entry(root,width=50)
    EntryDoTemp = Entry(root,width=50)
    EntryRightTemp = Entry(root,width=50)
    EntryRedoTemp = Entry(root,width=50)

    EntryPerformanceCoef = Entry(root,width=50)

    EntryMaxActivities = Entry(root,width=50)
    EntryMeanActivities = Entry(root,width=50)

    EntryLostEffort = Entry(root,width=50)

    EntryChooseGroup = Entry(root,width=50)

    EntryLayerName = Entry(root, width=50)
    EntryInputFile = Entry(root, width=50)

    ####################################################################################################################################################################################

    EntryNumHomeworks.grid(row=0, column=1)

    EntryMaxScore.grid(row=1, column=1)
    EntryMaxEffort.grid(row=2, column=1)
    EntryMaxEfficiency.grid(row=3, column=1)
    EntryMaxPerformance.grid(row=4, column=1)

    EntryTotalFailBonus.grid(row=5,column=1)
    EntrySuccessBonus.grid(row=6,column=1)
    EntryFailBonus.grid(row=7,column=1)
    EntryRedoBonus.grid(row=8,column=1)

    EntryEffortTemp.grid(row=9, column=1)
    EntryPerformanceTemp.grid(row=10, column=1)
    EntryEfficiencyTemp.grid(row=11, column=1)
    EntryDoTemp.grid(row=12, column=1)
    EntryRightTemp.grid(row=13, column=1)
    EntryRedoTemp.grid(row=14, column=1)

    EntryPerformanceCoef.grid(row=14, column=1)


    EntryMaxActivities.grid(row=15, column=1)
    EntryMeanActivities.grid(row=16, column=1)

    EntryLostEffort.grid(row=17, column=1)

    EntryChooseGroup.grid(row=18, column=1)

    EntryLayerName.grid(row=19, column=1)
    EntryInputFile.grid(row=20, column=1)
    ####################################################################################################################################################################################

    EntryNumHomeworks.insert(END, '1000')

    EntryMaxScore.insert(END, '100')
    EntryMaxEffort.insert(END, '100')
    EntryMaxEfficiency.insert(END, '100')
    EntryMaxPerformance.insert(END, '100')

    EntryTotalFailBonus.insert(END,'-0.1')
    EntrySuccessBonus.insert(END,'0.01')
    EntryFailBonus.insert(END,'-0.05')
    EntryRedoBonus.insert(END,'0.001')

    EntryEffortTemp.insert(END,'0.1')
    EntryPerformanceTemp.insert(END,'1.0')
    EntryEfficiencyTemp.insert(END,'0.2')
    EntryDoTemp.insert(END,'5.0')
    EntryRightTemp.insert(END,'2.5')
    EntryRedoTemp.insert(END,'2.5')

    EntryPerformanceCoef.insert(END,'0.65')

    EntryMaxActivities.insert(END,'20.0')
    EntryMeanActivities.insert(END,'5.0')

    EntryLostEffort.insert(END,'2.0')

    EntryChooseGroup.insert(END,'Cresceu')

    EntryLayerName.insert(END,"Todos")
    EntryInputFile.insert(END, "./DataBase/DataBase.db")
    ####################################################################################################################################################################################

    Label(root, text="Número de Tarefas").grid(row=0)

    Label(root, text="Nota Máxima").grid(row=1)
    Label(root, text="Esforço Máximo").grid(row=2)
    Label(root, text="Eficiência Máxima").grid(row=3)
    Label(root, text="Desempenho Máximo").grid(row=4)

    Label(root, text="Penalidade Por Não Fazer").grid(row=5)
    Label(root, text="Bonus Por Acerto").grid(row=6)
    Label(root, text="Penalidade Por Errar").grid(row=7)
    Label(root, text="Bonus Por Refazer").grid(row=8)

    Label(root, text="Ruído do Esforço").grid(row=9)
    Label(root, text="Ruído do Desempenho").grid(row=10)
    Label(root, text="Ruído da Eficiência").grid(row=11)
    Label(root, text="Ruído da Tarefa").grid(row=12)
    Label(root, text="Ruído de Acertos").grid(row=13)

    Label(root, text="Importancia Do Esforço e Desempenho Para a Performance").grid(row=14)

    Label(root, text="Nº Máximo de Atividades por Tarefa").grid(row=15)
    Label(root, text="Nº Médio de Atividades Por Tarefa").grid(row=16)

    Label(root, text="Perda de Vontade a Cada Atividade").grid(row=17)

    Label(root, text="Alunos que Cresceram ou Decresceram").grid(row=18)

    Label(root, text="Gráficos dos Alunos, ou Turma ou Escola...").grid(row=19)
    Label(root, text="Nome do Arquivo de Entrada").grid(row=20)

    def UpdateValues():
        global NumHomeworks
        global MaxScore
        global MaxEffort
        global MaxEfficiency
        global MaxPerformance
        global TotalFailBonus
        global SuccessBonus
        global FailBonus
        global RedoBonus
        global PerformanceTemp
        global EffortTemp
        global EfficiencyTemp
        global DoTemp
        global RightTemp
        global RedoTemp
        global PerformanceCoef
        global MaxActivities
        global MeanActivities
        global LostEffort
        global ChoosenGroup
        global LayerName
        global InputFile

        NumHomeworks    = int(EntryNumHomeworks.get())

        MaxScore        = float(EntryMaxScore.get())
        MaxEffort       = float(EntryMaxEffort.get())
        MaxEfficiency   = float(EntryMaxEfficiency.get())
        MaxPerformance  = float(EntryMaxPerformance.get())


        TotalFailBonus  = float(EntryTotalFailBonus.get())
        SuccessBonus    = float(EntrySuccessBonus.get())
        FailBonus       = float(EntryFailBonus.get())
        RedoBonus       = float(EntryRedoBonus.get())

        PerformanceTemp = float(EntryPerformanceTemp.get())
        EffortTemp      = float(EntryEffortTemp.get())
        EfficiencyTemp  = float(EntryEfficiencyTemp.get())
        DoTemp          = float(EntryDoTemp.get())
        RightTemp       = float(EntryRightTemp.get())
        RedoTemp        = float(EntryRedoTemp.get())

        PerformanceCoef = float(EntryPerformanceCoef.get())

        MaxActivities   = float(EntryMaxActivities.get())
        MeanActivities  = float(EntryMeanActivities.get())

        LostEffort      = float(EntryLostEffort.get())

        ChoosenGroup    = str(EntryChooseGroup.get())

        LayerName       = "'"+EntryLayerName.get()+"'"
        InputFile       = EntryInputFile.get()

    def Reset():
        global subplot
        global subplot1
        global subplot2
        global subplot3
        global figure
        global figure1
        global figure2
        global figure3

        figure = Figure(figsize=(5, 4), dpi=100)
        subplot = figure.add_subplot(1, 1, 1)
        figure1 = Figure(figsize=(5, 4), dpi=100)
        subplot1 = figure1.add_subplot(1, 1, 1)
        figure2 = Figure(figsize=(5, 4), dpi=100)
        subplot2 = figure2.add_subplot(1, 1, 1)
        figure3 = Figure(figsize=(5, 4), dpi=100)
        subplot3 = figure3.add_subplot(1, 1, 1)

    def PlotAverage():
        global subplot
        global subplot1
        global subplot2
        global subplot3
        global figure
        global figure1
        global figure2
        global figure3

        t=[]
        Effi=[]
        Effo=[]
        Perf=[]
        Mean=[]
        LayerData=[]

        Connection = None
        try:
            Connection = sqlite3.connect(InputFile)
            Cursor = Connection.cursor()
        except Error as e:
            print(e)

        #UserId = np.asarray(SqlCommand(Connection,"""SELECT DISTINCT User_id from Desempenhos""")).flatten()
        Group = (np.asarray(SqlCommand(Connection,"SELECT Camada from Grupos "))).flatten()

        if LayerName == "'Todos'":
            UserIds = (np.asarray(SqlCommand(Connection,"SELECT id from Input"))).flatten()
        else:
            for i in range(0,len(Group)):
                try:
                    if SqlCommand(Connection,"SELECT "+Group[i]+" from Input WHERE "+Group[i]+"="+LayerName) != []:
                        Layer = Group[i]
                except:
                    continue

            UserIds = (np.asarray(SqlCommand(Connection,"SELECT id from Input WHERE "+Layer+"="+LayerName))).flatten()

        t=SqlCommand(Connection,"""SELECT Tempo from Desempenhos WHERE User_id="""+str(UserIds[0]))

        for i in range(0,len(UserIds)):
            Perf.append((SqlCommand(Connection,"SELECT Desempenho from Desempenhos WHERE User_id="+str(UserIds[i]))))
            Effi.append((SqlCommand(Connection,"SELECT Eficiência from Desempenhos WHERE User_id="+str(UserIds[i]))))
            Effo.append((SqlCommand(Connection,"SELECT Esforço from Desempenhos WHERE User_id="+str(UserIds[i]))))

        x=np.asarray(t).flatten()
        y=sum(np.asarray(Effi)).flatten()/len(UserIds)
        z=sum(np.asarray(Effo)).flatten()/len(UserIds)
        l=sum(np.asarray(Perf)).flatten()/len(UserIds)

        subplot.plot(x,y)
        subplot1.plot(x,z)
        subplot2.plot(x,l)
        subplot3.plot(y,z)

        childWindows = Toplevel(root)

        subplot.set_ylim(0,100)
        subplot.set_xlabel('Tempo')
        subplot.set_ylabel('Eficiência')
        canvas = FigureCanvasTkAgg(figure, childWindows)
        canvas.get_tk_widget().grid(row=0, column=2, rowspan=18)


        subplot1.set_ylim(0,100)
        subplot1.set_xlabel('Tempo')
        subplot1.set_ylabel('Esforço')
        canvas1 = FigureCanvasTkAgg(figure1, childWindows)
        canvas1.get_tk_widget().grid(row=0, column=3, rowspan=18)


        subplot2.set_ylim(0,100)
        subplot2.set_xlabel('Tempo')
        subplot2.set_ylabel('Desempenho')
        canvas2 = FigureCanvasTkAgg(figure2, childWindows)
        canvas2.get_tk_widget().grid(row=19, column=2, rowspan=18)


        subplot3.set_ylim(0,100)
        subplot3.set_xlim(0,100)
        subplot3.set_xlabel('Eficiência')
        subplot3.set_ylabel('Esforço')
        canvas3 = FigureCanvasTkAgg(figure3, childWindows)
        canvas3.get_tk_widget().grid(row=19, column=3, rowspan=18)

    def PlotAll():
        global subplot
        global subplot1
        global subplot2
        global subplot3
        global figure
        global figure1
        global figure2
        global figure3

        t=[]
        Effi=[]
        Effo=[]
        Perf=[]
        Mean=[]
        LayerData=[]

        #InputFile = EntryInputFile.get()

        Connection = None
        try:
            Connection = sqlite3.connect(InputFile)
            Cursor = Connection.cursor()
        except Error as e:
            print(e)

        #UserId = np.asarray(SqlCommand(Connection,"""SELECT DISTINCT User_id from Desempenhos""")).flatten()
        Group = (np.asarray(SqlCommand(Connection,"SELECT Camada from Grupos "))).flatten()

        if LayerName == "'Todos'":
            Layer = ""
            UserIds = (np.asarray(SqlCommand(Connection,"SELECT id from Input"))).flatten()
        else:
            for i in range(0,len(Group)):
                try:
                    if SqlCommand(Connection,"SELECT "+Group[i]+" from Input WHERE "+Group[i]+"="+LayerName) != []:
                        Layer = Group[i]
                except:
                    continue

            UserIds = (np.asarray(SqlCommand(Connection,"SELECT id FROM Input WHERE "+Layer+"="+LayerName))).flatten()

        t=SqlCommand(Connection,"""SELECT Tempo from Desempenhos WHERE User_id="""+str(UserIds[0]))
        x=np.asarray(t).flatten()

        for i in range(0,len(UserIds)):
            performance = (SqlCommand(Connection,"SELECT Desempenho FROM Desempenhos WHERE User_id="+str(UserIds[i])))

            performance = np.asarray(performance).flatten()

            avgDerivative = 0
            for j in range(0,len(performance)-1):
                avgDerivative = avgDerivative + (performance[j+1] - performance[j])/(len(performance)-1)

            if avgDerivative>0:
                Cursor.execute("INSERT INTO Classificações(User_Id,Classificação) VALUES(?,?);",(str(UserIds[i]),"Cresceu"))
                Connection.commit()

            if avgDerivative<0:
                Cursor.execute("INSERT INTO Classificações(User_Id,Classificação) VALUES(?,?);",(str(UserIds[i]),"Decresceu"))
                Connection.commit()

        if ChoosenGroup=="Cresceu":
            UserIds = np.asarray(SqlCommand(Connection,"SELECT User_Id FROM Classificações WHERE Classificação='Cresceu'")).flatten()
            for i in range(0,len(UserIds)):
                l = (SqlCommand(Connection,"SELECT Desempenho from Desempenhos WHERE User_id="+str(UserIds[i])))
                y = (SqlCommand(Connection,"SELECT Eficiência from Desempenhos WHERE User_id="+str(UserIds[i])))
                z = (SqlCommand(Connection,"SELECT Esforço from Desempenhos WHERE User_id="+str(UserIds[i])))

                Connection.commit()

                subplot.plot(x,y)
                subplot1.plot(x,z)
                subplot2.plot(x,l)
                subplot3.plot(y,z)

        if ChoosenGroup=="Decresceu":
            UserIds = np.asarray(SqlCommand(Connection,"SELECT User_Id FROM Classificações WHERE Classificação='Decresceu'")).flatten()
            for i in range(0,len(UserIds)):
                l = (SqlCommand(Connection,"SELECT Desempenho from Desempenhos WHERE User_id="+str(UserIds[i])))
                y = (SqlCommand(Connection,"SELECT Eficiência from Desempenhos WHERE User_id="+str(UserIds[i])))
                z = (SqlCommand(Connection,"SELECT Esforço from Desempenhos WHERE User_id="+str(UserIds[i])))

                Connection.commit()

                subplot.plot(x,y)
                subplot1.plot(x,z)
                subplot2.plot(x,l)
                subplot3.plot(y,z)

        if ChoosenGroup=="Todos":
            UserIds = np.asarray(SqlCommand(Connection,"SELECT User_Id FROM Classificações")).flatten()
            for i in range(0,len(UserIds)):
                l = (SqlCommand(Connection,"SELECT Desempenho from Desempenhos WHERE User_id="+str(UserIds[i])))
                y = (SqlCommand(Connection,"SELECT Eficiência from Desempenhos WHERE User_id="+str(UserIds[i])))
                z = (SqlCommand(Connection,"SELECT Esforço from Desempenhos WHERE User_id="+str(UserIds[i])))

                Connection.commit()

                subplot.plot(x,y)
                subplot1.plot(x,z)
                subplot2.plot(x,l)
                subplot3.plot(y,z)


        childWindows = Toplevel(root)

        subplot.set_ylim(0,100)
        subplot.set_xlabel('Tempo')
        subplot.set_ylabel('Eficiência')
        canvas = FigureCanvasTkAgg(figure, childWindows)
        canvas.get_tk_widget().grid(row=0, column=2, rowspan=18)


        subplot1.set_ylim(0,100)
        subplot1.set_xlabel('Tempo')
        subplot1.set_ylabel('Esforço')
        canvas1 = FigureCanvasTkAgg(figure1, childWindows)
        canvas1.get_tk_widget().grid(row=0, column=3, rowspan=18)


        subplot2.set_ylim(0,100)
        subplot2.set_xlabel('Tempo')
        subplot2.set_ylabel('Desempenho')
        canvas2 = FigureCanvasTkAgg(figure2, childWindows)
        canvas2.get_tk_widget().grid(row=19, column=2, rowspan=18)


        subplot3.set_ylim(0,100)
        subplot3.set_xlim(0,100)
        subplot3.set_xlabel('Eficiência')
        subplot3.set_ylabel('Esforço')
        canvas3 = FigureCanvasTkAgg(figure3, childWindows)
        canvas3.get_tk_widget().grid(row=19, column=3, rowspan=18)


    StartButton = Button(root, text = "Iniciar",command=Simu)
    StartButton.grid(row=21)

    UpdateButton = Button(root, text = "Atualizar Valores",command=UpdateValues)
    UpdateButton.grid(row=22)

    GenFigButton = Button(root, text = "Resetar", command=Reset)
    GenFigButton.grid(row=23)

    PlotButton = Button(root, text = "Plotar Média", command=PlotAverage)
    PlotButton.grid(row=24)

    PlotButton = Button(root, text = "Plotar Todos", command=PlotAll)
    PlotButton.grid(row=25)

    Reset()


    root.update()
    root.mainloop()

####################################################################################################################################################################################

#Declaring

NofActivities = [1.0,1.0,1.0]
Quality = 0.0

####################################################################################################################################################################################
#Functions
def Truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


####################################################################################################################################################################################


class Profile:
    def __init__(self, Name, Efficiency, Effort, Performance, **kwargs):
        self.__dict__.update(kwargs)
        self.Name = Name
        self.Efficiency = Efficiency
        self.Effort = Effort
        self.Performance = Performance


        self.Did = [0,0,0]
        self.Right = [0,0,0]
        self.Redo = [0,0,0]


    def ShowName(self):
        print("Nome: ",self.Name)

    def ShowEfficiency(self):
        return(self.Efficiency)

    def ShowEffort(self):
        return(self.Effort)

    def ShowPerformance(self):
        return(self.Performance)


    ####################################################################################################################################################################################

    def DoHomework(self):

        DoThreshold = [50.0,50.0,50.0]
        RightThreshold = [50.0,60.0,70.0]
        RedoThreshold = [60.0,70.0,75.0]

        for k in range(0,3):

            self.Did[k] = 0.0
            self.Right[k] = 0.0
            self.Redo[k] = 0.0
            j=0


            NofActivities[k] = int(rayleigh(MeanActivities))
            while(NofActivities[k] < 1.0 or NofActivities[k] > MaxActivities):
                NofActivities[k] = int(rayleigh(MeanActivities))

            DoOrNot = DoTemp * normal(0.0,1.0) + self.Effort
            while(DoOrNot<0.0 or DoOrNot>100.0):
                DoOrNot = DoTemp * normal(0.0,1.0) + self.Effort

            if(DoOrNot >= DoThreshold[k]):
                for i in range(0,NofActivities[k]):
                    DoOrNot = DoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort
                    while(DoOrNot<0.0 or DoOrNot>100.0):
                        DoOrNot = DoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort

                    RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort
                    while(RedoOrNot<0.0 or RedoOrNot>100.0 ):
                        RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort

                    if(DoOrNot >= DoThreshold[k]):
                        self.Did[k] = self.Did[k] + 1.0

                        RightOrNot = RightTemp * normal(0.0,1.0) + self.Efficiency
                        while(RightOrNot<0.0 or RightOrNot>100.0):
                            RightOrNot = RightTemp * normal(0.0,1.0) + self.Efficiency

                        if(RightOrNot >= RightThreshold[k]):
                            self.Right[k] = self.Right[k] + 1.0

                            RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort
                            while(RedoOrNot<0.0 or RedoOrNot>100.0 ):
                                RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort

                            while(RedoOrNot >= RedoThreshold[k] and j<5):
                                j=j+1
                                RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort
                                while(RedoOrNot<0.0 or RedoOrNot>100.0 ):
                                    RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort
                                self.Redo[k] = self.Redo[k] + 1.0
                                RightOrNot = RightTemp * normal(0.0,1.0) + self.Efficiency
                                while(RightOrNot<0.0 or RightOrNot>100.0):
                                    RightOrNot = RightTemp * normal(0.0,1.0) + self.Efficiency

                                if(RightOrNot >= RightThreshold[k]):
                                    self.Right[k] = self.Right[k] + 1.0
                            j=0

                        else:
                            RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort
                            while(RedoOrNot<0.0 or RedoOrNot>100.0 ):
                                RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort

                            while(RedoOrNot >= RedoThreshold[k] and j<5):
                                j=j+1
                                RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort
                                while(RedoOrNot<0.0 or RedoOrNot>100.0 ):
                                    RedoOrNot = RedoTemp * normal(0.0,1.0) + self.Effort - i * LostEffort
                                self.Redo[k] = self.Redo[k] + 1.0
                                RightOrNot = RightTemp * normal(0.0,1.0) + self.Efficiency
                                while(RightOrNot<0.0 or RightOrNot>100.0):
                                    RightOrNot = RightTemp * normal(0.0,1.0) + self.Efficiency

                                if(RightOrNot >= RightThreshold[k]):
                                    self.Right[k] = self.Right[k] + 1.0
                            j=0
    ####################################################################################################################################################################################

    def IterateEfficiency(self):

        RandVal = EfficiencyTemp * normal(0.0, 1.0)

        self.Efficiency = self.Efficiency + RandVal
        if(self.Efficiency > MaxEfficiency):
            self.Efficiency = MaxEfficiency
        if(self.Efficiency < 1.0):
            self.Efficiency = 1.0

    ####################################################################################################################################################################################

    def IterateEffort(self,Quality):
        #Param = list(self.__dict__.values())
        #print(Param[0][1])

        global NofActivities

        RandVal = EffortTemp * normal(0.0, 1.0)

        self.Effort = self.Effort + Quality + RandVal

        if(self.Did != 0.0):
            for k in range(0,3):
                self.Effort = self.Effort + (1.0/NofActivities[k]) * (self.Right[k] * SuccessBonus + self.Redo[k] * RedoBonus + (self.Did[k] - self.Right[k])*FailBonus)
                if(self.Effort > MaxEffort):
                    self.Effort = MaxEffort
                if(self.Effort < 1.0):
                    self.Effort = 1.0


        if(self.Did == 0.0):
            self.Effort = self.Effort + TotalFailBonus + RandVal
            if(self.Effort > MaxEffort):
                self.Effort = MaxEffort
            if(self.Effort < 1.0):
                self.Effort = 1.0
    ####################################################################################################################################################################################

    def IteratePerformance(self):
        EffAndEff = PerformanceCoef*(self.Effort+self.Efficiency)

        if(EffAndEff > MaxPerformance):
            EffAndEff = MaxPerformance
        if(EffAndEff < 1.0):
            EffAndEff = 1.0

        RandVal = PerformanceTemp * normal(0.0,1.0) + EffAndEff
        while(RandVal<0.0 or RandVal>MaxPerformance):
            RandVal = PerformanceTemp * normal(0.0,1.0) + EffAndEff

        self.Performance = RandVal

####################################################################################################################################################################################
#def Classify():
#    d = SqlCommand(Connection,"SELECT Desempenho from Desempenhos WHERE User_id="+str(UserIds[i]))
####################################################################################################################################################################################

def ConnectToSql(datafile,i):
    Connection = None
    try:
        Connection = sqlite3.connect(datafile)
        Cursor = Connection.cursor()
    except Error as e:
        print(e)

    if i==1:
        return Connection
    else:
        return Cursor
####################################################################################################################################################################################

def UpdatePerformance(Connection, Row):

    sql = ''' INSERT INTO Desempenhos(User_id,Nome,Tempo,Eficiência,Esforço,Desempenho)
              VALUES(?,?,?,?,?,?) '''
    Cursor = Connection.cursor()
    Cursor.execute(sql, Row)

####################################################################################################################################################################################

def UpdateJournal(Connection, Row):
    sql = ''' INSERT INTO Desempenhos(User_id,Acontecimento)
              VALUES(?,?) '''
    Cursor = Connection.cursor()
    Cursor.execute(sql, Row)

####################################################################################################################################################################################

def ReportHomework(Connection, Row):
    sql = ''' INSERT INTO Tarefas(User_id, Fez_Obrigatória, Fez_Obrigatória_Corretamente, Refez_Obrigatória, Fez_Recomendada, Fez_Recomendada_Corretamente, Refez_Recomendada, Fez_Eletiva, Fez_Eletiva_Corretamente, Refez_Eletiva) VALUES(?,?,?,?,?,?,?,?,?,?) '''

    Cursor = Connection.cursor()
    Cursor.execute(sql, Row)
    #return Cursor.lastrowid

####################################################################################################################################################################################
def SqlCommand(Connection, Command):
    Cursor = Connection.cursor()
    Cursor.execute(Command)

    Rows = Cursor.fetchall()

    return Rows
####################################################################################################################################################################################
def FindColumnsWithString(Connection, String):
    Column = []

    Query = SqlCommand(Connection,"""PRAGMA table_info(Input);""")

    for j in Query:
        for s in j:
            Column.append(s)

    NoNumbers = [str(x) for x in Column if not isinstance(x, int) and not isinstance(x, float)]

    FilteredQuery = [s for s in NoNumbers if String in s]

    return FilteredQuery

####################################################################################################################################################################################
def Simu():
    Connection = ConnectToSql(InputFile,1)
    Cursor = ConnectToSql(InputFile,2)

    QualityList = []

    Quality = 0

    global NofActivities

    print("Starting")

    with Connection:
        ReadSqliteQuery = """select * from input"""
        Cursor.execute(ReadSqliteQuery)
        Records = Cursor.fetchall()

        Cursor.execute("""select * from Desempenhos_Iniciais""")
        Data = Cursor.fetchall()

        UserId = (np.asarray(SqlCommand(Connection,"""SELECT DISTINCT id from Input"""))).flatten()

        QualityString = FindColumnsWithString(Connection, "Qualidade")

        for i in range(0,len(QualityString)):
            Quality = Quality + np.asarray(SqlCommand(Connection,"""SELECT """ + QualityString[i] + """ from Input"""))
        Quality = Quality.flatten()

        for i in range(0,len(UserId)):
            Alumni = Profile(Name=Data[i][1], Effort=Data[i][3], Efficiency=Data[i][4], Performance=Data[i][5])

            for j in range(0,NumHomeworks):
                Alumni.DoHomework()
                Alumni.IterateEfficiency()
                Alumni.IterateEffort(Quality[i])
                Alumni.IteratePerformance()

                UpdatePerformance(Connection,(Data[i][0],Data[i][1],j,Alumni.Efficiency,Alumni.Effort,Alumni.Performance))

                #UpdateJournal(Connection,(Desempenhos[i][0],""))

                ReportHomework(Connection,(Data[i][0], Alumni.Did[0], Alumni.Right[0], Alumni.Redo[0], Alumni.Did[1], Alumni.Right[1], Alumni.Redo[1], Alumni.Did[2], Alumni.Right[2], Alumni.Redo[2]))
            #Plotting(Connection)

        print("Finished")


        #SqlCommand(Connection,"""""")#Fazer um comando aqui que faça as médias dos alunos para achar o desempenho da escola.

TkinterGui()





#Talpessoa(regiao, - , Escola)

#Resultado agrupado por dia
#E visão extensiva das atividades
#Repetiu ou não o exercício
#nao fazer ele retroalimentado ou usar Langevin
#Grafico do esforço vs performance mediado
#Fazer varias atividades por lição de casa
#Intensidade de trabalho?
#sortear alunos com tendencia que defina o comportamento final da sala
#testar se a evolução dos resultados das regiões, escolas, series, ...
#H=escola cresce + regiao cresce + aluno vai mal
#    def load(nivel, parametro):
#        if nivel == 'escola':
#            load('cidade', parametro)



#Acertou, repete o exercício
#Errou, repetiu?, acertou quando
#Tarefa eletiva prob menor
#Tarefa voluntaria menor ainda
#Temperatura baixa
#"Comportamento a la Gaussiana"
#Django - interface grafica - fazer a interface ate quinta

####Pra proxima reuniao
#Pra cada Camada e Qualidade, usar uma lista
# Definir data de Inicial e Final
#Linha de tempo
#Variação das aitividades (eletiva obrigatŕia e recomendada)
#Turma  tem que estar pronta
#Comporatmento melhorando ou piorando ou ficando igual definido pelo usuário que da input
#

#Fazer um dropdown para não precisar mostrar todas os inputs
#Simplificar os valores como barrinhas

#Consertar o négocio de plotar médias ou todos, na segunda vez que eu aperto em plotar médias depois de plotar todos, o botão de plotar médias também plota todos.. (01-03-20)




"""
for Row in Reader:
            LineCount = LineCount + 1
            for Index in Row:
                if "Q" in Index:
                    Quality = Quality + float(Row[Index])
                if Index !='Esforço' and Index !='Eficiência' and Index!='Desempenho' and "Q" not in Index:
                    String = String +" "+ Row[Index]
            StringGroup.append(String)
            String = ""

Alumni = Profile(Name=Row['Nome'], Effort=float(Row['Esforço']), Efficiency=float(Row['Eficiência']), Performance=float(Row['Desempenho']))

            for i in range(0,NumHomeworks):
                Alumni.DoHomework()
                Alumni.IterateEfficiency()
                Alumni.IterateEffort()
                Alumni.IteratePerformance()

                if(i==0):
                    Line[LineCount].append([StringGroup[LineCount],"Tempo","Eficiência","Esforço","Desempenho","Fez Obrigatória","Fez Obrigatória Corretamente","Refez Obrigatória","Fez Recomendada","Fez Recomendada Corretamente","Refez Recomendada","Fez Eletiva","Fez Eletiva Corretamente","Refez Eletiva"])

                    Line[LineCount].append([" ",i,Truncate(Alumni.Efficiency,2),Truncate(Alumni.Effort,2),Truncate(Alumni.Performance,2),Alumni.Did[0],Alumni.Right[0],Alumni.Redo[0],Alumni.Did[1],Alumni.Right[1],Alumni.Redo[1],Alumni.Did[2],Alumni.Right[2],Alumni.Redo[2]])


            Quality = 0.0
            Line.append([])

        Rows = []
        for j in range(0,NumHomeworks):
            for i in range(0,LineCount):
                Rows = Rows + Line[i][j]
            Writer.writerow(Rows)
            Rows = []

    print("finished")

"""
