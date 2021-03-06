This project aims to plot a color-magnitude diagram of stars obtained by photometry in V and I filters. It assumes that we have the images "imageV.fits" and "imageI.fits", and two files with the pixel coordinates, magnitudes and errors of the stars in each filter: "visible.dat" and "infrared.dat".

After using the task xyxymatch in IRAF, we obtain a file (let us name it "results.dat") containing 6 columns: X reference coordinate, Y reference coordinate, X input coordinate, Y input coordinate, Reference line number and Input line number.

In this repository, you can find three files which allow you to obtain the sky coordinates of each star, the color-magnitude diagram and the tip of the Red Giant Branch.

The file "coordinates.py", to be run in pyraf, allows you to obtain the sky coordinates of each star, given the pixel coordinates in the files "visible.dat" and "infrared.dat". 

The file "cmd.py", to be run in python, plots the color-magnitude diagram of the stars from the file "results.dat".

The file "trgb.py", which is an extension of "cmd.py" and does not work alone, selects the 100 brightest stars in the color-magnitude diagram which are in the tip of the red giant branch.
