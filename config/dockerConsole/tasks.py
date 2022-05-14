from django.contrib.auth.models import User
from .models import Container
from celery.task.schedules import crontab



from celery.decorators import task
import subprocess
import os


@task(name="create_container")
def create_container(name, tag):
    print( 'task: creating container ${name}:${tag}')
    source = os.path.dirname(__file__)
    script_path = os.path.join(source, 'dockerCommands/create.sh')
    subprocess.call(['sudo',script_path], '${name} ${tag}')

@task(name="destroy_container")
def delete_container(name, tag):
    print( 'task: deleting container ')
    source = os.path.dirname(__file__)
    script_path = os.path.join(source, 'dockerCommands/delete.sh')
    subprocess.call(['sudo',script_path],'${name} ${tag}')



# @task(name="list_containers")
# def show_containers():
#     print( 'task: show containers ')
#     source = os.path.dirname(__file__)
#     script_path = os.path.join(source, 'dockerCommands/list.sh')
#     subprocess.call(['sudo',script_path])

    
