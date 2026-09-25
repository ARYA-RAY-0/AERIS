import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MissionPublisher(Node):

    def __init__(self):
        super().__init__("aeris_mission_publisher")

        self.publisher = self.create_publisher(
            String,
            "/aeris/mission_status",
            10
        )

        self.timer = self.create_timer(2.0, self.publish_status)

    def publish_status(self):
        message = String()
        message.data = "MISSION: INSPECTION_READY"

        self.publisher.publish(message)

        self.get_logger().info(
            f"Published: {message.data}"
        )


def main(args=None):
    rclpy.init(args=args)

    node = MissionPublisher()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
