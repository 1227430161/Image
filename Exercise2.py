from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np  

import tensorflow as tf 
mnist=tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y)=mnist.load_data()

plt.rcParams["font.sans-serif"]="SimHei"

for i in range(16):
    num=np.random.randint(1,10000)
    plt.subplot(4,4,i+1)
    plt.imshow(test_x[num],cmap="gray")
    plt.title("标签值"+str(test_y[num]),fontsize=14)
    plt.axis("off")

plt.suptitle("MNIST测试集样本",fontsize=20,color="red")
plt.tight_layout(rect=(0,0,1,0.95))
plt.show()

    
