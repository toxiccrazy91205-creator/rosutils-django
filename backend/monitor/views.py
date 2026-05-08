from django.shortcuts import render
from django.http import JsonResponse
from .ros_subscriber import send_ros_command
from .models import RobotStatus
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'monitor/index.html')

def get_latest_message(request):
    # Fetch from database
    status = RobotStatus.objects.filter(id=1).first()
    message = status.last_message if status else "Waiting for robot..."
    return JsonResponse({'message': message})

@csrf_exempt
def send_command(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', 'Web Command Received!')
        success = send_ros_command(text)
        return JsonResponse({'status': 'success' if success else 'failed'})
    return JsonResponse({'status': 'invalid_method'}, status=400)
