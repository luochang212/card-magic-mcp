import nox


@nox.session
def tests(session):
    session.install('pytest')
    session.install('-e', '.')
    session.run('pytest')


@nox.session
def lint(session):
    session.install('flake8')
    session.install('flake8-import-order')
    session.run('flake8', '--import-order-style', 'google')
