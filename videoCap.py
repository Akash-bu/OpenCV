import cv2 as cv

# Initialize video capture from default webcam (0)
capture = cv.VideoCapture(0)  # 0 means the default webcam

if not capture.isOpened():
    print("Error: Could not open video capture.")
    exit()

# Function to change the resolution of the live feed
def changeRes(width, height):
    capture.set(3, width)  # Set width
    capture.set(4, height)  # Set height

# Change resolution (set this to a value supported by your webcam)
changeRes(640, 480)  # For example, set to 640x480 resolution

# Loop to capture and display video frames
while True:
    # Read frame from the webcam
    ret, frame = capture.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Error: Could not read frame from video capture.")
        break

    # Display the original video feed
    cv.imshow('Video Feed', frame)

    # Break the loop if 'q' is pressed
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
capture.release()
cv.destroyAllWindows()
