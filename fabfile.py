from fabric.api import run, env, sudo, cd, prefix

env.hosts = ['45.76.233.87']
env.user = 'ryan'

DIR = '/home/ryan/Django-exercise'
VENV = 'source /home/ryan/.virtualenvs/dj-exercise/bin/activate && source SECRETS.env'

def start ():
  with cd(DIR):
    with prefix(VENV):
      run('pm2 start uwsgi -- --ini uwsgi.ini > start.log')

def stop ():
  run('pm2 stop all > stop.log')

def deploy ():
  with cd(DIR):
    run('git pull')

    with prefix(VENV):
      run('pip install -r requirements.txt  > install.log')

    run('pm2 restart all > restart.log')

def hello ():
  print("Hello")
