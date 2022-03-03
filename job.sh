#!/bin/bash

cd ./data/project #replace python filename with the name of your file

#conda activate styleganenv

pip install click
pip install numpy
pip install torch
pip install pillow
pip install psutil
pip install ninja 
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

python stylegan2-ada-pytorch/train.py --data converted_testkit --outdir results