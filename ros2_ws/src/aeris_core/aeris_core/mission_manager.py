import rclpy
from rclpy.node import Node

from aeris_interfaces.msg import MissionStatus


class MissionManager(Node):

    def __init__(self):
        super().__init__("aeris_mission_manager")

        self.subscription = self.create_subscription(
            MissionStatus,
            "/aeris/mission_status",
            self.mission_callback,
            10
        )

        self.current_state = "IDLE"
        self.last_mission_id = None
        self.last_message_state = None

    def mission_callback(self, message):

        if (
            message.mission_id == self.last_mission_id
            and message.state == self.last_message_state
        ):
            return

        self.last_mission_id = message.mission_id
        self.last_message_state = message.state

        self.get_logger().info(
            f"Received mission {message.mission_id} | "
            f"State: {message.state} | "
            f"Target: {message.target}"
        )

        if message.state == "PLANNING":
            self.handle_planning(message)

    def handle_planning(self, message):

        if message.waypoint_count == 0:
            self.get_logger().warning(
                "Mission rejected: no waypoints provided."
            )
            self.current_state = "REJECTED"
            return

        self.current_state = "ROUTE_GENERATION"

        self.get_logger().info(
            f"Mission {message.mission_id} validated."
        )

        self.get_logger().info(
            "Mission state transition: "
            "PLANNING -> ROUTE_GENERATION"
        )


def main(args=None):
    rclpy.init(args=args)

    node = MissionManager()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
