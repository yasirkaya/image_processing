import matplotlib.pyplot as plt

image_1=plt.imread("image_1.jpg")

def my_function_1(image_1):
    print("Resimin Boyutu : ",image_1.ndim)
    print("\nResimin Çözünürlüðü : ",image_1.shape)
    print("\nR için min deðer:",image_1[:,:,0].min(),",max deðer:",image_1[:,:,0].max())
    print("\nG için min deðer:",image_1[:,:,1].min(),",max deðer:",image_1[:,:,1].max())
    print("\nB için min deðer:",image_1[:,:,2].min(),",max deðer:",image_1[:,:,2].max())
    
    my_function_1(image_1)
plt.imshow(image_1)
plt.show()
image_1[:,:,1] = image_1[:,:,1] +100
plt.show()