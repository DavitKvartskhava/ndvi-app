# credit source 

import getopt
import sys

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import ticker
from matplotlib.colors import LinearSegmentedColormap

class NDVI(object):
    def __init__(self, file_path, output_file=False, colors=False):
        self.image = plt.imread(file_path)
        self.output_name = output_file or 'NDVI.jpg'
        self.colors = colors or ['red', 'orange', 'yellow', 'green', 'blue']

    def create_colormap(self, *args):
        return LinearSegmentedColormap.from_list(name='custom1', colors=args)

    def create_colorbar(self, fig, image):
        position = fig.add_axes([0.825, 0.19, 0.2, 0.05])
        norm = colors.Normalize(vmin=-1.0, vmax=1.0)
        cbar = plt.colorbar(image,
                            cax=position,
                            orientation='horizontal',
                            norm=norm)
        cbar.ax.tick_params(labelsize=20)
        tick_locator = ticker.MaxNLocator(nbins=3)
        cbar.locator = tick_locator
        cbar.update_ticks()
        cbar.set_label("NDVI", fontsize=20, x=0.5, y=0.5, labelpad=50)

    def convert(self):
        """
        This function performs the NDVI calculation and returns an GrayScaled frame with mapped colors)
        """
        NIR = (self.image[:, :, 0]).astype('float')
        blue = (self.image[:, :, 2]).astype('float')
        green = (self.image[:, :, 1]).astype('float')
        bottom = (blue - green) ** 2
        bottom[bottom == 0] = 1  # replace 0 from nd.array with 1
        VIS = (blue + green) ** 2 / bottom
        NDVI = (NIR - VIS) / (NIR + VIS)

        fig, ax = plt.subplots(figsize=(25,25))
        image = ax.imshow(NDVI, cmap=self.create_colormap(*self.colors))
        plt.axis('off')

        self.create_colorbar(fig, image)

        extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        # return fig
        fig.savefig(self.output_name, dpi=600, transparent=True, bbox_inches=extent, pad_inches=0)
        # plt.show()




class VARI(object):
    def __init__(self, file_path, output_file, colors=False):
        self.image = plt.imread(file_path)
        self.output_name = output_file
        self.colors = colors or ['red', 'orange', 'yellow', 'green', 'blue']

    def create_colormap_VARI(self, *args):
        return LinearSegmentedColormap.from_list(name='custom1', colors=args)

    def create_colorbar_VARI(self, fig, image):
        position = fig.add_axes([0.825, 0.19, 0.2, 0.05])
        norm = colors.Normalize(vmin=-1.0, vmax=1.0)
        cbar = plt.colorbar(image,
                            cax=position,
                            orientation='horizontal',
                            norm=norm)
        cbar.ax.tick_params(labelsize=20)
        tick_locator = ticker.MaxNLocator(nbins=3)
        cbar.locator = tick_locator
        cbar.update_ticks()
        cbar.set_label("VARI", fontsize=20, x=0.5, y=0.5, labelpad=50) 

    def convert_VARI(self):
        red = (self.image[:, :, 0]).astype('float')
        blue = (self.image[:, :, 2]).astype('float')
        green = (self.image[:, :, 1]).astype('float')
        VARI = (green - red) / (red + green - blue + .001)

        fig, ax = plt.subplots(figsize=(25,25))
        image = ax.imshow(VARI, cmap=self.create_colormap_VARI(*self.colors))
        plt.axis('off')

        self.create_colorbar_VARI(fig, image)

        extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig(self.output_name, dpi=600, transparent=True, bbox_inches=extent, pad_inches=0)


class TGI(object):
    def __init__(self, file_path, output_file=False, colors=False):
        self.image = plt.imread(file_path)
        self.output_name = output_file or 'VARI.jpg'
        self.colors = colors or ['red', 'orange', 'yellow', 'green', 'blue']

    def create_colormap_TGI(self, *args):
        return LinearSegmentedColormap.from_list(name='custom1', colors=args)

    def create_colorbar_TGI(self, fig, image):
        position = fig.add_axes([0.825, 0.19, 0.2, 0.05])
        norm = colors.Normalize(vmin=-1.0, vmax=1.0)
        cbar = plt.colorbar(image,
                            cax=position,
                            orientation='horizontal',
                            norm=norm)
        cbar.ax.tick_params(labelsize=20)
        tick_locator = ticker.MaxNLocator(nbins=3)
        cbar.locator = tick_locator
        cbar.update_ticks()
        cbar.set_label("TGI", fontsize=20, x=0.5, y=0.5, labelpad=50) 

    def convert_TGI(self):
        red = (self.image[:, :, 0]).astype('float')
        blue = (self.image[:, :, 2]).astype('float')
        green = (self.image[:, :, 1]).astype('float')
        VARI = (green - (.39 *red)) - (.61 * blue)

        fig, ax = plt.subplots(figsize=(25,25))
        image = ax.imshow(VARI, cmap=self.create_colormap_TGI(*self.colors))
        plt.axis('off')

        self.create_colorbar_TGI(fig, image)

        extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig(self.output_name, dpi=600, transparent=True, bbox_inches=extent, pad_inches=0)