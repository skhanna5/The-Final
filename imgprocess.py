# import cv2

# # Function to find the center and highlight the largest red object in the frame
# def detection(frame):
#     global cx, cy
#     b, g, r = cv2.split(frame)
#     red = cv2.subtract(r, g)
#     # Blur the red channel image
#     blurred = cv2.GaussianBlur(red, (5, 5), 0)
#     # Threshold the blurred image
#     thresh = cv2.threshold(blurred, 125, 255, cv2.THRESH_BINARY)[1]
#     # Find contours in the thresholded image
#     cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     # Find the largest contour (if any)
#     largest_contour = max(cnts, key=cv2.contourArea, default=None)
#     if largest_contour is not None:
#         # Highlight the largest contour
#         cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
#         # Compute the center of the largest contour
#         M = cv2.moments(largest_contour)
#         if M["m00"] != 0:
#             cx = int(M['m10'] / M['m00'])
#             cy = int(M['m01'] / M['m00'])
#             return cx, cy
#     return None

# # Main script
# def capture():
#     # Open the native webcam
#     cap = cv2.VideoCapture(0)
#     while True:
#         # Read a frame from the webcam
#         ret, frame = cap.read()
#         # Find the center of the largest red object and highlight it
#         center = detection(frame)
#         # Live data box
#         cv2.rectangle(frame,(5,5),(320,95),(255,0,255),8)
#         cv2.putText(frame, "X, Y Coordinates:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 6)
#         # Draw a circle at the center and post coordinates if it is found
#         if center is not None:
#             cv2.circle(frame, center, 10, (255, 0, 0), -1)
#             cv2.putText(frame, "Center", (center[0] - 20, center[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 6) #0.5, 2
#             cv2.putText(frame, '(' + str(int(cx)) + ', ' + str(int(cy)) + ')', (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 6)
#         # Display the frame
#         cv2.imshow('Live Video', frame)
#         # Break the loop if 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     # Release the webcam and close all windows
#     cap.release()
#     cv2.destroyAllWindows()


import cv2

# Global variables to store centroid coordinates
cx, cy = None, None

# Function to find the center and highlight the largest red object in the frame
def detection(frame):
    global cx, cy
    b, g, r = cv2.split(frame)
    red = cv2.subtract(r, g)
    # Blur the red channel image
    blurred = cv2.GaussianBlur(red, (5, 5), 0)
    # Threshold the blurred image
    thresh = cv2.threshold(blurred, 125, 255, cv2.THRESH_BINARY)[1]
    # Find contours in the thresholded image
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Find the largest contour (if any)
    largest_contour = max(cnts, key=cv2.contourArea, default=None)
    if largest_contour is not None:
        # Highlight the largest contour
        cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
        # Compute the center of the largest contour
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
    else:
        # Reset centroid coordinates if no contour is found
        cx, cy = None, None

# Main script
def capture():
    # Open the native webcam
    cap = cv2.VideoCapture(0)
    global cx, cy
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        # Find the center of the largest red object and highlight it
        detection(frame)
        # Live data box
        cv2.rectangle(frame,(5,5),(320,95),(255,0,255),8)
        cv2.putText(frame, "X, Y Coordinates:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 6)
        # Draw a circle at the center and post coordinates if it is found
        if cx is not None and cy is not None:
            cv2.circle(frame, (cx, cy), 10, (255, 0, 0), -1)
            cv2.putText(frame, "Center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 6)
            cv2.putText(frame, '(' + str(int(cx)) + ', ' + str(int(cy)) + ')', (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 6)
        # Display the frame
        cv2.imshow('Live Video', frame)
        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

capture()