import random
import math as Math
import sys

class blowcript():
    def __init__(self,key,message):
        self.thritytwoones = ((1<<32)-1)
        self.eightones = ((1<<8)-1)
        self.p=[]
        self.s=[]
        self.s1=[]
        self.s2=[]
        self.s3=[]
        self.s0=[]
        key=int(key)
        self.key=int(key)
        message=int(message)
        for i in range(256):
            self.s0.append(Math.floor(random.random()*2**31))
            self.s1.append(Math.floor(random.random()*2**31))
            self.s2.append(Math.floor(random.random()*2**31))
            self.s3.append(Math.floor(random.random()*2**31))
        for i in range(18):
            buff = (key%(2**32)) & self.thritytwoones
            if buff != 0:
                self.p.append(buff)
            else:
                key=self.key
                buff = key & self.thritytwoones
                self.p.append(buff)
            key=key>>32
        right = message & self.thritytwoones
        left = (message>>32) & self.thritytwoones
        print(self.round(left,right))
        self.reverse()
        message = self.round(left,right)
        right = message & self.thritytwoones
        left = (message>>32) & self.thritytwoones
        #print(self.round(left,right))

    def reverse(self):
        for i in range(9):
            temp = self.p[i]
            self.p[0]= self.p[-(i+1)]
            self.p[-(i+1)]=temp

    def sbox(self,n,val):
        if n==3:
            return self.s3[val]
        if n==2:
            return self.s2[val]
        if n==1:
            return self.s1[val]
        if n==0:
            return self.s0[val]

    def round(self,left,right,n=0):
        if n==16:
            rig = right ^ self.p[16]
            lef = left ^ self.p[17]
            return (lef<<32) + rig
        else:
            temp=self.fun(left,self.p[n])
            newleft=temp^right
            newright=left
            return self.round(newleft,newright,n+1)

    def fun(self,left,p):
        x=left^p
        s3 = self.sbox(3,self.eightones&x)
        x=x>>8
        s2 = self.sbox(2,self.eightones&x)
        x=x>>8
        s1 = self.sbox(1,self.eightones&x)
        x=x>>8
        s0 = self.sbox(0,self.eightones&x)
        s0 = (s0+s1) % (2**31)
        s0 = s0 ^ s2
        s0 = (s0 + s3) % (2**31)
        return s0

        
print(sys.argv[1],sys.argv[2])
obj = blowcript(sys.argv[1],sys.argv[2])




