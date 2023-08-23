class otpgen():
    def gen(self,n):
        s=""
        for i in range(1,len(n),2):
            s+=str((int(n[i])**2))
        if(len(s)>=4):
            print(s[:4])
        else:
            print("-1")
        
    


a=otpgen()
a.gen("1234453")
