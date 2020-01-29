<h1>Image identification with a convolutional neural network</h1>

developed by M. Simsek @ University Reutlingen

The aim of this project is to find the color, shape and x/y-coordinates of images with a convolutional neural network. 
The data for train and test was generated by an own image generator using scikit-image (see image_generator folder). 
Used Data includes 6.000 training images and 3.000 test images. 

Image properties:

    image size: 128x128
    shapes: triangle, window, hook  
    color: red, green, blue 
  
Following parameters were used for the CNN:

    learning rate: 0.001, momentum:0.9 (SGD optimizer)
    number of epochs: 20
    batch size: 16
    
Achieved results:

    Coordinate deviation: 
        mean error: x: 0.14 / y: 1.01
        standard error: x: 0.11 / y: 0.94
    accuracy of colour: 100% 
    accuracy of shape: 100%
    avg. loss: 0.0023

**Before execution, unpack the images from training_images and testing_images folders or generate new images using the image generator.**
    
This prototyp was developed as an container-based application to minimize the influence of the application to the execution environment and its operating system. Use the following commands to execute the docker-based application:

build image

    docker build --rm -f Dockerfile -t nn_image_identification .

run container

    docker run --rm -it -p 0.0.0.0:6006:6006 nn_image_identification

conncecting to running container

    docker attach <container>

run script

    python main.py
