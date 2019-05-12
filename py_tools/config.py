import configparser

config = configparser.ConfigParser()
config.read('../.env')

# section default
default_section = config['default']

APPLICATION_NAME = default_section['application_name']

__all__ = [
    'APPLICATION_NAME'
]