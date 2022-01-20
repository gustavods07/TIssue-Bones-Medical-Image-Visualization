##Importing the libraries
from openpyxl import load_workbook
import os
from PIL import Image
import pydicom
import numpy as np
import cv2
import os, glob
import matplotlib.pyplot as plt
import skimage.morphology as morphology
from scipy import misc,ndimage
import scipy.misc





##reading of all DCM files at the chosen path ()

diretorio_usuario = 'C:/Users/gusta/Documents/LAPS/live/dicom/54879843/DICOM/Doe^Pierre [54879843]/20060101 000000 [ - CRANE POLYGONE]/'
diretorio = '/Series 005 [CT - Crane APC]'

array=[]
def listar(diretorio_usuario, diretorio):
	if os.path.isdir(diretorio_usuario + diretorio ):
		os.chdir(diretorio_usuario + diretorio)
		for arquivo in glob.glob("*"):
			if os.path.isdir(diretorio_usuario+diretorio+arquivo):
				listar(diretorio_usuario, diretorio+arquivo+'/')
			else:
				array.append(arquivo)
	else:
		print('arquivo: '+diretorio_usuario+diretorio)

listar(diretorio_usuario, diretorio)





##turning pixel values into HU values
def transform_to_hu(medical_image, image):
    intercept = medical_image.RescaleIntercept
    slope = medical_image.RescaleSlope
    hu_image = image * slope + intercept
    #print(image,hu_image)

    return hu_image

##windowing function
def window_image(image, window_center, window_width):
    img_min = window_center - window_width // 2
    img_max = window_center + window_width // 2
    window_image = image.copy()
    window_image[window_image < img_min] = img_min
    window_image[window_image > img_max] = img_max
    
    return window_image

for i in array:
    ##loading the image files
    #print(i)
    file_path = i
    output_path = "./"
    medical_image = pydicom.read_file(file_path)

    image = medical_image.pixel_array

    ##windowing to better visualize tissue or bones
    hu_image = transform_to_hu(medical_image,image)
    brain_image = window_image(hu_image, 40, 20)
    bone_image = window_image(hu_image, 400, 1000)


    ##choosing the final image dimensions
    target_width=1024
    target_height=1024
    ##generating the final image with bicubic interpolation
    bone = cv2.resize(bone_image, dsize=(target_width, target_height),interpolation=cv2.INTER_CUBIC)
    brain = cv2.resize(brain_image, dsize=(target_width, target_height),interpolation=cv2.INTER_CUBIC)


        
    ##saving the images at a chosen directory
    plt.imsave('C:/Users/gusta/Documents/LAPS/Experimento 2/images/'+'bone_'+i+'.jpeg',bone,cmap=plt.get_cmap('gray'))
    plt.imsave('C:/Users/gusta/Documents/LAPS/Experimento 2/images/'+'brain_'+i+'.jpeg',brain,cmap=plt.get_cmap('gray'))





