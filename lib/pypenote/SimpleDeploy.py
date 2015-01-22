#!/usr/bin/python

from fabric.api import env, local, cd
from ConfigParser import ConfigParser
import os
import subprocess


config = ConfigParser()
config.read('config.ini')


class GitHubDeploy():
    def __init__(self): 
        env.server = config.get('GitHub', 'host')
        env.user = config.get('GitHub', 'user')
        env.password = config.get('GitHub', 'password')


    def deploy(self, projectpath, article):
        os.chdir(projectpath)

        with cd(projectpath):
            try:
                local('git branch gh-pages', shell=False)

            except:
                pass

            finally:
                local('make html')
                local('ghp-import output')
                local('git checkout master')
                local('git merge gh-pages')
                local('git push --all')