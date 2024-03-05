import cv2
import numpy as np

img1 = cv2.imread("thor.jpg")
img1 = cv2.resize(img1, (500, 700))
img2 = cv2.imread("iron.jpg")
img2 = cv2.resize(img2, (500, 700))


# cv2.imshow("Thor", img1)
# cv2.imshow("Iron", img2)

def blend(x):
    pass


img = np.zeros((400, 400, 3), np.uint8)
cv2.namedWindow("window")
cv2.createTrackbar("alpha", "window", 1, 100, blend)
switch = '0:OFF 1:ON'
cv2.createTrackbar(switch, "window", 0, 1, blend)

while True:
    s = cv2.getTrackbarPos(switch, "window")
    a = cv2.getTrackbarPos("alpha", "window")
    n = float(a / 100)
    print(n)

    if s == 0:
        res = img[:]
    else:
        res = cv2.addWeighted(img1, 1 - n, img2, n, 0)
        cv2.putText(res, str(a), (20,50), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255,255,255), 2)
    cv2.imshow("res",res)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
