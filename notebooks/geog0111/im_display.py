import matplotlib.pyplot as plt
import matplotlib

def im_display(data,names,band=0,r=[None,None],c=[None,None],\
               title=None,colourmap=None,vmin=[],vmax=[],\
               x_size=12,y_size=8,shape=None,sub=(None,None)):
    '''
    a function called im_display that takes as input:
        data  :  a data dictionary
        names :  a list of keywords of datasets to plot

        optionally:
            band             : if 3D dataset
            title = None     : a title
            r=[None,None]    : row min/max
            c=[None,None]    : column min/max
            colourmap = None : a colourmap name
            x_size=16        : plot x size * shape[0]
            y_size=12        : plot y size * shape[1]
            shape=None       : subplots shape : e.g. (2,2)
    '''
    # sort out options
    n = len(names)
    if shape == None:
        shape = (n,1)
    # adaptive size
    x_size = x_size * shape[0]
    y_size = y_size * shape[1]

    fig, axs = plt.subplots(*shape,figsize=(x_size,y_size))
    if shape[0] ==1 and shape[1] == 1:
      axs = [axs]
    else:
      axs = axs.flatten()

    # set the figure title
    if title:
        fig.suptitle(title)

    # loop over names
    for i,k in enumerate(names):
        v_min = (type(vmin) == list and len(vmin)==len(names) and vmin[i]) or \
                ((type(vmin) is not list) and vmin) or None
        v_max = (type(vmax) == list and len(vmax)==len(names) and vmax[i]) or \
                ((type(vmax) is not list) and vmax)or None

        # plot image data
        this = data[k]
        if this.ndim == 2:
          this = this[r[0]:r[1],c[0]:c[1]]
        else:
          this = this[band,r[0]:r[1],c[0]:c[1]]
        im = axs[i].imshow(this,vmin=v_min,vmax=v_max,interpolation='nearest')
        if colourmap:
            im.set_cmap(colourmap)
        axs[i].set_title(k)
        fig.colorbar(im, ax=axs[i])    
      
