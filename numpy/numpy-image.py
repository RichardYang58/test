from PIL import Image
import numpy as np
# a=np.array(Image.open("d:/temp/Beijin.jpg"))
# print(a.shape,a.dtype)
# b=[255,255,255]-a
# im=Image.fromarray(b.astype('uint8'))
# im.save("D:/temp/Beijin2.jpg")

# a=np.array(Image.open("d:/temp/Beijin.jpg").convert('L'))
# b=255-a
# im=Image.fromarray(b.astype('uint8'))
# im.save("D:/temp/Beijin3.jpg")

# a=np.array(Image.open("d:/temp/Beijin.jpg").convert('L'))
# c=(100/255)*a
# im=Image.fromarray(c.astype('uint8'))
# im.save("D:/temp/Beijin4.jpg")

# a=np.array(Image.open("d:/temp/Beijin.jpg").convert('L'))
# d=255*(a/255)**2
# im=Image.fromarray(d.astype('uint8'))
# im.save("D:/temp/Beijin5.jpg")

a=np.array(Image.open("d:/temp/Beijin.jpg").convert('L')).astype('float')
depth=10.
grad=np.gradient(a)
grad_x,grad_y=grad
grad_x=grad_x*depth/100.
grad_y=grad_y*depth/100.
A=np.sqrt(grad_x**2+grad_y**2+1.)
uni_x=grad_x/A
uni_y=grad_y/A
uni_z=1./A

vec_e1=np.pi/2.2
vec_az=np.pi/4.
dx=np.cos(vec_e1)*np.cos(vec_az)
dy=np.cos(vec_e1)*np.sin(vec_az)
dz=np.sin(vec_e1)

b=255*(dx*uni_x+dy*uni_y+dz*uni_z)
b=b.clip(0,255)
im=Image.fromarray(b.astype('uint8'))
im.save("D:/temp/BeijinHD.jpg")