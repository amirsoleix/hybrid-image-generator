# Hybrid Image Generator

The project consists of various sections, each one demanding knowledge from a different aspect of basic image recognition. The project is an assignment from **Signals and Systems** course in **Sharif University of Technology** instructed by **Dr. Babak Khalaj**.

## Applying Filters

Different filters including Mean, Gaussian, and Median are used to reduce noise in a colored image and a black and white image. The effectiveness of each filter with different degrees of pressure is documented in the `report.pdf`. The filters are then used to reduce noise in black and white pictures with different types of noise.

## Template Matching

Using Python `OpenCV` library a template matching operation is carried out to detect wheels of a car. Another example is used to detect faces in a movie poster.

## Line Detection

The same library is used to detect lines with different lengths by setting parameters and determing the threshold in the instance image recognition function.

## Hybrid Images

The last section generates a [hybrid image](https://en.wikipedia.org/wiki/Hybrid_image) from two different images and saves the result in the given directory. Note that the action is performed by first transforming the images into frequency domain, applying low-pass and high-pass filters to images and then morphing them in frequency domain. Finally, by reversing the operation from the first step we obtain the hybrid image.

P.S. More about details of implementation and results can be found in `report.pdf`.
