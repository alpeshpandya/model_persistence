#!/usr/bin/env bash

export PATH=~/miniconda3/bin/:$PATH
# conda create -n mp_env python=3.6
# conda activate mp_env
pip install -r requirements.txt
conda install -c -y soumith torchvision
conda install -c -y soumith pytorch
conda install -c -y caffe2 caffe2