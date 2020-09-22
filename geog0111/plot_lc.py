# ANSWER
# this is a little long-winded, but just wraps up the codes above
import matplotlib
import matplotlib.pyplot as plt
from geog0111.modis import Modis

def plot_lc(data,x_size=12,y_size=12):
    '''
    takes as input  LC dataset
    plots the associated land cover map
    
    x_size,y_size as optional inputs
    '''
    # datasets
    # assume these are sorted in order
    LC_Type1_class = {
        'Unclassified': -1,
        'Evergreen_Needleleaf_Forests': 1,
        'Evergreen_Broadleaf_Forests': 2,
        'Deciduous_Needleleaf_Forests': 3,
        'Deciduous_Broadleaf_Forests': 4,
        'Mixed_Forests': 5,
        'Closed_Shrublands': 6,
        'Open_Shrublands': 7,
        'Woody_Savannas': 8,
        'Savannas': 9,
        'Grasslands': 10,
        'Permanent_Wetlands': 11,
        'Croplands': 12,
        'Urban_and_Built_up_Lands': 13,
        'Cropland_Natural_Vegetation_Mosaics': 14,
        'Permanent_Snow_and_Ice': 15,
        'Barren': 16,
        'Water_Bodies': 17,
    }
    # 
    # set up colour names associated with the class names
    # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
    LC_Type1_colour = {
        'Unclassified': "black",
        'Evergreen_Needleleaf_Forests': "springgreen",
        'Evergreen_Broadleaf_Forests': "darkgreen",
        'Deciduous_Needleleaf_Forests': "green",
        'Deciduous_Broadleaf_Forests': "lightgreen",
        'Mixed_Forests': "yellow",
        'Closed_Shrublands': "blue",
        'Open_Shrublands': "tan",
        'Woody_Savannas': "brown",
        'Savannas': "khaki",
        'Grasslands': "darkolivegreen",
        'Permanent_Wetlands': "aqua",
        'Croplands': "red",
        'Urban_and_Built_up_Lands': "dimgrey",
        'Cropland_Natural_Vegetation_Mosaics': "violet",
        'Permanent_Snow_and_Ice': "snow",
        'Barren': "sienna",
        'Water_Bodies': "navy",
    }
    
    # generate matplotlib cmap and norm objects from these

    # get the LC codes, colours and classes
    # from LC_Type1_class and LC_Type1_colour
    codes   = list(LC_Type1_class.values())
    classes = list(LC_Type1_colour.keys())
    colour  = list(LC_Type1_colour.values())

    cmap = matplotlib.colors.ListedColormap(colour)
    norm = matplotlib.colors.BoundaryNorm(codes, len(codes))
    
    # set up the legend
    legend_labels = dict(zip(colour,classes))
    patches = [matplotlib.patches.Patch(color=c, label=l)
               for c,l in legend_labels.items()]
    fig, axs = plt.subplots(1,figsize=(x_size,y_size))
    im = axs.imshow(data,cmap=cmap,norm=norm,interpolation=None)
    plt.legend(handles=patches,
              bbox_to_anchor=(1.4, 1),
              facecolor="white")

