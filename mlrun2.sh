#!/bin/bash

sudo docker run -it --privileged --runtime nvidia --network host -v /home/kimtomato/project:/project \
        nvcr.io/nvidia/l4t-ml:r32.5.0-py3
