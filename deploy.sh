#!/bin/sh
RPI_LGN=pi
RPI_IP=192.168.1.215
FOLDER=/home/pi/Documents/Projects/pi-booth

rsync -rav * $RPI_LGN@$RPI_IP:$FOLDER