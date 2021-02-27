# Image_Cutter
# Yichen Wang 2020 Oct

import cv2


def crop_manga(height):
    im = cv2.imread('original.png')
    h,w,c = im.shape
    print(h,w)
    lastpage_height = h % height
    page_number = h // height
    print(lastpage_height, page_number)
    for i in range (0,page_number):
        page_name = str(i)+'.png'
        crop_img = im[i*height:(i+1)*height, 0:w]
        cv2.imwrite('pages/'+page_name,crop_img)
    last_page = im[page_number*height:h, 0:w]
    last_page_name = str(page_number) + '.png'
    cv2.imwrite('pages/'+last_page_name, last_page)

if __name__ == '__main__':
    crop_manga(1200)



