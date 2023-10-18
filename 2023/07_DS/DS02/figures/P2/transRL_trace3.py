from pylab import*
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def cm2inch(value):
    return value/2.54

E=6
R=100
L=0.1
tau1=L/2/R
tau2=2*L/3/R
t1=5
t2=10
t3=15

def i(t) :
    return 0*t

def i1(t) :
    return E*(1-exp(-t*0.001/tau1))/2/R
def i2(t) :
    return E*(2+exp(-(t-t1)*0.001/tau2))/6/R
def i3(t) :
    return E*exp(-(t-t2)*0.001/tau1)/3/R

def u(t) :
    return 0*t
def u1(t) :
    return E/2*(1+exp(-t*0.001/tau1))

def u2(t) :
    return E/6*(2-0.5*exp(-(t-t1)*0.001/tau2))
def u3(t) :
    return -E/3*exp(-(t-t2)*0.001/tau1)


fig=figure(figsize=(cm2inch(18),cm2inch(7)))
subplots_adjust(bottom=0.25, right=0.95, top=0.88,left=0.1,wspace=0.3)

ts=linspace(-1,0)
ts1=linspace(0,t1)
ts2=linspace(t1,t2)
ts3=linspace(t2,t3)

fig1=subplot(111)
#plot(ts,i(ts)*1000,color='k')
plot(ts1,i1(ts1)*1000,color='k')
#plot(ts2,i2(ts2)*1000,color='k')
#plot(ts3,i3(ts3)*1000,color='k')
xlabel('$t(ms)$',fontsize=10)
ylabel('$i(mA)$',fontsize=10)
xticks(arange(-1,16,1), fontsize=10)
yticks(fontsize=10)
xlim(-1,15)
ylim(-10,35)
grid()
savefig("tracei.pdf")

fig=figure(figsize=(cm2inch(18),cm2inch(7)))
subplots_adjust(bottom=0.25, right=0.95, top=0.88,left=0.1,wspace=0.3)
fig2=subplot(111)
#plot(ts,u(ts1),color='k')
plot(ts1,u1(ts1),color='k')
##plot(ts2,u2(ts2),color='k')
##plot(ts3,u3(ts3),color='k')
xlabel('$t(ms)$',fontsize=10)
ylabel('$u(V)$',fontsize=10)
xticks(fontsize=10)
yticks(fontsize=10)

xticks(arange(-1,16,1), fontsize=10)
yticks(fontsize=10)
xlim(-1,15)
ylim(-3,7)
grid()
savefig("traceu.pdf")
show()
