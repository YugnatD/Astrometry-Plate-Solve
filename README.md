# Astrometry-Plate-Solve
Plate solver based on astrometry.net to generate sky-plot image without internet using index files

## Installation Instruction :

```
$ sudo apt-get install astrometry.net
$ sudo apt-get install astrometry-data-tycho2
```

Download index files with wget in this adresse : http://broiler.astrometry.net/~dstn/4200/
Be careful, there is about ~30Go of data.
```
$ wget -r -c http://broiler.astrometry.net/~dstn/4200/
```

Place the index file on : /usr/share/astrometry/

### Install dependency :
```
$ sudo apt-get install python-dev libatlas-base-dev
$ pip3 install ligo.skymap
$ pip3 install astropy
```

## Run application :
```
$ python3 main.py --image M27.png --focale 1000 --photosite 4.8
```

## Result Example
![Sky Plot](sky_plot_result.png)