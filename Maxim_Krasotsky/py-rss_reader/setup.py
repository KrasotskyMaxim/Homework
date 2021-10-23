"""contains setup settings for creating an application using setuptools"""

from setuptools import setup, find_packages

"""variables for setup settings"""
VERSION = "4.0"
DESCRIPTION = "RSS Parser"
LONG_DESCRIPTION = "Python RSS-feeds parser using python 3.9"


"""contains all the necessary settings"""
setup(
    name="rss-reader",
    version=VERSION,
    author="Maxim Krasotsky",
    author_email="krasotskiy.maksim@mail.ru",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages('rss_package'),
    include_package_data=True,
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords=['python', 'feed parser'],
    entry_points={
        'console_scripts': ['rss_reader = rss_reader:main']
    }
)