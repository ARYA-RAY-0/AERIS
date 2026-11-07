import rclpy
from rclpy.node import Node

from aeris_interfaces.msg import MissionStatus


class MissionPublisher(Node):

    def __init__(self):
        super().__init__("aeris_mission_publisher")

        self.publisher = self.create_publisher(
            MissionStatus,
            "/aeris/mission_status",
            10
        )

        self.timer = self.create_timer(2.0, self.publish_status)

    def publish_status(self):
        message = MissionStatus()

        message.mission_id = "INSPECT-001"
        message.target = "BRIDGE_DECK_A"
        message.state = "PLANNING"
        message.priority = 2
        message.waypoint_count = 18
        message.progress = 0.0

        self.publisher.publish(message)

        self.get_logger().info(
            f"Mission {message.mission_id} | "
            f"Target: {message.target} | "
            f"State: {message.state}"
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
    
