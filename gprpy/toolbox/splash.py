import gprpy.gprpy as gp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import os
import matplotlib.image as im
from scipy import signal

def showSplash(a,dir_path,widfac,highfac):
    try:
        filename=os.path.join(dir_path,'exampledata','SnS','ComOffs','XLINE00.DT1')
        snakeGPR = gp.gprpy2d(filename)
        maxpoint=100;
        x=snakeGPR.twtt[0:maxpoint]
        y=snakeGPR.data[0:maxpoint,10]
    except:
        rick = signal.ricker(150, 4.0)
        x = np.linspace(0,85,100)
        y = rick[50:150]*25000
        
    # Snake body
    lw=7#5
    a.plot(x,y,'k',linewidth=lw*widfac,solid_capstyle='round')
    # Snake head
    Path = mpath.Path
    xshift=0
    headval=2500*widfac/highfac
    path_data = [
        (Path.MOVETO, [xshift,headval]),
        (Path.CURVE3, [-20+xshift,0]),
        (Path.LINETO, [xshift,-headval]),
        (Path.CURVE3, [10+xshift,0]),
        (Path.LINETO, [xshift,headval]),
        (Path.CLOSEPOLY, [xshift,headval])]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    patch = mpatches.PathPatch(path)
    patch.set_facecolor('black')
    a.add_patch(patch)
    # Eyes
    eye1 = mpatches.Ellipse([-2,1000], 3, 1000)
    eye2 = mpatches.Ellipse([-2,-1000], 3, 1000)
    eye1.set_facecolor('white')
    eye2.set_facecolor('white')
    a.add_patch(eye1)
    a.add_patch(eye2)
    # Tongue
    x, y = np.array([[-10, -13, -15], [0.0, 0.0, 600]])
    line1 = mlines.Line2D(x, y, lw=2*widfac, color='black')
    x, y = np.array([[-10, -13, -15], [0.0, 0.0, -600]])
    line2 = mlines.Line2D(x, y, lw=2*widfac, color='black')
    a.add_line(line1)
    a.add_line(line2)
    # Axis setup
    a.set_xlim([-25,90])
    a.set_ylim([-28000,12000])
    a.axis('off')
    # Text
    font = {'family': 'DejaVu Sans',
        'color':  'black',
        'weight': 'bold',
        'style': 'italic',
        'size': 60
            # 'size': 35*widfac
        }
#    a.text(35,-10000,'GPRPy',fontdict=font)
    a.text(50,-10000,'GPRPy',fontdict=font)

    # add UA logo
    filename1=os.path.join(dir_path,'toolbox','splashdat',
                           'A_Square_Logo_4c.png')
    ua = im.imread(filename1)
    #yanchor = -24500
    #yheight = 10000*0.9
    yanchor = -24000
    yheight = 10000*0.8
    xanchor = -20
    figsize = a.figure.get_size_inches()
    figratio = figsize[0]/figsize[1]
    ratio = a.get_data_ratio()*figratio
    xwidth = yheight/ratio
    a.imshow(ua, aspect='auto', extent=(xanchor, xanchor+xwidth,
                                        yanchor, yanchor+yheight),
             interpolation='spline36')

    # # add UA words
    # filename1=os.path.join(dir_path,'toolbox','splashdat',
    #                         'UA-StackedNameplate.png')
    # ua = im.imread(filename1)
    # #yanchor = -24500
    # #yheight = 10000*0.9
    # yanchor = -24000
    # yheight = 10000*0.4
    # xanchor = -10
    # figsize = a.figure.get_size_inches()
    # figratio = figsize[0]/figsize[1]
    # ratio = a.get_data_ratio()*figratio
    # xwidth = 5*yheight/ratio
    # a.imshow(ua, aspect='auto', extent=(xanchor, xanchor+xwidth,
    #                                     yanchor, yanchor+yheight),
    #          interpolation='spline36')
    
    
    # Add NSF logo
    filename2=os.path.join(dir_path,'toolbox','splashdat',
                           'NSF_4-Color_bitmap_Logo.png')
    nsf = im.imread(filename2)
    yanchor = -25000
    yheight = 10000
    xanchor = -5
    figsize = a.figure.get_size_inches()
    figratio = figsize[0]/figsize[1]
    ratio = a.get_data_ratio()*figratio
    xwidth = yheight/ratio
    a.imshow(nsf, aspect='auto', extent=(xanchor, xanchor+xwidth,
                                         yanchor, yanchor+yheight),
             interpolation='spline36')
    font2 = {'family': 'DejaVu Sans',
             'color':  'black',
             'size': 13.5}
    # 'size': 7.5*widfac
    a.text(-5,-27000,'EAR-1550732',fontdict=font2)

    
    # Add name/email
    font3 = {'family': 'DejaVu Sans',
             'color':  'gray',
             'size': 13.5}
    a.text(70,-22000,'Alain Plattner',fontdict=font3)
    a.text(59,-24000,'plattner@alumni.ethz.ch',fontdict=font3)
    #a.text(59.5,-24000,'plattner@alumni.ethz.ch',fontdict=font3)