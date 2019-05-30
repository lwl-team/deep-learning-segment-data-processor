#!/bin/bash
#sudo gedit ~/.local/lib/python3.5/site-packages/labelme/cli/json_to_dataset.py

dir=`ls /home/ai18/shared_dir/data/1905261602_DS_BT_G2_NO_CONTAINER_LABEL_TIME/`    #定义遍历的目录
path="/home/ai18/shared_dir/data/1905261602_DS_BT_G2_NO_CONTAINER_LABEL_TIME/"
for i in $dir
do
    labelme_json_to_dataset ${path}$i
done

sudo python3 rename_images.py ${path} && sudo python3 data_argument_traditional_E4_3ways+resize.py ${path}

