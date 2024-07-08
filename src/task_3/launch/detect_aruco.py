import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('aruco.mp4')

# Load the Aruco dictionary
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()


# Note: Replace with actual camera calibration parameters for accurate results
cameraMatrix = np.array([[1000, 0, 640],
                         [0, 1000, 360],
                         [0, 0, 1]])
distCoeffs = np.array([0, 0, 0, 0, 0])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect markers
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    if ids is not None:
        # Draw detected markers with IDs
        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        # Estimate pose of each marker
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.1, cameraMatrix, distCoeffs)
        
        # Draw Axis and orientation of each marker
        for i in range(len(ids)):
            cv2.aruco.drawAxis(frame, cameraMatrix, distCoeffs, rvecs[i], tvecs[i], 0.1)
            cv2.putText(frame, f'ID: {ids[i][0]}', (corners[i][0][0][0], corners[i][0][0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
#cv2.destroyAllWindows()


