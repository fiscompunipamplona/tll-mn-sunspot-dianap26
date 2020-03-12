from pylab import plot, show
from numpy import linspace,sin,cos
from pylab import loadtxt
from pylab import plot,show,xlim,ylim
x=linspace(0,10,100)
y=sin(x)
ylim(-1.1,1.1)
h=cos(x)
plot(x,y)
plot(x,h)
show()

a=open("text.dat" ,"w")
for i in range(len(x)):
     a.write("%.2f%.2f\n" % (x[i],y[i]))
     a.close()
  
b=loadtxt("text.dat",float)
print(b[:,0])
print(b[:,1])


