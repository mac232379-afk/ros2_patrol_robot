from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy
# from tf_transformations import quaternion_from_euler   # 新增导入
# import math
def main():
    rclpy.init()
    nav = BasicNavigator() # 节点
    init_pose = PoseStamped()
    init_pose.header.frame_id = "map"
    init_pose.header.stamp = nav.get_clock().now().to_msg()
    init_pose.pose.position.x = 0.0
    init_pose.pose.position.y = 0.0
    # 用欧拉角 -> 四元数转换（此处 yaw=0，等价于原来的 w=1.0）
    # q = quaternion_from_euler(0.0, 0.0, 0.0)          # 返回 (x, y, z, w)
    # init_pose.pose.orientation.x = q[0]
    # init_pose.pose.orientation.y = q[1]
    # init_pose.pose.orientation.z = q[2]
    # init_pose.pose.orientation.w = q[3]
    init_pose.pose.orientation.w = 1.0
    nav.setInitialPose(init_pose)
    nav.waitUntilNav2Active() # 等待导航可用
    rclpy.spin(nav)
    rclpy.shutdown()