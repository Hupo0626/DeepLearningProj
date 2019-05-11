import cv2
class CVDetector:
    def __init__(self):
        pass
    def line_detector(self,img):
        lsd = cv2.createLineSegmentDetector(0)
        lines = lsd.detect(img)[0] #Position 0 of the returned tuple are the detected lines
        res=[]
        print('Detecting Lines')
        for l in lines[0]:
            x2,y2,x1,y1=l
            res.append('Line({},{},{},{})'.format(x2,y2,x1,y1))
        return res

    def circle_detector(self,img):
        print('Detecting Circle')
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
        res=[]
    #     print(circles)
        for c in circles:
            x,y,r=c[0]
            res.append('Circle({},{},{})'.format(x,y,r))
        return res
    def cont_detector(self,img):
        print('Detecting Contour')
        _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
        _,contours,_=cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        res=[]
    #     print(contours)
        for cnt in contours:
    #         print(cnt)
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            img=cv2.drawContours(img, [approx], 0, (0), 2)
            plt.imshow(img)
            print(len(approx))
            if len(approx) == 3:
                p1,p2,p3=(tuple(x[0]) for x in approx)
                res.append("Triangle({},{},{})".format(p1,p2,p3))
            elif len(approx) == 4:
                p1,p2,p3,p4=(x[0] for x in approx)
                ps=sorted([tuple(p1),tuple(p2),tuple(p3),tuple(p4)],key=lambda x:x[0]+x[1])
                res.append("Rectangle({},{})".format(ps[0],ps[-1]))
        return res
    def detect(self,img_dir):
        img=cv2.imread(img_dir,cv2.IMREAD_GRAYSCALE)

        lines = self.line_detector(img)

        circles=self.fcircle_detector(img)

        cont=self.cont_detector(img)

#         print('Line:',lines)
#         print('Circles:',circles)
#         print('Cont:',cont)
        return lines+circles+cont