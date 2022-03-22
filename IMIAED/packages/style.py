import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt 
import numpy as np
import cv2 
import os 
print(os.listdir("./"))

model = hub.load('http://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

def filtro(img1,img2):
    content_image = load_image("./IMIAED/packages/prueba.jpg")
    style_image = load_image('./IMIAED/packages/bag.jpg')
    content_image.shape
    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
    plt.imshow(np.squeeze(stylized_image))
    plt.show()
    cv2.imwrite('generated_img2.jpg')