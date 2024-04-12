# import rclpy
# from rclpy.node import Node
# from sensor_msgs.msg import CompressedImage, Image, Imu, CameraInfo
# from cv_bridge import CvBridge
# from rclpy.qos import qos_profile_sensor_data
# import cv2

# class Listener(Node):
#     def __init__(self):
#         super().__init__('Listener')


#         self.imu_subscription = self.create_subscription(
#             Imu,
#             '/camera/imu',
#             self.imu_callback,
#             qos_profile=qos_profile_sensor_data)
        
#         self.color_cameraInfo_sub = self.create_subscription(
#             CameraInfo,
#             '/camera/color/camera_info',
#             self.color_cameraInfo_callback,
#             10)
        
#         self.depth_cameraInfo_sub = self.create_subscription(
#             CameraInfo,
#             '/camera/depth/camera_info',
#             self.depth_cameraInfo_callback,
#             10)

#         ##compressed rgb
#         self.color_subscription = self.create_subscription(
#             Image,
#             '/camera/color/image_raw',
#             self.color_callback,
#             10)
        
#         ##compressed depth
#         self.depth_subscription = self.create_subscription(
#             Image,
#             '/camera/depth/image_rect_raw',
#             self.depth_callback,
#             10)
        
#         ##compressed aligned depth
#         self.aligned_depth_subscription = self.create_subscription(
#             Image,
#             '/camera/aligned_depth_to_color/image_raw',
#             self.aligned_depth_callback,
#             10)

#         ##compressed rgb
#         self.compr_color_subscription = self.create_subscription(
#             CompressedImage,
#             '/camera/color/image_raw/compressed',
#             self.compr_color_callback,
#             10)
        
#         ##compressed depth
#         self.compr_depth_subscription = self.create_subscription(
#             CompressedImage,
#             '/camera/depth/image_rect_raw/compressedDepth',
#             self.compr_depth_callback,
#             10)
        
#         ##compressed aligned depth
#         self.compr_aligned_depth_subscription = self.create_subscription(
#             CompressedImage,
#             '/camera/aligned_depth_to_color/image_raw/compressedDepth',
#             self.compr_aligned_depth_callback,
#             10)
        
#         self.bridge = CvBridge()

#     def imu_callback(self, data):
#         return
#     def color_cameraInfo_callback(self, data):
#         return
#     def depth_cameraInfo_callback(self, data):
#         return
#     def color_callback(self, data):
#         return
#     def depth_callback(self, data):
#         return
#     def aligned_depth_callback(self, data):
#         return
#     def compr_color_callback(self, data):
#         return
#     def compr_depth_callback(self, data):
#         return
    
#     def compr_aligned_depth_callback(self, data):
#         return


# def main(args=None):
#     rclpy.init(args=args)
#     listener = Listener()
#     rclpy.spin(listener)
#     listener.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, qos_profile_sensor_data
from sensor_msgs.msg import Image, CompressedImage, CameraInfo, Imu

class Listener(Node):
    def __init__(self):
        super().__init__('listener_node')

        # QoS Profile for Camera Info might not need to be as robust as image data
        camera_info_qos = QoSProfile(depth=10, reliability=rclpy.qos.QoSReliabilityPolicy.RELIABLE)

        # More robust QoS for high-frequency image data
        image_data_qos = QoSProfile(depth=10, reliability=rclpy.qos.QoSReliabilityPolicy.RELIABLE)


        self.imu_subscription = self.create_subscription(
             Imu,
             '/camera/imu',
             self.imu_callback,
             qos_profile= qos_profile_sensor_data)

        # Subscriptions to camera info topics
        self.color_cameraInfo_sub = self.create_subscription(
            CameraInfo,
            '/camera/color/camera_info',
            self.color_cameraInfo_callback,
            camera_info_qos)
        
        self.depth_cameraInfo_sub = self.create_subscription(
            CameraInfo,
            '/camera/depth/camera_info',
            self.depth_cameraInfo_callback,
            camera_info_qos)

        # Subscriptions to uncompressed image topics
        self.color_subscription = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.color_callback,
            image_data_qos)
        
        # self.depth_subscription = self.create_subscription(
        #     Image,
        #     '/camera/depth/image_rect_raw',
        #     self.depth_callback,
        #     image_data_qos)
        
        self.aligned_depth_subscription = self.create_subscription(
            Image,
            '/camera/aligned_depth_to_color/image_raw',
            self.aligned_depth_callback,
            image_data_qos)

        # Subscriptions to compressed image topics
        self.compr_color_subscription = self.create_subscription(
            CompressedImage,
            '/camera/color/image_raw/compressed',
            self.compr_color_callback,
            image_data_qos)
        
        # self.compr_depth_subscription = self.create_subscription(
        #     CompressedImage,
        #     '/camera/depth/image_rect_raw/compressedDepth',
        #     self.compr_depth_callback,
        #     image_data_qos)
        
        self.compr_aligned_depth_subscription = self.create_subscription(
            CompressedImage,
            '/camera/aligned_depth_to_color/image_raw/compressedDepth',
            self.compr_aligned_depth_callback,
            image_data_qos)

    # Callback functions for each subscription
    def color_cameraInfo_callback(self, msg):
        pass
    
    def depth_cameraInfo_callback(self, msg):
        pass
    
    def color_callback(self, msg):
        pass
    
    def depth_callback(self, msg):
        pass
    
    def aligned_depth_callback(self, msg):
        pass
    
    def compr_color_callback(self, msg):
        pass
    
    def compr_depth_callback(self, msg):
        pass
    
    def compr_aligned_depth_callback(self, msg):
        pass

def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
