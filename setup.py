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
    package_dir={'src': 'test'},
    url='https://github.com/JesseLeung97/discord-error-logger/',
    license='',
    author='',
    author_email='',
    description=''
)
