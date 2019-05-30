#coding=utf-8
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import tensorflow as tf
import sys


image_path = sys.argv[1]
# image_path = 'D:\\DATASETS\\坏箱照片_TEST\\BT


def my_rename(path):
    a,b = os.listdir(path)
    a = path + '/' + a
    b = path + '/' + b
    a_l = sorted(os.listdir(a))
    b_l = sorted(os.listdir(b))
    with open(path + '/' + 'train.txt', 'x') as f:
        for i in range(len(a_l)):
            if a_l[i][:-4] == b_l[i][:-4]:
                f.write(a_l[i][:-4]+'\n')
    


def pre_main(img):

    IMG_NAME=img[:-4]
    IMG_FORMAT=img.split('.')[len(img.split('.'))-1]
    im = Image.open(img)
    KK=0

    ROTATE_TYPE_LIST=[Image.FLIP_LEFT_RIGHT,Image.FLIP_TOP_BOTTOM,Image.FLIP_TOP_BOTTOM,Image.ROTATE_90,Image.ROTATE_180,Image.ROTATE_270]
    for ROTATE_TYPE in ROTATE_TYPE_LIST:
        out = im.transpose(ROTATE_TYPE)
        out.save(IMG_NAME+'_'+str(KK)+'.'+IMG_FORMAT)
        KK=KK+1

    img_size = im.size
    print("图片宽度 ",im.size[0])
    print("图片高度 ",im.size[1])

    im_resize=im.resize(( int(im.size[0]/2),int(im.size[1]/2) ),Image.BILINEAR)
    im_resize.save(IMG_NAME+'_'+str(KK)+'.'+IMG_FORMAT)
    KK=KK+1

    im_resize=im.resize(( int(im.size[0]/4),int(im.size[1]/4) ),Image.BILINEAR)
    im_resize.save(IMG_NAME+'_'+str(KK)+'.'+IMG_FORMAT)
    KK=KK+1


    if IMG_FORMAT=='png':


        im.save(IMG_NAME+'_'+str(KK)+'.'+IMG_FORMAT)
        KK=KK+1
        im.save(IMG_NAME+'_'+str(KK)+'.'+IMG_FORMAT)
        KK=KK+1
        im.save(IMG_NAME+'_'+str(KK)+'.'+IMG_FORMAT)
        KK=KK+1
        im.save(IMG_NAME+'_'+str(KK)+'.'+IMG_FORMAT)
        KK=KK+1


    else:


        with tf.gfile.FastGFile(img, "rb") as f:
            image_raw_data = f.read()
        with tf.Session() as sess:
            image = tf.image.decode_jpeg(image_raw_data)

            result = tf.image.adjust_brightness(image, 0.2)
            with tf.gfile.FastGFile('{}_{}.{}'.format(IMG_NAME,KK,IMG_FORMAT),'wb') as f:
                    f.write(sess.run(tf.image.encode_jpeg(tf.image.convert_image_dtype(result,dtype=tf.uint8))))
            KK=KK+1

            result = tf.image.adjust_brightness(image, -0.1)
            with tf.gfile.FastGFile('{}_{}.{}'.format(IMG_NAME,KK,IMG_FORMAT),'wb') as f:
                    f.write(sess.run(tf.image.encode_jpeg(tf.image.convert_image_dtype(result,dtype=tf.uint8))))
            KK=KK+1

            result = tf.image.adjust_saturation(image, 1.5)
            with tf.gfile.FastGFile('{}_{}.{}'.format(IMG_NAME,KK,IMG_FORMAT),'wb') as f:
                    f.write(sess.run(tf.image.encode_jpeg(tf.image.convert_image_dtype(result,dtype=tf.uint8))))
            KK=KK+1

            result = tf.image.adjust_saturation(image, -0.5)
            with tf.gfile.FastGFile('{}_{}.{}'.format(IMG_NAME,KK,IMG_FORMAT),'wb') as f:
                    f.write(sess.run(tf.image.encode_jpeg(tf.image.convert_image_dtype(result,dtype=tf.uint8))))










def add_image_tolist(image_path,imglist):
    #把每一个图片加到list中
    filelist=os.listdir(image_path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        org_image=os.path.join(image_path,files);#原来的文件路径                
        imglist.append(org_image)
    return imglist

def get_image_all(image_path):
    imglist=[]    
    #遍历文件夹,收集所有文件的名字
    for f in os.listdir(image_path):
        if os.path.isfile(image_path + os.path.sep + f):
            add_image_tolist(image_path,imglist)
        elif os.path.isdir(image_path + os.path.sep + f):
            print(image_path + os.sep + f)
            add_image_tolist(image_path + os.path.sep + f,imglist)
    return imglist


if __name__=='__main__':


    for image in get_image_all(image_path):
       print(image)
       pre_main(image)
    
    my_rename(image_path)

    exit()
