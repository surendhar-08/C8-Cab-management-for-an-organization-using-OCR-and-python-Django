from django.http import HttpResponse
import cv2
import imutils
import numpy as np
import pytesseract
import os
import re
from PIL import Image
from django.shortcuts import render
from django.utils import timezone
from .models import carEntry,carDetails,Test
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import carEntrySerializers


class carList(APIView):
    def get(self,request):
        cars=carEntry.objects.all()
        serializers=carEntrySerializers(cars,many=True)
        return Response(serializers.data)

# def button(request):
#     return render(request, 'NumberPlateDetector/NPDhome.html')

def index(request):
    vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)


    while (1):
        ret, frame = vid.read()
        # img = cv2.imread(r'C:\Users\NantheshPrabu\Downloads\desktop\Car-Number-Plate-Detection-OpenCV-Python-master\Car-Number-Plate-Detection-OpenCV-Python-master\car5.png')
        names = []
        NumberPlate=NPDFuntion(frame)
        if (NumberPlate is not None):
            print(NumberPlate)
            q = carDetails.objects.all().values_list('car_number', flat=True)


            # if NumberPlate in q:
            #     test=Test(number=NumberPlate)
            #     test.save()
            #     print(list(Test.objects.all()))
            if (NumberPlate in q):
                print("numberplatedetector")
                c = carEntry(number_plate=NumberPlate, enter_date=timezone.now())
                c.save()

            names.append(NumberPlate)
            return render(request, 'NumberPlateDetector/NPDHome.html',{'NPDdata': NumberPlate})


        # cv2.waitKey(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()

    cv2.destoryAllWindows()


def NPDFuntion(frame):
    try:
        img = cv2.resize(frame, (620, 480))
    except Exception as e:
        print(str(e))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grey scale

    gray = cv2.bilateralFilter(gray, 13, 15, 15)

    edged = cv2.Canny(gray, 30, 200)  # Perform Edge detection

    contours = cv2.findContours(edged, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    screenCnt = None

    for c in contours:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        # if our approximated contour has four points, then
        # we can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break

    # Masking the part other than the number plate
    mask = np.zeros(gray.shape, np.uint8)

    if (screenCnt is not None):
        # print(screenCnt)
        new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
        new_image = cv2.bitwise_and(img, img, mask=mask)

        # Now crop
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
        cv2.imshow("show", Cropped)

        # filename = "car5_crop.png".format(os.getpid())
        # cv2.imwrite(filename, Cropped)
        # image = cv2.imread(r'C:\Users\NantheshPrabu\Downloads\desktop\Car-Number-Plate-Detection-OpenCV-Python-master\Car-Number-Plate-Detection-OpenCV-Python-master\car5_crop.png')

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        data = pytesseract.image_to_string(Cropped)
        data = re.sub(r"\s+", "", data)
        data = re.sub(r'[^\w\s]', '', data)
        if (len(data) >= 9 and len(data) <= 10):
            return data




# try:
#     path=os.path.join(mypath,n)

#     img=cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#     img=cv2.resize(img, (img_rows,img_cols))
#
# except Exception as e:
#     print(str(e))
