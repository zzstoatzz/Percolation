import pandas as pd
from findiff import FinDiff as fd 
import igraph as i

def display(outfile):
    df = pd.read_csv(outfile,sep=' ', header=None)
    df.columns = ['smax', 'M2', 'M2-']
    df.plot(y='smax', use_index=True, figsize=(9, 5))
    M = df['smax']
    d_di = fd(0, 1)
    dm_di = d_di(M, 1)
    cp = dm_di.tolist().index(max(dm_di))
    print("\n", "p_c_i =",round(cp/df.shape[0], 5))

def init_g(WIDTH, HEIGHT):
    g = i.Graph()
    g.add_vertices(WIDTH*WIDTH*HEIGHT)
    style = {}
    style["vertex_size"] = 0.5
    style["layout"] = 'grid'
    style["bbox"] = (300, 300)
    style["margin"] = 50
    style["autocurve"] = False
    return g, style
  
def plot(g, style, j):
    return i.plot(g, **style).save("imgs/img"+str(j+1)+".png")
    
def valid_pair(s, t, WIDTH):
    distinct = s != t
    x_per = abs(s-t) != WIDTH-1
    y_per = abs(s-t) != (WIDTH-1)*WIDTH
    return distinct and x_per and y_per