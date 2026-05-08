from django.apps import AppConfig

class MonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitor'

    def ready(self):
        # With --noreload, we can just start the thread directly
        from .ros_subscriber import start_ros_thread
        try:
            start_ros_thread()
        except Exception as e:
            print(f"ERROR: Could not start ROS thread: {e}")
