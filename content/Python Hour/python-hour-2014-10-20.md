Title: Python Hour - 20 October 2014
Slug: python-hour-2014-10-20
Date: 2014-10-20 11:00 UTC-07:00
Tags: colors, colormaps, jet
Summary: Colormaps, colormaps, colormaps!!!
Author: J.Paul Rinehimer

## Meeting Summary

### Color and colormaps in matplotlib
We informally discussed various aspects of color and colormaps in matplotlib. Some of the topics included:

* Color and colormap basics
* Generating custom diverging colors
* Centering colormaps and displaying the center-valued color
* Differences between `pcolormesh` and `contourf`
* Setting upper, lower limits, and bad colors
* Using a colormap to color lines

After the meeting, I created a notebook expanding on many of the examples that were shown.  The notebook may be found in the [How-to section](colormap-examples) and has been added to the [notebook repository](https://github.com/PyHOGS/pyhogs-code/blob/master/notebooks/examples/Colormap%20examples.ipynb) on GitHub.

### The problem with jet
We also talked about the disadvantages of the jet colormap that is the default for matplotlib and Matlab (pre-2014b).  The main disadvantage of the jet colormap is that there are discontinuities in the luminosity (lightness) of the map. Because of these kinks in lightness and non-ordered colors, figures using the jet colormap often seem to have details that aren't in the data, for example, bands existing in smoothly-varying data around yellow. Worse yet, jet can also obscure details in green and cyan bands because the lightness doesn't change as rapidly in these regions. So jet both obscures features and generates false features. For examples of this, see some of the references below.

### Basic colormap theory
What is needed instead is a *perceptual colormap*, i.e. one in which equal steps in data are perceived as equal steps in the colorspace. Because humans perceive changes in lightness more readily than changes in hue, colormaps with monotonically and evenly increasing lightness are easier to interpret. jet does not fit this category.

Colormaps can generally be split into 4 groups:

* Sequential: Lightness increases/decreases monotonically, often from white through a single hue.  Good for showing magnitude and ordering of data. Generally converts to grayscale well.
* Diverging: Lightness has a maximum at some central or critical value, and reaches a minimum at either end. Good for showing anomalies about zero or some other critical value as well as direction. Usually *does not* convert well to grayscale because the two ends often have similar luminosity.
* Qualitative: These colormaps represent categorical data that may not have an ordering and are often discrete. For these mappings, it is important that all the colors are distinguishable from all the others.
* Special / Miscellaneous: These are maps that may or may not fit the above categories and usually consist of maps designed for a particular use such as showing both land and water topography or displaying hot/cold regions. These colormaps try to connect with intuitive colors for the parameters and, while they may not be perfect perceptual maps, are useful for some purposes where nature suggests a colormap.

Other important considerations when designing colormaps include awareness of colorblindness, conversion to grayscale, and how the colors look when used in different media such as online, print, and projection.

## Colormap references
During the meeting, we compiled a number of useful colormap references, both from online and published literature:

### matplotlib  references
* [Choosing colormaps Guide](http://matplotlib.org/users/colormaps.html): Good guide on choosing colormaps provided by the matplotlib team.  Has plots of the various default colormaps show how lightness changes throughout the maps
* [Default colormaps](http://matplotlib.org/examples/color/colormaps_reference.html): Quick reference for all of the default colormaps in matplotlib.

#### Webpages
* [Colorbrewer](http://colorbrewer2.org/): Good source for colormaps.  Shows example maps applying the colormap in different regions.  Also gives color-blind and printer-safe options.
* [Palletton](http://paletton.com) and [Adobe Color CC](https://color.adobe.com/create/color-wheel/): Online utilities for generating custom color schemes that follow established color paradigms.
* [How bad is your colormap?]( https://jakevdp.github.io/blog/2014/10/16/how-bad-is-your-colormap/): Quick and recent overview of problems with the jet colormap along with some Python code (and a haiku!).
* [The Rainbow is Dead. Long live the Rainbow!]( http://mycarta.wordpress.com/2012/05/29/the-rainbow-is-dead-long-live-the-rainbow-series-outline/): Long series examining the jet colormap, how to make it better, and looking at different colorspaces for interpolation.

#### Publications
* [Ware, C (1998) Color Sequences for Univariate Maps: Theory, Experiments, and Principles *IEEE Computer Graphics and Applications,* Sep 1998, 41-49.](http://ccom.unh.edu/sites/default/files/publications/Ware_1988_CGA_Color_sequences_univariate_maps.pdf)

    Nice article with a quick overview and theory of color perception.

* [Eddins, S (2014) Rainbow color map critiques: An overview and annotated bibliography. Mathworks Newsletter.](http://www.mathworks.com/tagteam/81137_92238v00_RainbowColorMap_57312.pdf)

    Great overview of colormaps and some color theory by a Matlab developer. Also includes a comprehensive annotated bibliography of more in-depth references. This was likely developed as a whitepaper to support the change in the Matlab default colormap (from jet to parula) in Release 2014b.

* [Light, P and J.Bartlein (2004), The end of the rainbow? Color schemes for improved data graphics, Eos, Transactions American Geophysical Union, 85 (40), 385-391, doi:10.1029/2004EO400002.](http://onlinelibrary.wiley.com/doi/10.1029/2004EO400002/abstract)

    This paper focuses on colormaps in the geosciences and colorblindness. Matplotlib has a few similar default colormaps and a [library for Matlab](http://www.mathworks.com/matlabcentral/fileexchange/17555-light-bartlein-color-maps) is available. Ironically, the first few pages of the online PDF are in black-and-white with color pages reproduced afterwards.

* [Borland, D and RM Taylor (2007) Rainbow color map (still) considered harmful, IEEE Computer Graphics and Applications, 27 (2), 14-17, doi:10.1109/MCG.2007.323435.](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4118486&tag=1)

    Short review of the problems with rainbow colormaps and some statistics on how often it's used in medical imaging.

* [Moreland, K (2009) Diverging color maps for scientific visualization, Proceedings of the 5th International Symposium on Visual Computing, December 2009, doi:10.1007/978-3-642-10520-3_9.](http://www.sandia.gov/~kmorel/documents/ColorMaps/)

    A longish paper that goes into some color theory and discusses various colorspaces and the math involved in colors. Also included on the website are supplemental materials like Excel, R, Python, and Matlab tools to create custom colormaps.
