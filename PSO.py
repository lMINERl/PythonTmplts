#PSO(a.k.a Particle Swarm Optimization) uses random Position in the Cost Functions
#and by interacting Socialy and personaly the over all solution is converges to Optimum solution

import numpy as np #for matrix multiplication
from sys import float_info # for Float Max num

class cls_PSO(object):
    #Constants answers to universe and everything... just from random reserch paper
    CONST_CHI=0.729844
    CONST_PERSONAL_ACCEL=1.49618
    CONST_SOCIAL_ACCEL=1.49618
    
    #shared Variables A classes
    shrd_GlobalBestPos=[]
    shrd_GlobalBestCost=float_info.max #worst value possible 
    def __init__(self,population,variables,maxItterations):
        self.population = population # number of particles 
        self.variables =variables # number of Dimentions of the problem (how many dimentions to search for opt solution)
        self.maxItterations = maxItterations 
        self.Particles=np.random.rand(self.population,self.variables) #create n by n matrix of random positions
        self.Velocity = np.zeros(shape=(self.population,self.variables)) #create n by n matrix of Zeros as start velocity
        self.Cost=np.ones(self.population) #initial Cost of each Row of Particles
        self.PersonalBestPos=np.ones(self.variables)
        self.PerosnalBestCost=float_info.max
    
    #like the 2-D U-shaped function is the same but with any dimentions 
    #where the global minimum is always at the Zeros Position
    def fn_GetCost(self):
        self.Cost=np.sum(np.power(self.Particles,2),axis=1) 
        
    def fn_Updt_CP(self):# updates personal and global best Position and cost
        #print(sys._getframe().f_code.co_name)
        i=0
        while i < self.population:
            if self.Cost[i] < self.PerosnalBestCost:
                self.PersonalBestPos=self.Particles[i,:]
                self.PersonalBestCost=self.Cost[i]
                
            if self.Cost[i] < cls_PSO.shrd_GlobalBestCost:
                cls_PSO.shrd_GlobalBestPos=self.Particles[i,:]
                cls_PSO.shrd_GlobalBestCost=self.Cost[i]
                #print (cls_Particle.shrd_GlobalBestCost)
                
            i=i+1
            
    
    def fn_Updt_Velocity(self):#the known Formula of the Reserch Paper
        i=0
        while i<self.population:
            #prtcl.Velocity=T1+(T2*T3)+(S1*S2)
            T1=np.multiply(self.Velocity[i,:],cls_PSO.CONST_CHI)
            T2=np.multiply(np.random.rand(1,self.variables),cls_PSO.CONST_PERSONAL_ACCEL)
            T3=np.subtract(self.PersonalBestPos,self.Particles[i,:])
            S1=np.multiply(np.random.rand(1,self.variables),cls_PSO.CONST_SOCIAL_ACCEL)
            S2=np.subtract(cls_PSO.shrd_GlobalBestPos,self.Particles[i,:])
            T23=np.multiply(T2,T3)
            S12=np.multiply(S1,S2)
            add_T23_S12=np.add(T23,S12)
            self.Velocity[i,:]=np.add(T1,add_T23_S12)
            i=i+1
            
    def fn_Updt_Pos(self):
        self.Particles=np.add(self.Particles,self.Velocity)
    
    def fn_Display(self):
        print(cls_PSO.shrd_GlobalBestCost)
        
    def fn_Main(self):#main Loop or excution method
        self.fn_GetCost()
        i=0
        while i<self.maxItterations:
            self.fn_Updt_CP()
            self.fn_Updt_Velocity()
            self.fn_Updt_Pos()
            self.fn_GetCost()
            self.fn_Display()
            i=i+1
           
#initialize & execute
A=cls_PSO(10,7,100)
A.fn_Main()