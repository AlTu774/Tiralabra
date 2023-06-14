from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
	ctx.run("poetry pytest src", pty=True)
