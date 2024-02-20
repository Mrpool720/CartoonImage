# CartoonImage

This Python code is a graphical user interface (GUI) application for cartoonifying images. Here's a breakdown of the major components and functionalities:

Imported Libraries:

cv2: OpenCV library for image processing.<br>
easygui: Provides a file dialog box for easy file selection. <br>
numpy: For array manipulation, particularly for storing images.<br>
imageio: For reading images stored at a particular path.<br>
sys: For system-specific parameters and functions.<br>
matplotlib.pyplot: For plotting images.<br>
os: For interacting with the operating system, such as file path operations.<br>
tkinter: For creating the GUI.<br>
PIL: Python Imaging Library, used here for opening, manipulating, and saving many different image file formats.<br>
GUI Creation:<br>

Creates a main window using tkinter.<br>
Sets the window dimensions, title, and background color.<br>
Initializes a label for displaying messages.<br>
Functionality:<br>

upload(): Opens a file dialog box using easygui for the user to select an image file. Upon selection, it calls the cartoonify() function.<br>
cartoonify(ImagePath): This function takes the selected image path as input and performs the following operations:<br>
Reads the image using OpenCV.<br>
Converts the image to RGB color space.<br>
Checks if the image is valid.<br>
Resizes the image.<br>
Converts the image to grayscale.<br>
Applies median blur to smooth the grayscale image.<br>
Retrieves edges using adaptive thresholding.<br>
Applies bilateral filter to the color image to remove noise.<br>
Masks the edged image with the color image to create a cartoon effect.<br>
Displays the original image, grayscale image, smoothed image, edge-detected image, color image, and final cartoon image using matplotlib.<br>
Creates a button to save the cartoonified image.<br>
save(ReSized6, ImagePath): This function saves the cartoonified image. It takes the cartoonified image and the original image path as input, determines the save path based on the original image's directory and a predefined name ("cartoonified_Image"), and saves the image in the appropriate format (maintaining the original extension). It also displays a message box confirming the successful save operation.<br>
upload Button: Initializes a button for triggering the image upload process.<br>
save1 Button: Initializes a button for saving the cartoonified image.<br>
GUI Execution:<br>

Initiates the GUI event loop using top.mainloop().<br>




