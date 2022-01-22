import numpy
import cv2
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from scipy import misc
from scipy import ndimage
import math
from matplotlib import pyplot as plt

def scaleSpectrum(A):
  return numpy.real(numpy.log10(numpy.absolute(A) + numpy.ones(A.shape)))


# The Function Samples values from a spherical gaussian function from image center.
def makeGaussianFilter(numRows, numCols, sigma, highPass=True):
  centerI = int(numRows/2) + 1 if numRows % 2 == 1 else int(numRows/2)
  centerJ = int(numCols/2) + 1 if numCols % 2 == 1 else int(numCols/2)

  def gaussian(i,j):
    coefficient = math.exp(-1.0 * ((i - centerI)**2 + (j - centerJ)**2) / (2 * sigma**2))
    return 1 - coefficient if highPass else coefficient

  return numpy.array([[gaussian(i,j) for j in range(numCols)] for i in range(numRows)])


def filterDFT(imageMatrix, filterMatrix):
  shiftedDFT = fftshift(fft2(imageMatrix))

  filteredDFT = shiftedDFT * filterMatrix
  return ifft2(ifftshift(filteredDFT))


def lowPass(imageMatrix, sigma):
  n = imageMatrix.shape[0]
  m = imageMatrix.shape[1]
  return filterDFT(imageMatrix, makeGaussianFilter(n, m, sigma, highPass=False))


def highPass(imageMatrix, sigma):
  n = imageMatrix.shape[0]
  m = imageMatrix.shape[1]
  return filterDFT(imageMatrix, makeGaussianFilter(n, m, sigma, highPass=True))


def hybridImage(highFreqImg, lowFreqImg, sigmaHigh, sigmaLow):
  highPassed = highPass(highFreqImg, sigmaHigh)
  lowPassed = lowPass(lowFreqImg, sigmaLow)
  cv2.imwrite('../images/highpassed09.jpg',numpy.real(highPassed))
  cv2.imwrite('../images/lowpassed10.jpg', numpy.real(lowPassed))
  return highPassed + lowPassed

if __name__ == "__main__":
  mona_lisa = cv2.imread("../images/near03.jpg")
  mona_lisa = cv2.cvtColor(mona_lisa, cv2.COLOR_BGR2GRAY)
  da_vinci = cv2.imread("../images/far04.jpg")
  da_vinci = cv2.cvtColor(da_vinci, cv2.COLOR_BGR2GRAY)

  hybrid = hybridImage(mona_lisa, da_vinci, 25, 15)
  cv2.imwrite("../images/final_near.jpg", numpy.real(hybrid))