import subprocess
import sys


def installed_packages():
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    return [r.decode().split('==')[0] for r in reqs.split()]


def install_dependencies():
    print('Checking dependencies are installed')
    if 'requests' not in installed_packages():
        print("Missing dependency 'Requests'. Installing:")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    print('All dependencies installed')

