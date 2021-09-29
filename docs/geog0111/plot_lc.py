# ANSWER
# this is a little long-winded, but just wraps up the codes above
import matplotlib
import matplotlib.patches
import matplotlib.pyplot as plt
import pandas as pd

def plot_lc(data,x_size=12,y_size=12):
    '''
    takes as input MODIS LC dataset
    plots the associated land cover map

    x_size,y_size as optional inputs
    '''
    lc_Type1 = pd.read_csv('data/LC_Type1_colour.csv')

    # generate matplotlib cmap and norm objects from these

    # get the LC codes, colours and classes
    # from LC_Type1_class and LC_Type1_colour
    cmap = matplotlib.colors.\
            ListedColormap(list(lc_Type1['colour']))
    norm = matplotlib.colors.\
            BoundaryNorm(list(lc_Type1['code']), len(lc_Type1['code']))

    # set up the legend
    legend_labels = dict(zip(list(lc_Type1['colour']),\
                             list(lc_Type1['class'])))
    patches = [matplotlib.patches.Patch(color=c, label=l)
               for c,l in legend_labels.items()]
    fig, axs = plt.subplots(1,figsize=(x_size,y_size))
    im = axs.imshow(data,cmap=cmap,norm=norm,interpolation="nearest")
    plt.legend(handles=patches,
              bbox_to_anchor=(1.4, 1),
              facecolor="white")
