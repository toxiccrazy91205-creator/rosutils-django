import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.publisher_ = self.create_publisher(String, 'greeting', 10)
        
        # Subscriber to listen for commands from the web
        self.command_sub = self.create_subscription(
            String,
            'cmd',
            self.command_callback,
            10)
            
        self.message_text = 'Hello ROS 2! I am talking from a new project.'
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Talker Node started and ready for smart replies!')

    def command_callback(self, msg):
        received_text = msg.data.lower()
        self.get_logger().info(f'RECIEVED COMMAND: "{msg.data}"')
        
        # --- Automatic Reply Logic ---
        if 'hello' in received_text or 'hi' in received_text:
            self.message_text = "Hello! How can I help you today?"
        elif 'status' in received_text:
            self.message_text = "System Status: All sensors and motors online."
        elif 'move' in received_text:
            self.message_text = "Action: Moving to the target position..."
        elif 'who are you' in received_text:
            self.message_text = "I am a ROS 2 Robot controlled by your Django dashboard!"
        else:
            # Default response
            self.message_text = f"Acknowledged: I received your message '{msg.data}'"
        
        self.get_logger().info(f'AUTOREPLY SET: "{self.message_text}"')

    def timer_callback(self):
        msg = String()
        msg.data = self.message_text
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    talker_node = TalkerNode()
    rclpy.spin(talker_node)
    talker_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
