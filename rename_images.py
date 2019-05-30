import os, sys
import cv2
from PIL import Image
import shutil

class BatchRename():

	def __init__(self):
		self.path = sys.argv[1]
		print('==========',self.path)
		imgname = self.path + '/img'
		JPEGImagesname = self.path + '/JPEGImages'
		SegmentationClassname = self.path + '/SegmentationClass'
		if not os.path.exists(imgname):
			os.makedirs(imgname)
		if not os.path.exists(JPEGImagesname):
			os.makedirs(JPEGImagesname)
		if not os.path.exists(SegmentationClassname):
			os.makedirs(SegmentationClassname)

	def rename_img(self):
		filelist = os.listdir(self.path)
		list_x = []
		for x in filelist:
			if x != 'SegmentationClass' and x != "img" and x != "JPEGImages" and x != "JPEGImages_resized":
				list_x.append(x)
		i = 1
		for y in list_x:
			path_img=os.path.join(os.path.abspath(self.path), y+'/img.png')
			dst = os.path.join(os.path.abspath(self.path), 'img/' + str(i) + '.png')
			try:
				os.rename(path_img, dst)
				i = i + 1
			except:
				continue
		path_img_png = self.path + '/img/'
		for filename in os.listdir(self.path+'/img'):
			if os.path.splitext(filename)[1] == '.png':
				img = Image.open(path_img_png+filename)
				x = img.size[0]
				y = img.size[1]
				if x >= y:
					new_x = 500
					new_y = (500 * y) // x
				else:
					new_y = 500
					new_x = (x * 500) // y
				newfilename = filename.replace(".png", ".jpg")
				img = img.resize((new_x, new_y))
				img.save(self.path + '/JPEGImages/'+newfilename)

		path_img_512 = self.path + '/JPEGImages/'
		print(path_img_512)
		image_output_dir = self.path+'/JPEGImages_resized/'
		print(image_output_dir)
		if not os.path.exists(image_output_dir):
			os.mkdir(image_output_dir)

	def rename_label(self):
		filelist = os.listdir(self.path)
		list_x = []
		for x in filelist:
			if x != 'SegmentationClass' and x != "img" and x != "JPEGImages" and x != "JPEGImages_resized":
				list_x.append(x)
		i = 1
		txt_len = len(list_x)
		for y in list_x:
			path_img=os.path.join(os.path.abspath(self.path), y+'/label.png')
			dst = os.path.join(os.path.abspath(self.path), 'SegmentationClass/' + str(i) + '.png')
			try:
				os.rename(path_img, dst)
				i = i + 1
			except:
				continue
		path_img_png = self.path + '/SegmentationClass/'
		for filename in os.listdir(self.path + '/SegmentationClass'):
			if os.path.splitext(filename)[1] == '.png':
				img = Image.open(path_img_png + filename)
				# newfilename = filename.replace(".png", ".jpg")
				x = img.size[0]
				y = img.size[1]
				if x >= y:
					new_x = 500
					new_y = (500 * y) // x
				else:
					new_y = 500
					new_x = (x * 500) // y
				img = img.resize((new_x, new_y))
				img.save(self.path + '/SegmentationClass/'+ filename)

		with open(self.path+'/train.txt','w') as f1,\
			open(self.path+'/train.txt', 'r') as f2:
			for i in range(1,txt_len+1):
				f1.write(U"%d\r\n"%i)
			print(f2.read())
		with open(self.path+'/val.txt','w') as f1,\
			open(self.path+'/val.txt', 'r') as f2:
			for i in range(1,txt_len+1):
				f1.write(U"%d\r\n"%i)
			print(f2.read())
	def rm(self):
		l = os.listdir(self.path)
		for i in l:
			print(i)
			if i not in ('JPEGImages', 'SegmentationClass'):
				if os.path.isdir(self.path + '/' +i):
					shutil.rmtree(self.path + '/' +i)
				else:
					os.remove(self.path + '/' +i)


# /home/ai19/11

        

if __name__ == '__main__':
	demo = BatchRename()
	demo.rename_img()
	demo.rename_label()
	demo.rm()
	print("Successed !!!!!!!!! pu pu pa pu pu pa")




