"""
Shows how to read in netcdf file, and plot using pcolor and contourf. Different 
methods of plot editing are demonstrated as well.

netcdf reference
reference: http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson14-Reading-NetCDF-files.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc4


#controls:
fntsze = 14 #variable to change fontsize of labels and text on plots

#close all figures
plt.close('all') #optional

#load coastline, 
#coastline.txt has two columns, which represent lon, lat coords of coastline
cline = np.loadtxt('coastline.txt')

#read in precip netcdf file
f = nc4.Dataset('cpc_precip_mon_mean.nc','r') 

#if you didn't know the variable names, you could check by doing the following:
#for name in f.variables:
#    print name

#print(f) would also provide information about the file

#assign individual variable names to object
lat = f.variables['lat'][:]
lon = f.variables['lon'][:]
precip = f.variables['precip'][:]

#check to see how precip is stored:
#print f.variables['precip'].dimensions

#precip has time,lat,lon on first,second and third dimensions
#suppose you wanted time on the last dimension. you could do:
precip = np.transpose(precip,[1,2,0]) 
#values in [1,2,0] specify where the dimension should go: send dim 0 to dim 1,
#send dim 1 to dim 2, send dim 3 to dim 0.

#print precip.shape
#dimensions are now lat,lon,time

#lets take an annual mean of the data and plot the spatial map
precip_annual_mean = precip.mean(2) #2 specifies that the mean should be taken along dimension 2

#create a figure
fig1 = plt.figure(figsize = (10,8)) #figsize = (width,height) in inches

#make plot using pcolor
subplt1 = plt.subplot(2,1,1)
subplt1.axes.set_aspect('equal') #preserves data scaling, so image doesn't get distorted
im1 = plt.pcolormesh(lon,lat,precip_annual_mean,cmap = plt.cm.YlGnBu)
plt.plot(cline[:,0],cline[:,1],'k')
im1.set_clim(2,10) #set color limits
plt.title('Annual mean precip over the Bay of Bengal')

#make plot using contourf
subplt2 = plt.subplot(2,1,2) #plot number starts 1. Execption to 0 based indexing!
subplt2.axes.set_aspect('equal') #preserves data scaling, so image doesn't get distorted
plt.plot(cline[:,0],cline[:,1],'k')
im2 = plt.contourf(lon,lat,precip_annual_mean,13,cmap = plt.cm.YlGnBu)
im2.set_clim(2,10)
plt.title('Same as above but with contours')

#note that we could have used a for loop to make those two plots rather than copy-pasting

#I'll just use a for loop to do the plot editting
for subplt in [subplt1, subplt2]:
    subplt.set_ylabel('Latitude',fontsize=fntsze)
    subplt.set_xlim(75,100)
    subplt.set_ylim(5,20)
    subplt.tick_params(axis='both', labelsize=fntsze)

cbar_ax = fig1.add_axes([0.8, 0.15, 0.05, 0.7]) #make a new axes for the colorbar
cb = fig1.colorbar(im1, cax=cbar_ax) #plot colorbar in cbar_ax using colormap of im1
cb.set_label('mm per day',fontsize=fntsze)
cb.ax.tick_params(labelsize=fntsze)

#save figure if you want
plt.savefig('annual_mean_precip_bob') #saves as .png by default

plt.show() #display on screen

#######################################################

#now we want to plot a time series of precipitation for a given area.
#suppose the region of interest was between 85N and 95N, and 5N and 15N
lati = np.logical_and(lat>=5,lat <15) #use logical_and to do element-wise truth testing
loni = np.logical_and(lon>=85,lon <95)

#we are going to call this region central Bay of Bengal: cbb
lon_cbb = lon[loni]
lat_cbb = lat[lati]
precip_cbb = precip[lati,:,:]
precip_cbb = precip_cbb[:,loni,:] 
#precip_cbb = precip_cbb[lati,loni,:] does something weird.
#print precip_cbb.shape

#reshape precip_cbb so that lat,lon values are in the same dimension
sz = precip_cbb.shape
precip_cbb = np.resize(precip_cbb,[sz[0]*sz[1],sz[2]])

#take spatial mean and std
precip_cbb_mean = np.squeeze(np.mean(precip_cbb,0))
precip_cbb_std = np.squeeze(np.std(precip_cbb,0))


#create a figure
fig2, (ax0, ax1) = plt.subplots(nrows=2, sharex=True) #alternative way to create subplot 
#sharex means share x-axis 

#plot monthly mean with std as errorbars
mon = np.arange(1,13) #arange stops at the value before the end point
ax0.errorbar(mon,precip_cbb_mean,yerr = precip_cbb_std,fmt='-o')

#plot with range of std shaded
err_up = precip_cbb_mean+precip_cbb_std/2
err_low = precip_cbb_mean-precip_cbb_std/2

ax1.fill_between(mon,err_low,err_up,facecolor='0.9')
ax1.plot(mon,precip_cbb_mean,'-r')

ax0.set_title('Monthly mean precipitation in central BoB')
ax1.set_title('Same above but with uncertainty shaded')
ax1.set_xlabel('Month')
ax0.set_ylabel('Precip (mm/day)')
ax1.set_ylabel('Precip (mm/day)')
ax1.set_xlim(1,12)
ax0.set_ylim(0,16)
ax1.set_ylim(0,16)


#save figure if you want
plt.savefig('precip_timeseries_bob')

plt.show() #display on screen














