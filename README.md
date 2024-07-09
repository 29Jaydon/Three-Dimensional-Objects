#Creating 3D objects using OpenGL with Python
This project makes use of PyOpenGL in order to create a cube, a triangular prism and a pyramid. All of these objects exist within three-dimensional space. Furthermore, when the user presses certain keys on the keyboard the object will be set into motion. The objects within this program can be translated, rotated, and scaled along all three axes. 

##File structure
The code base contains five files namely: Cube.py, Display.py, Prism.py, Pyramid.py and motion.py. The Cube.py, Prism.py, and Pyramid.py contain the source code used to crate the objects in OpenGL.  The Display.py file contains the code that will allow the user to view and cycle through all the objects. The motion.py file contains the source code that will allow the user to translate, rotate and scale the objects within 3D space.

##Instructions on how to use the program. 
How to View and cycle through the objects:
Objects can be viewed individually by running the either the Cube.py, Prism.py, or Pyramid.py file, depending on which object you want to view. It is important to note that you can not interact with these files.
Objects can also be viewed by running the Display.py file. In this program you can cycle through the objects by clicking on either 1, 2, or 3.  When the 1 is clicked on the keyboard it will display the cube, 2 will display the triangular prism and 3 will display the pyramid. Note when the file runs you will see a blank pygame window, will have to click either 1,2, or 3 in order for an image to display. 

###How to select an object:
The motion.py file will execute the function that appears at the bottom of the page. Thus, all you have to do is type either cube_in_3d , prism_in_3d(), or  pyramid_in_3d(). To view the desired shape.

###How to translate an object about an axis
This feature can be done in the motion.py file after you have selected the object and executed the file.  You can use the following keyboard keys to translate the object:
a	Translate the object on the x axis in the positive direction.
d	Translate the object on the x axis in the negative direction.
w	Translate the object on the y axis in the positive direction.
s	Translate the object on the y axis in the negative direction.
z	Translate the object on the z axis in the positive direction.
x	Translate the object on the z axis in the negative direction.

###How to Rotate an object about an axis
This feature can be done in the motion.py file. After you have selected the object and executed the file.  You can use the following keyboard keys to rotate the object:
Keyboard keys	Action
h	Rotate the object on the x axis in the positive direction.
u	Rotate the object on the y axis in the negative direction.
j	Rotate the object on the z axis in the positive direction.
k	Rotate the object on the x axis in the negative direction.
n	Rotate the object on the z axis in the positive direction.

###How to Scale an object
This feature can be done in the motion.py file. After you have selected the object and executed the file.  You can use the following keyboard keys to scale the object:
Keyboard keys	Action
Right CTRL	Zooms in
Left CTRL	Zooms out



