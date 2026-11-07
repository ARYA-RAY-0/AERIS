import rclpy
from rclpy.node import Node

from aeris_interfaces.msg import MissionStatus


class RoutePlanner(Node):

    def __init__(self):
        super().__init__("aeris_route_planner")

        self.subscription = self.create_subscription(
            MissionStatus,
            "/aeris/mission_status",
            self.mission_callback,
            10
        )

        self.last_mission_id = None

    def mission_callback(self, message):

        if message.mission_id == self.last_mission_id:
            return

        self.last_mission_id = message.mission_id

        if message.state != "PLANNING":
            return

        self.get_logger().info(
            f"Generating route for {message.mission_id} | "
            f"Target: {message.target}"
        )

        waypoints = self.generate_route(message.waypoint_count)

        self.get_logger().info(
            f"Generated {len(waypoints)} inspection waypoints."
        )

        for index, waypoint in enumerate(waypoints, start=1):
            self.get_logger().info(
                f"Waypoint {index}: "
                f"x={waypoint[0]:.1f}, "
                f"y={waypoint[1]:.1f}, "
                f"z={waypoint[2]:.1f}"
            )

    def generate_route(self, waypoint_count):

        waypoints = []

        for index in range(waypoint_count):
            x = float(index * 10)
            y = 0.0
            z = 10.0

            waypoints.append((x, y, z))

        return waypoints


def main(args=None):
    rclpy.init(args=args)

    node = RoutePlanner()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
