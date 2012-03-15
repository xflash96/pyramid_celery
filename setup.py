import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = ['pyramid', 'celery']

setup(name='pyramid_celery',
      version='0.1',
      description='Celery integration with pyramid',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      author='Po-Wei Wang',
      author_email='xflash96@gmail.com',
      url='https://github.com/xflash96/pyramid_celery',
      keywords='paste pyramid celery message queue amqp job task distributed mongodb',
      license='BSD',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires + ['pytest', 'mock'],
      test_suite="pyramid_celery",
      entry_points = """\
        [console_scripts]
        pceleryd = pyramid_celery.celeryd:main
      """,
      )

