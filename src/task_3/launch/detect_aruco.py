import cv2
import numpy as np

cap = cv2.VideoCapture('aruco.mp4')

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()

cameraMatrix = np.array([[1000, 0, 640],
                         [0, 1000, 360],
                         [0, 0, 1]])
distCoeffs = np.array([0, 0, 0, 0, 0])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None:
        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.1, cameraMatrix, distCoeffs)

        for i in range(len(ids)):
            cv2.aruco.drawAxis(frame, cameraMatrix, distCoeffs, rvecs[i], tvecs[i], 0.1)
            cv2.putText(frame, f'ID: {ids[i][0]}', (corners[i][0][0][0], corners[i][0][0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



