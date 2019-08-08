def plot(x, Y, title, labels, axis_title, log):
    import matplotlib.pyplot as plt
    colors = ['k','b','g','r','c', 'y', 'k']
    fig, ax1 = plt.subplots()
    plt.gcf().set_size_inches(12,8)
    ax = []
    threshold = 0
    axscale = 5
    ax.append(ax1)
    n = len(Y)
    if log == True:
        ax1.loglog(x, Y[0],'-k')
        ax1.grid('off')
        ax1.set_xlabel(axis_title[0])
        ax1.set_ylabel(axis_title[1])
        xt = np.linspace(x[0],x[-1],3)
        yt = np.linspace(Y[0][0],Y[0][-1],3)
        plt.xticks(xt);
        plt.yticks(yt);
        plt.title(title)
    else:
        count = 0
        for i in range(0, n):
            test = max(Y[i])-min(Y[i])
            if i > 0 and test > axscale*threshold or test < 1/axscale*threshold: # maintain good aspect ratio
                threshold = test
                fign, axn = plt.subplots()
                plt.gcf().set_size_inches(10,6)
                axn.plot(x, Y[i], '-' + colors[i] , label=labels[i])
                axn.legend(loc='lower right', fontsize = 14)
                ax.append(axn)
                count += 1
            else:
                ax1.plot(x, Y[i], '-' + colors[i], label=labels[i])
            plt.title(title, fontsize=20)
        # name existent axes when applicable
        if isinstance(axis_title, list):
            for i in range(0, count):
                ax[i].set_xlabel(axis_title[0])
                ax[i].set_ylabel(axis_title[i+1])
        else: #string
            ax1.set_xlabel(axis_title)
    if labels[0] != None:
        ax1.legend(loc='best', fontsize = 14)
        #ax2.legend(loc='best', fontsize = 14)
    for i in range(0, len(ax)):
        ax[i].grid(which='major', linestyle='-', linewidth='.05', color = colors[0]) # only on left axis, reduce clutter
        ax[i].grid(which='minor', linestyle='-', linewidth='.1', color = colors[0])

##---------------------------------------------------------------------------------------------------------------------------------------##

def PP(file, n, N, plotting=True, convolution=True, windows = False): # ParsePlot
    import subprocess
    import matplotlib.pyplot as plt
    import numpy as np
    from numpy import diff
    if (windows):
        raw = subprocess.getoutput(["type", file]).split()
    else:
        raw = subprocess.check_output(["type", file]).decode("utf-8").split()

    data = [float(i) for i in raw] # str -> f
    index, Q, labels, axis_title = [], [], [], ['index']
    for i in range(0, n):
        Q.append([])
        labels.append('Q'+str(i+1))
        if i < n:
            axis_title.append('Q'+str(i+1))
    i = 0
    while i < len(data)-1:
        if i%(n+1) == 0:
            index.append(data[i])
            Q_i = data[i+1:i+n+1]
            for j in range(0, len(Q)):
                try:
                    Q[j].append(Q_i[j])
                except IndexError:
                    print("You entered an invalid value for n")
                    return 0
            i += n+1
        else:
            print("something is very wrong")

    size = len(Q[0])

    indicator = Q[-1]
    if convolution == False:
        indicator = diff(indicator)
    i = index[indicator.index(min(indicator,key=abs))]
    p_ = str(round(i/N, 8))
    print('p* = ' + str(p_))
    x = [index[i]/N for i in range(0, len(index))]
    if plotting == True:
        if len(index) != size:
            print('ERROR: Dimensions do not match')
            print('index = '+ str(len(index)) +', Q = ' + str(len(Q)) +', Q[0] = ' + str(len(Q[0])))
        else:
            title = file + ' : $p^* = $ ' + '0.47045353'
            plot(x, Q, title, labels, axis_title, False)
