import numpy as np  
import cv2


def pad(img, filtr, value = 0):

    ker_size = filtr.shape[0]
    p = (ker_size - 1) // 2
    m, n, *_ = img.shape
    padded_h = m + 2 * p
    padded_w = n + 2 * p
    padded_img = np.ones([padded_h, padded_w], np.uint8) * value
    padded_img[p:m + p, p:n + p] = img.copy()
    # print(padded_img.shape)
    return padded_img


#dilation
def dilate(img, str_ele):

    str_ele = np.array(str_ele) 

    no_of_ones = np.sum(str_ele)
     
    m , n, *_ = img.shape

    p = (ker_size - 1) // 2

    padded_img = pad(img, str_ele)

    padded_img[p:m + 2, p:n + 2] = img.copy()

    img2=np.zeros([m,n],np.uint8)

    padded_img = padded_img / 255

    for i in range(p, m):
        for j in range(p, n):
            kernel = padded_img[i - n : i + n + 1, j - n : j + n + 1]    
            value = int(np.dot(kernel.flatten(), str_ele.flatten()))
           
            if value > 0:
                img2[i, j]=255
            else:
                img2[i, j]=0

    return img2


#erosion
def erode(img, str_ele):
    
    str_ele = np.array(str_ele) 

    no_of_ones = np.sum(str_ele)

    m , n, *_ = img.shape

    p = (ker_size - 1) // 2

    padded_img = pad(img, str_ele)

    padded_img[p:m + 2, p:n + 2] = img.copy()

    img2=np.zeros([m,n],np.uint8)

    padded_img = padded_img / 255

    for i in range(p, m):
        for j in range(p, n):
            kernel = padded_img[i - n : i + n + 1, j - n : j + n + 1]    
            value = int(np.dot(kernel.flatten(), str_ele.flatten()))
           
            if value == no_of_ones:
                img2[i, j]=255
            else:
                img2[i, j]=0

    return img2


if __name__ == '__main__':


    img = cv2.imread('f://cvg19//789.png',0)
    cv2.imshow("img",img)
    #print(list(img))

    #structural element
    se = [[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]]

    # se =  [[0, 0, 1, 0, 0],
    #        [0, 0, 1, 0, 0],
    #        [1, 1, 1, 1, 1],
    #        [0, 0, 1, 0, 0],
    #        [0, 0, 1, 0, 0]]  
    

    dil = dilate(img, se)
    ero = erode(img, se)
    cls = erode(dil, se)
    opn = dilate(ero, se)

    cv2.imshow("dilation", dil)
    cv2.imshow("erosion", ero)
    cv2.imshow("opening", opn)
    cv2.imshow("closing", cls)
    cv2.imshow("gradient", dil - ero)


    cv2.waitKey(0)
    cv2.destroyAllWindows()



