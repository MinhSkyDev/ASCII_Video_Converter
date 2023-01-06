from PIL import ImageDraw,ImageFont,Image
import cv2
import numpy as np
import math


fileName="testVideo.mp4"
chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
charlist=list(chars)
charlen=len(charlist)
interval=charlen/256
scale_factor=0.09
charwidth=10
charheight=10


def draw_label(img, text, pos, bg_color):
   font_face = cv2.FONT_HERSHEY_SIMPLEX
   scale = 0.4
   color = (0, 0, 0)
   thickness = cv2.FILLED
   margin = 2
   txt_size = cv2.getTextSize(text, font_face, scale, thickness)

   end_x = pos[0] + txt_size[0][0] + margin
   end_y = pos[1] - txt_size[0][1] - margin

   cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
   cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)


def get_char(i):
    return charlist[math.floor(i*interval)]

font = cv2.FONT_HERSHEY_SIMPLEX

cap=cv2.VideoCapture(fileName)

Font=ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf',15)
while True:
    _,img=cap.read()
    frame = img
    img=Image.fromarray(img)

    width,height=img.size
    ##text_width = with
    print(width,height)
    img=img.resize((int(scale_factor*width),int(scale_factor*height*(charwidth/charheight))),Image.NEAREST)
    width,height=img.size
    pixel=img.load()
    outputImage=Image.new("RGB",(charwidth*width,charheight*height),color=(0,0,0))
    dest=ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r,g,b=pixel[j,i]
            h=int(0.299*r+0.587*g+0.114*b)
            pixel[j,i]=(h,h,h)
            dest.text((j*charwidth,i*charheight),get_char(h),font=Font,fill=(r,g,b))

    open_cv_image=np.array(outputImage)
    key=cv2.waitKey(1)
    if key == ord("q"):
        break
    draw_label(open_cv_image,"HAPU GAAAAA",(550,350), (255,255,255))
    cv2.imshow("Hmmm testing",open_cv_image)
cap.release()
cv2.destroyAllWindows()
