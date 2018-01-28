#!/usr/bin/env python3.6
from app import create_app
from flask_script import Manager, Server

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)


@manager.command
def test():
    """
    Runs the unit tests.
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
