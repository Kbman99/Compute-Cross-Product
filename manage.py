from termcolor import colored
import click

from app.core import db
from app import create_app


app = create_app()


@app.cli.command()
def initdb():
    """ Create the SQL database. """
    db.create_all()
    print(colored('The SQL database has been created', 'green'))


@app.cli.command()
@click.confirmation_option(
    prompt='This will erase everything in the database. Do you want to continue?')
def dropdb():
    """ Drop the SQL database. """
    db.drop_all()
    print(colored('The SQL database has been deleted', 'green'))


@app.cli.command()
@click.confirmation_option(
    prompt='This will remove the current database and reinitialize it. Do you want to continue?')
def refreshdb():
    """ Drop then reinitialize the database """
    db.drop_all()
    db.create_all()
    print(colored('The SQL database has been recreated!', 'green'))


if __name__ == '__main__':
    app.cli(host='0.0.0.0')
