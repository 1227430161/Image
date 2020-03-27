from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np  

plt.rcParams["font.sans-serif"]="SimHei"
plt.figure(figsize=(10,10))

img=Image.open("Lena.tiff")
img_r,img_g,img_b=img.split()#颜色通道分离

plt.subplot(221)
plt.axis("off")
img_r_small=img_r.resize((50,50))
plt.imshow(img_r_small,cmap="gray")
plt.title("R-缩放",fontsize=14)

plt.subplot(222)
img_b_tr=img_b.transpose(Image.FLIP_LEFT_RIGHT)
img_b_tr_90=img_b_tr.transpose(Image.ROTATE_270)
plt.imshow(img_b_tr_90,cmap="gray")
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
plt.axis("off")
img_b_region=img_b.crop((0,0,150,150))
plt.imshow(img_b_region,cmap="gray")
plt.title("B-裁剪",fontsize=14)

plt.subplot(224)
plt.axis("off")
img_rgb=Image.merge("RGB",[img_r,img_g,img_b])
plt.imshow(img_rgb)
plt.title("RGB",fontsize=14)
img_rgb.save("test.png")

plt.suptitle("图像基本操作",fontsize=20,color="blue")

plt.show()

