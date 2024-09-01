from pylab import *

def cm2inch(value):
    return value/2.54

fig=figure(figsize=(cm2inch(12),cm2inch(8)))

subplots_adjust(hspace=0.3)
subplots_adjust(bottom=0.18, right=0.95, top=0.95,left=0.1,wspace=0.3)
ylim(-0.5,5)

xticks(fontsize=10)
yticks(fontsize=10)


xlabel("$u_D(V)$",fontsize=10)
ylabel("$i_D(A)$",fontsize=10)


plot([-0.5,0.6,1.5],[0,0,4.5])
grid()
savefig("annexe.pdf")
show()
