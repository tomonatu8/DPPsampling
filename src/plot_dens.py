import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.cm as cm
import datetime


rootpi=1/np.sqrt(np.pi)



def v(x,y,B_num):
    """This is a
    """
    vec=[]
    for i in B_num:
        #print("math.factorial(i) = ",math.factorial(i))
        vec.append(1/rootpi * 1/math.sqrt(math.factorial(i)) * math.e**(-1/2 * (x**2+y**2)) *  complex(x,y)**i)
    return vec



#K(x1,x2) = v(x2)^T v(x1)
def pn(x,y,B_num):
    #print("v(x,y, B_num) = ",v(x,y, B_num))
    n = np.sum(B_num)
    return (np.linalg.norm(v(x,y,B_num)))**2 / n

def conj(zvec):
    newz=[]
    for z in zvec:
        newz.append(z.conjugate())
    return newz

def pi(x,y,i,B_num):
    hiku=0
    for j in range(i):
        hiku=hiku+np.dot(conj(e[j]),v(x,y,B_num))**2
    return (np.linalg.norm(v(x,y,B_num))**2 - hiku) / i


def make_data():
    L=[]
    for LL in range(20):
        L.append(0.7)
    for LL in range(20):
        L.append(0.3)
    print("L = ",L)
    B=[]
    B_num=[]
    for i in range(len(L)):
        bb=np.random.binomial(1, L[i], size=1)[0]
        B.append(bb)
        if bb==1:
            B_num.append(i)
    #Example: B_num =  [0, 1, 3, 4, 6, 7, 8, 9, 10, 12, 15, 16, 19, 20, 21, 24, 25, 26, 30, 31, 36, 37]
    print("B_num = ",B_num)
    return B_num

def plot_dens(Xlist, B_num, dt_now):
    x = np.linspace(-5,5,100)
    y = np.linspace(-5,5,100)
    pilist=[]
    for xx in x:
        for yy in y:
            pilist.append(pi(xx,yy,i+1,B_num))

    yilist=[]
    for j in range(50000):
        x=np.random.uniform(-5, 5)
        y=np.random.uniform(-5, 5)
        print("pilist = ", pilist)
        sn=(max(pilist))
        print("sn = ", sn)
        #棄却サンプリング
        pi_sampling=np.random.uniform(0, sn)
        if pi_sampling <= pi(x,y,i+1,B_num):
            #pi_samplelist.append(pi_sam)
            #ylist.append(y)
            Xi=[x,y]
            yilist.append([x,y])
    print("X_"+str(i+2)+"=",Xi)
    w = v(Xi[0],Xi[1],B_num)
    for j in range(i+1):
        w = np.array(w) - np.dot(conj(e[j]),v(Xi[0],Xi[1],B_num)) * np.array(e[j])
    e_new=w / np.linalg.norm(w, ord=2)
    e.append(e_new)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    counts,ybins,xbins,H = ax.hist2d([y[0] for y in yilist],[y[1] for y in yilist], bins=40, cmap=cm.jet)
    #ax.contour(counts,extent=[xbins.min(),xbins.max(),ybins.min(),ybins.max()],linewidths=3)
    fig.colorbar(H,ax=ax)
    print("Xlist = ",Xlist)
    for X in Xlist:
        ax.scatter(X[0],X[1],s=150, c="black")
    #plt.savefig('src/png/figure'+str(i+2)+'_'+dt_now.isoformat()+'.png')
    plt.show()
    return Xi


def plot_original_dens(B_num, dt_now):
    x = np.linspace(-5,5,100)
    y = np.linspace(-5,5,100)
    pnlist=[]
    for xx in x:
        for yy in y:
            pnlist.append(pn(xx,yy,B_num))

    pn_samplelist=[]
    ylist=[]
    for i in range(50000):
        x=np.random.uniform(-5, 5)
        y=np.random.uniform(-5, 5)
        sn=(max(pnlist))
        pn_sam=np.random.uniform(0, sn)
        if pn_sam <= pn(x,y,B_num):
            pn_samplelist.append(pn_sam)
            ylist.append([x,y])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    counts,ybins,xbins,H = ax.hist2d([y[0] for y in ylist],[y[1] for y in ylist], bins=40, cmap=cm.jet)
    #ax.contour(counts,extent=[xbins.min(),xbins.max(),ybins.min(),ybins.max()],linewidths=3)
    fig.colorbar(H,ax=ax)
    #plt.savefig('src/png/figure'+str(1)+'_'+dt_now.isoformat()+'.png')
    plt.show()

    return ylist


if __name__ == '__main__':
    """Sampling by the spectral method
    """
    dt_now = datetime.datetime.now()
    
    B_num = make_data()

    T = 5

    ylist = plot_original_dens(B_num, dt_now)
    #print("ylist = ", ylist)

    Xn=ylist[0]
    e_1=v(Xn[0],Xn[1],B_num)/np.linalg.norm(v(Xn[0],Xn[1],B_num), ord=2)
    e=[e_1]
    #正規直交基底の集合
    Xlist=[Xn]
    print("X_1=",Xn)
    for i in range(T):
        Xi = plot_dens(Xlist, B_num, dt_now)
        Xlist.append(Xi)
