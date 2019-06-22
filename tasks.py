from invoke import task

@task
def install(c):
    c.run("git clone https://github.com/mtn/cocoa-eh-hugo-theme.git themes/cocoa-eh ")

@task(install)
def build(c):
    c.run("hugo")

@task
def server(c):
    c.run("hugo server -D")

