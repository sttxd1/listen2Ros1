import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage, Image, Imu, CameraInfo
from cv_bridge import CvBridge
import cv2

class Listener(Node):
    def __init__(self):
        super().__init__('Listener')


        self.imu_subscription = self.create_subscription(
            Imu,
            '/camera/imu',
            self.imu_callback,
            10)
        
        self.color_cameraInfo = self.create_subscription(
            CameraInfo,
            '/camera/color/camera_info',
            self.color_cameraInfo_callback,
            10)
        
        self.depth_cameraInfo = self.create_subscription(
            CameraInfo,
            '/camera/depth/camera_info',
            self.depth_cameraInfo_callback,
            10)

        ##compressed rgb
        self.color_subscription = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.color_callback,
            10)
        
        ##compressed depth
        self.depth_subscription = self.create_subscription(
            Image,
            '/camera/depth/image_rect_raw',
            self.depth_callback,
            10)
        
        ##compressed aligned depth
        self.aligned_depth_subscription = self.create_subscription(
            Image,
            '/camera/aligned_depth_to_color/image_raw',
            self.aligned_depth_callback,
            10)

        ##compressed rgb
        self.compr_color_subscription = self.create_subscription(
            CompressedImage,
            '/camera/color/image_raw/compressed',
            self.compr_color_callback,
            10)
        
        ##compressed depth
        self.compr_depth_subscription = self.create_subscription(
            CompressedImage,
            '/camera/depth/image_rect_raw/compressedDepth',
            self.compr_depth_callback,
            10)
        
        ##compressed aligned depth
        self.compr_aligned_depth_subscription = self.create_subscription(
            CompressedImage,
            '/camera/aligned_depth_to_color/image_raw/compressedDepth',
            self.compr_aligned_depth_callback,
            10)
        
        self.bridge = CvBridge()

    def imu_callback(self, data):
        pass
    def color_cameraInfo_callback(self, data):
        pass
    def depth_cameraInfo_callback(self, data):
        pass
    def color_callback(self, data):
        pass
    def depth_callback(self, data):
        pass
    def aligned_depth_callback(self, data):
        pass
    def compr_color_callback(self, data):
        pass
    def compr_depth_callback(self, data):
        pass
    
    def compr_aligned_depth_callback(self, data):
        pass


def main(args=None):
    rclpy.init(args=args)
    listener = Listener()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
