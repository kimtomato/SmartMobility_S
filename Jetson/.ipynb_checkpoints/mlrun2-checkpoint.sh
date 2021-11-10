#!/bin/bash

sudo docker run -it --privileged --runtime nvidia --network host -v /home/kimtomato/project:/project \
        --env DISPLAY='192.168.123.104:0' nvcr.io/nvidia/l4t-ml:r32.5.0-py3
