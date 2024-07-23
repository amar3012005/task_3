#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/image.hpp>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/aruco.hpp>

class ArucoMarkerDetector : public rclcpp::Node {
public:
    ArucoMarkerDetector() : Node("aruco_marker_detector") {
        image_subscription_ = this->create_subscription<sensor_msgs::msg::Image>(
            "camera/image_raw", 10, std::bind(&ArucoMarkerDetector::image_callback, this, std::placeholders::_1));
    
        cv::namedWindow("Aruco Markers", cv::WINDOW_AUTOSIZE);
    }

    ~ArucoMarkerDetector() 
        cv::destroyWindow("Aruco Markers");
    }

private:
    void image_callback(const sensor_msgs::msg::Image::SharedPtr msg) {
    
        cv::Mat frame;
        try {
            frame = cv_bridge::toCvShare(msg, "bgr8")->image;
        } catch (cv_bridge::Exception& e) {
            RCLCPP_ERROR(this->get_logger(), "cv_bridge exception: %s", e.what());
            return;
        }
        std::vector<int> marker_ids;
        std::vector<std::vector<cv::Point2f>> marker_corners;
        cv::Ptr<cv::aruco::Dictionary> dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_1000);
        cv::aruco::detectMarkers(frame, dictionary, marker_corners, marker_ids);

        
        if (!marker_ids.empty()) {
            cv::aruco::drawDetectedMarkers(frame, marker_corners, marker_ids);
        }

    
        cv::imshow("Aruco Markers", frame);
        cv::waitKey(1);
    }

    rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr image_subscription_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ArucoMarkerDetector>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
