from django.shortcuts import render
from django.http import Http404
from robotInventory.models import Robot


def index(request):
    robots = Robot.objects.exclude(amount=0)
    return render(request, 'RobotInventory/index.html', {
        'robots': robots,
    })


def item_detail(request, id):
    try:
        robot = Robot.objects.get(id=id)
    except Robot.DoesNotExist:
        raise Http404('This robot does not exist')
    return render(request, 'RobotInventory/item_detail.html', {
        'robot': robot
    })
