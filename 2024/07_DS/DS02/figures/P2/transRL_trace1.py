from pylab import*
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def cm2inch(value):
    return value/2.54

E=6
R=100
L=0.1
tau=L/2/R

def i(t) :
    return E*(1-exp(-t*0.001/tau))/2/R

def u(t) :
    return E/2*(1+exp(-t*0.001/tau))

fig=figure(figsize=(cm2inch(18),cm2inch(7)))
subplots_adjust(bottom=0.25, right=0.95, top=0.88,left=0.1,wspace=0.3)

ts=linspace(0,3)

fig1=subplot(121)
plot(ts,i(ts)*1000)
xlabel('$t(ms)$',fontsize=10)
ylabel('$i(mA)$',fontsize=10)
xticks(fontsize=10)
yticks(fontsize=10)
fig1.xaxis.set_minor_locator(MultipleLocator(0.5))
grid(True,which='major',ls='-.',lw=0.5)
grid(True,which='minor',lw=0.5)


fig2=subplot(122)
plot(ts,u(ts))
xlabel('$t(ms)$',fontsize=10)
ylabel('$u(V)$',fontsize=10)
xticks(fontsize=10)
yticks(fontsize=10)

fig2.xaxis.set_minor_locator(MultipleLocator(0.5))
grid(True,which='major',ls='-.',lw=0.5)
grid(True,which='minor',lw=0.5)

savefig("trace.pdf")
show()
