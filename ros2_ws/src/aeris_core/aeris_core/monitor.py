import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class AerisMonitor(Node):

    def __init__(self):
        super().__init__("aeris_monitor")

        self.subscription = self.create_subscription(
            String,
            "/aeris/mission_status",
            self.mission_callback,
            10
        )

    def mission_callback(self, message):
        self.get_logger().info(
            f"Mission update received: {message.data}"
        )


def main(args=None):
    rclpy.init(args=args)

    node = AerisMonitor()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
