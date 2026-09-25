import rclpy
from rclpy.node import Node


class AerisHeartbeat(Node):

    def __init__(self):
        super().__init__("aeris_heartbeat")
        self.timer = self.create_timer(1.0, self.publish_heartbeat)

    def publish_heartbeat(self):
        self.get_logger().info("AERIS system heartbeat: ONLINE")


def main(args=None):
    rclpy.init(args=args)

    node = AerisHeartbeat()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
