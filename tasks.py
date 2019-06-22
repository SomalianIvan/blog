from invoke import task

@task
def build(c):
    c.run("hugo")

@task
def server(c):
    c.run("hugo server -D")

@task
def clean(c):
    c.run("rm -rf ")

@task
def install(c):
    c.run("git clone https://github.com/mtn/cocoa-eh-hugo-theme.git themes/cocoa-eh ")
