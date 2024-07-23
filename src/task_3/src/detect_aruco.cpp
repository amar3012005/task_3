#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/image.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/aruco.hpp>

class ArucoMarkerDetector : public rclcpp::Node {
public:
    ArucoMarkerDetector() : Node("aruco_marker_detector") 
    }
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ArucoMarkerDetector>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
