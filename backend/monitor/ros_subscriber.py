import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading

# We import the model inside the callback to avoid startup issues
def update_db_message(text):
    from monitor.models import RobotStatus
    # Get the first record or create it
    status, created = RobotStatus.objects.get_or_create(id=1)
    status.last_message = text
    status.save()

cmd_publisher = None

class DjangoNode(Node):
    def __init__(self):
        super().__init__('django_node')
        self.subscription = self.create_subscription(
            String,
            'greeting',
            self.listener_callback,
            10)
        
        self.publisher_ = self.create_publisher(String, 'cmd', 10)
        global cmd_publisher
        cmd_publisher = self.publisher_
        self.get_logger().info('>>> DJANGO ROS NODE ACTIVE (DB MODE) <<<')

    def listener_callback(self, msg):
        print(f"WEB_LOG: Saving to DB: {msg.data}")
        try:
            update_db_message(msg.data)
        except Exception as e:
            print(f"WEB_LOG ERROR: DB save failed: {e}")

def send_ros_command(text):
    global cmd_publisher
    if cmd_publisher:
        msg = String()
        msg.data = text
        cmd_publisher.publish(msg)
        return True
    return False

def start_ros_thread():
    def run_ros():
        if not rclpy.ok():
            rclpy.init()
        node = DjangoNode()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

    thread = threading.Thread(target=run_ros, daemon=True)
    thread.start()
