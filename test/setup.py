from distutils.core import setup

setup(
    name='discord-error-logger',
    version='1.0',
    packages=['external',
              'internal',
              'discord_logger',
              'discord_logger.external',
              'discord_logger.internal',
              'discord_logger.constants'],
    package_dir={'': 'test'},
    url='',
    license='',
    author='',
    author_email='',
    description=''
)
