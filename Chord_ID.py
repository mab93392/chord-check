import numpy as np
from chord import Chord
from synth_detect import synth_detect
from type_weight import type_weight
from type_act import type_act
from key_weight import key_weight
from key_act import key_act
from inv_act import inv_act
from inv_weight import inv_weight
from table_control import table_control
from test_case import test_case


class Chord_ID:
    
    def __init__(self):
        chord = Chord()                # this class generates a simulated chord w/
        data = chord.final_out()       # randomly selected type, key, and inversion
        # data = test_case()           # used for a known chord data set
        # self.key = data[0]
        # self.type = data[1]
        # self.inv = data[2]
        # self.input = np.reshape(data[3],(len(data[3]),1))
        self.key = data[2]
        self.type = data[3]
        self.inv = data[4]
        self.input = np.reshape(synth_detect(data[0],44100)[1],(882,1))

# intializes the comparison values for the cost function
        self.a1 = np.reshape(key_act(self.key + 1)[0][1:],(11,1))
        self.a2 = np.reshape(type_act(self.type + 1)[0][1:],(27,1))
        self.a3 = np.reshape(inv_act(self.inv + 1)[0][1:],(11,1))

# initializes the wieghts for the network
        self.w1 = key_weight()
        self.w2 = type_weight()
        self.w3 = inv_weight()

# activation function
    def sig(self,x):
        return np.power(1+np.exp(np.multiply(-1,x)),-1)

# derivative of activation function         
    def sigd(self,x):
        return x*(1-x)


# gradient descent algorithm   
# its essentially broken into two layers 
# the first deals with the gradient descent for key and inversion and the second 
# deals with the chord type 
    def learn(self):    
        # key and inversion layer
        for k in range(0,2000):    
            x1 = np.dot((self.w1),self.input) # key activation input
            x3 = np.dot(self.w3,self.input) # inversion activation input
            y1 = self.sig(x1) # key activation
            y3 = self.sig(x3) # inversion activation
            dy1 = self.sigd(x1) # derivative of key activation 
            dy3 = self.sigd(x3) # derivative of inversion activation
            dc1 = 2*(self.a1-y1) # derivatives of cost functions
            dc3 = 2*(self.a3-y3)
            adj01 = dc1*dy1 # continuation of product rule
            adj03 = dc3*dy3
            
            
            for i in range(0,11):
                adji1 = []
                adji3 = []
                
                for j in range(0,882):
                    v1 = adj01[i]*self.w1[i][j]*0.0001 # completion of product rule for the dc/dw
                    v3 = adj03[i]*self.w3[i][j]*0.0001
                    adji1 = np.append(adji1,v1) # builds array for adjustment values to weights
                    adji3 = np.append(adji3,v3)
                # forms matrix of adjustment values
                if i == 0:
                    adj1 = adji1
                    adj3 = adji3
                else: 
                    adj1 = np.vstack((adj1,adji1))
                    adj3 = np.vstack((adj3,adji3))
            
            self.w1 = self.w1-adj1
            self.w3 = self.w3-adj3
        y13 = np.append(y1,y3,0) # used as "detection" the type layer
        


        # type layer
        for k in range(0,2000): 
            
            x2 = np.dot((self.w2),y13) # input for type activation
            y2 = self.sig(x2) # activation function for type 
            dy2 = self.sigd(x2) # derivative of type activation function
            dc2 = 2*(self.a2-y2) # derivative of type cost function
            adj0 = dc2*dy2 # continuation of product rule
        
            for i in range(0,27):
                adji = []
                for j in range(0,22):
                    v = adj0[i]*self.w2[i][j]*0.001
                    v2 = np.round(v,2)
                    adji = np.append(adji,v2)
                if i == 0:
                    adj = adji
                else: 
                    adj = np.vstack((adj,adji))
            
            self.w2 = self.w2-adj
        

            


      
        

            
        
        
        
        
        







