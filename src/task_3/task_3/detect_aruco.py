import cv2
import cv2.aruco as aruco

def main():
    # Load the video
    cap = cv2.VideoCapture('aruco.mp4')

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Define the ArUco dictionary and parameters
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect markers
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        # Draw detected markers
        if ids is not None:
            aruco.drawDetectedMarkers(frame, corners, ids)

        # Display the frame
        cv2.imshow('Frame', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

