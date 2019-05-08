import itertools
import cv2
'''
todo: install opencv2
'''
import numpy as np
import matplotlib.pyplot as plt

class Transform:
    def __init__(self):
        pass
    def interpolate(self,img,i,j):
        i,j=np.clip(i,0,img.shape[0]-1),np.clip(j,0,img.shape[1]-1)
    #     i=min(img.shape[0])
        i0,i1,j0,j1=map(int,[max(0,np.floor(i)),min(img.shape[0]-1,np.ceil(i)),max(0,np.floor(j)),min(img.shape[1]-1,np.ceil(j))])

        try:
            if i1==i0:
                pij0=img[i0,j0]
                pij1=img[i0,j1]
            else:
                pij0=img[i0,j0]*((i-i0)/(i1-i0))+img[i1,j0]*((i1-i)/(i1-i0))
                pij1=img[i0,j1]*((i-i0)/(i1-i0))+img[i1,j1]*((i1-i)/(i1-i0))
            if j1==j0:
                p=pij0*0.5+pij1*0.5
            else:
                p=pij0*((j-j0)/(j1-j0))+pij1*((j1-j)/(j1-j0))
        except:
            print(img.shape,i,j,i0,j0,i1,j1)
    #         print(pij0,pij1,p)
            raise
        return p

    def distortion(self,img,anchor,vector):
        '''
        :param img: dismiss
        :param anchor: the anchor point where vector starts
        :param vector: the vector representing the distortion (direction and level)
        :return: distorted image
        '''
        size=img.shape
    #     anchor=(np.random.randint(size[0]),np.random.randint(size[1]))
#         anchor=(130,130)
        p1=(anchor[0]+vector[0],anchor[1]+vector[1])
#         print(p0,p1)
        new_img=img.copy()

    #     for oi,oj in itertools.product(range(anchor[0]-sqr_radius,anchor[0]+sqr_radius),range(anchor[1]-sqr_radius,anchor[1]+sqr_radius)):
        for ti,tj in itertools.product(range(size[0]),range(size[0])):
            d1,d2=abs(ti-p1[0]),abs(tj-p1[1])
            d=np.sqrt((ti-p1[0])**2+(tj-p1[1])**2)
            vij=(vector[0]*(1-d/size[0])),vector[1]*(1-d/size[1])
            oi,oj=ti-vij[0],tj-vij[1]
            v=self.interpolate(img,oi,oj)
            if (v>255).all():
                print(v)
            new_img[ti,tj]=v

        return new_img