import os
import pip
from subprocess import call

def install(package):
    pip.main(['install', package])

if __name__=="__main__":
    avaliable_packages = sorted(["%s==%s" %(i.key,i.version)for i in pip.get_installed_distributions()])

    if "django==1.11" not in avaliable_packages:
        install("Django-1.11-py2.py3-none-any.whl")

    call(["python","manage.py","runserver"])