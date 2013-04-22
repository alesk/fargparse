from distutils.core import setup
setup(name='fargparse',
      version='0.2',
      py_modules=['fargparse'],
      author_email='ales.kotnik@gmail.com',
      url='https://github.com/alesk/fargparse.git',
      license='MIT',
      platforms = 'any',
      classifiers=['Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'],
      requires = [
          "argparse", "importlib"]
      )
