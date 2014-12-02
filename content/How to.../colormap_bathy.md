Title: Colormap example for bathymetry
Slug: colormap-bathymetry
Date: 2014-11-04 13:12 UTC-07:00
Authors: ZB Szuts
Tags: color, colormap, jet, bathymetry
Summary: An example of making a map with filled bathymetric contours in matplotlib.

# Manipulating colormaps for bathymetric data

The following notebook gives one example of how to make a decent looking chart with filled bathymetric contours using matplotlib - decent being in the eye of the beholder.  This builds on discussion from the 27 Oct 2014 PyHOGS meeting, earlier meetings on colormaps with matplotlib, and on the 10 Nov 2014 PyHOGS meeting.

## Aim
Using Matlab it's hard to directly align desired contour intervals with the desired color, and this becomes very tricky if your contour intervals are not evenly spaced.  It turns out there are easy ways to do this with matplotlib.

### Colormap
I'd like a colormap that goes from white (shallow water) to dark blue (deep water), that has more colors for shallow depths for resolving large bathymetric changes close to land, and that has a small discrete number of colors.  Few discrete colors helps the viewer to determine which isobath corresponds to what depth.

### Nonuniform contour intervals
There is an easy way to implement this with built-in scaling functions that scale the data to the colormap.  Although one can always scale the data oneself before plotting, e.g. by taking its log, it is more convenient in python to use the built in normalization methods instead.

Generally speaking, this is related to how the colormap is mapped to the data.  
![](/images/color_data_mapping.jpg "Mapping between colormap and data")
Normally (at left), this is done automatically, or by matching the [0,1] range of the colormap to the specified [vmin,vmax] range of the data (here, I've used the [-8000,0] range of the bathymetric dataset I plot below).  Uniform intervals in the data are mapped to uniform intervals in the colormap.  What I'm trying to do (at right) is to align non-uniform levels in the data to uniform levels in the colormap, to compress/extend the colormap to better resolve certain ranges of data.

### Spacing of colorbar ticks

When using `plt.colorbar()`, the contour intervals can be shown two ways, either with uniform spacing on the plotted colorbar (the default)

    colorbar(pc, spacing='uniform')

or by placing the colorbar ticks relative to their respective numerical value

    colorbar(spacing='proportional')

{% notebook examples/Colormap_bathy.ipynb%}
