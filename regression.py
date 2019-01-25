# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

numsteps = 0

#Counting Steps Function
def steps(inp):
    global numsteps
    numsteps+=inp


#The parsing of the data happens here.
def Parsing(data):
    try:
        for i in range(len(data)):
            data[i] = data[i].replace(" ","")
            data[i] = data[i].replace("(","")
            data[i] = data[i].replace("\n","")
            data[i] = data[i].replace(")","")
            data[i] = data[i].split(",")
            x.append(float(data[i][0]))
            y.append(float(data[i][1]))
        return x,y
    except:
        print("Make sure the text file has ordered pair in newlines and separated by commas.\n")
        raise SystemExit 


'''
The error function, this returns the summation of every point and their vertical distance from
our datapoints squared. 
'''
def error(x,y,m,b):
    error = 0
    for i in range(len(x)):
        error+=(y[i]-m*(x[i])-b)**2
        steps(8)
        
    return error



'''
Dynamic Step Size.
Gradient Descent can be slow if the stepsize is short.Can overshoot if the stepsize is big.
Dynamic step size tries to make the step size as big as possible.Since the error function is convex,
the gradient constantly decreases.
'''
def DynamicDelta(x0,y0,m,b,delta):
    fm,fb = gradient(x,y,m,b,delta)
    fm2,fb2 = gradient(x,y,m-fm,fb-b,delta)
    steps(16)
    while( np.sqrt((fm2**2+fm2**2)) > np.sqrt((fm**2+fb**2))):                  #Follows the gradient until the next gradient is less than the previous one.
        fm,fb = gradient(x,y,m,b,delta)
        fm2,fb2 = gradient(x,y,m-fm,fb-b,delta)
        delta/=2                                                                #Starts with a big step size,narrows it down by a factor of 0.5 every iteration.
        steps(27)
    return delta
    

'''
Approximates the gradient.
Doesn't assume the gradient to be the known error function, thus its scalable.
'''
def gradient(x0,y0,m,b,delta):
    fm = (error(x0,y0,m+delta,b) - error(x0,y0,m,b))
    fb = (error(x0,y0,m,b+delta) - error(x0,y0,m,b))
    steps(9)
    return fm,fb
    

'''Error Reduction
Stops where it thinks we have done enough iterations.
'''
def ErrorReduce(x,y,m,b,n,delta,flag):
    iterations = 0
    M = []
    B = []
    while(iterations<n):
        Error.append(error(x,y,m,b))
        fm,fb = gradient(x,y,m,b,delta)
        m-=fm
        b-=fb
        M.append(m)
        B.append(b)

        if(flag == False):
            delta = DynamicDelta(x,y,m,b,1)
        if(len(Error)>3):
            if (np.abs(Error[iterations]-Error[iterations-1])<0.1):             #If the error stops working.
                break
             
        iterations+=1
        
    steps(18*iterations)

    return m,b,M,B,Error,iterations


#All the graphing is done here. 
def Graph(x,y,m,b,M,B,t1,ax1,stop,Error):
    ax1.set(ylabel="Error",xlabel="Iterations")
    ax1.set_title("Iterations")
    ax2.set(ylabel="Evolution of Algorithm")
    if(stop==False):
        plt.plot(x, y,'go',markersize = 2)
    steps(11)

    plt.plot(t1,m*t1+b , 'b.-',markersize = 0.5)
    ax3.set(xlabel="Final Fit y="+str(m)+"x + "+str(b))
    ax1.set_ylim(Error[len(Error)-1],Error[0])                              #Scales the plot accordingly
    ax1.plot(Error,'b.-')
    
    M = np.asarray(M)
    B = np.asarray(B)
    ax2.set_ylim(np.min(M)-0.01,np.max(M)+0.01 )                                      #Scales the plot accordingly
    ax2.set_xlim(np.min(B)-0.01,np.max(B)+np.max(B)/10+0.01 )
    ax1.set_yscale('linear')
    ax2.scatter(B,M,c=B*2,cmap=plt.cm.get_cmap('winter_r'),s=10)
    ax2.plot(B[len(B)-1],M[len(B)-1],'ro')
    


    

    
#Parsing
try:    
    text_file = open('data.txt','r')
    file_data = text_file.readlines()
    text_file.close()                                                           #close the file.       
    # Create a copy of the file_data to work on 
    numbers = file_data
    
except:
    print("Please have a file called data.txt in the directory with ordered pairs.")
    raise SystemExit
x = []
y = []

x,y = Parsing(numbers)




#Initializtions
iterations = 0                                                  
m = 0                                                                       #Start from m = 0, b = 0 as initial guess.
b = 0

M = []
M.append(m)
B = []
B.append(b)
Error = []


#Graphing Initialization
fig, (ax1, ax2,ax3) = plt.subplots(3,sharey=False,sharex=False,figsize=(10,7))
t1 = np.arange( min(x) , max(x), 0.1)


input("This program will do a line of best fit on the ordered pairs of data.txt file.\nPlease Keep a data.txt file on the program directory with ordered co-ordinates.\nPress Enter to Continue\n")

#Computes the initial stepsize, if the user chooses fixed size, this stays put for the rest of the program.
delta = DynamicDelta(x,y,m,b,0.1)


flag = None
while(flag == None):
    inp = input("Enter a for fixed step size to reduce error, enter q if you prefer dynamic step size.\n")
    if ( inp =="a" or inp == "A"):
        try:
            n = int(input("Enter the amount of times you want error reducing algorithm to run."))
            flag = True
        except:
            n = int(input("Enter the amount of times you want error reducing algorithm to run."))
            flag = False
    elif (inp == "q" or inp == 'Q'):
        n = 1000
        flag = False
        
print("Please wait as this process takes a bit time.\n")


#The main error reducing function.
m,b,M,B,Error,iterations = ErrorReduce(x,y,m,b,n,delta,flag)


#Cumulative steps that are not in the loop added in the end.
steps(86)

print("It took",numsteps,"operational steps\n")
print("Final Fit y="+str(m)+"x + "+str(b))
print("Initial Error =",str(Error[0]),". Final Error = "+str(Error[len(Error)-1]))

if(iterations == n):
    print("Number of Iterations of gradient descent to reduce the error with a step size of ",delta," is",iterations)
    print("Please wait for graphing to finish since that takes quite a lot of time too.")
else:
    print("Optimal Iterations of gradient descent to reduce the error with a step size of ",delta," is",iterations)
    print("Please wait for graphing to finish.")
    


#Graphs after printing is done to make the process faster.
Graph(x,y,m,b,M,B,t1,ax1,False,Error)

      
#After making all the plots before, it finally shows the plots.
plt.show()




