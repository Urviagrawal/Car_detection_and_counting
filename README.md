# Car_detection_and_counting
In this repo I am sharing a simple code for detecting and counting cars.


# Methodology:

# 1: For Object detection:

	1) I have used a traffic monitoring video with the aim to detect cars.
	2) For object detection I have selected Haar Cascade classifier since it has high level of precision and require fewer 		        attempts to get a woking model. 
	3) I have used pre-trained cars.xml model.
	4) A loop has been created to read the frames and detect objects in each frame.
	5) Rectangular bounding box is created to identify object in video.


# 2: For counting object:

	1) A loop is created to count the total number of object detected in every 5th frame.
	2) This is done by counting actual bounding boxes detected in each frame.
	3) Using Pandas the results are stored into CSV file in example.csv.
	4) Number of frames and number of objects detected are displayed on screen.


# Files added

1) cars.xml: Pre-trained xml file.

2) Vehicles_detection_final.py: OpenCV Python file for Vehicle detection.

3) video.avi: Video file used for object detection.

4) example.csv: CSV file with results.
