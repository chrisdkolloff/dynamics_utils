from setuptools import setup, find_packages

setup(
    name='dynamics_utils',
    author='chrisdkolloff',
    author_email='chrisdkolloff@gmail.com',
    description='Utils for dealing with dynamic data (MSM, NMR, etc.)',
    url='https://github.com/chrisdkolloff/dynamics_utils.git',
    version='0.0',
    packages=['dynamics_utils'],
    install_requires=[
        'numpy', 'torch'
    ],
    py_modules=['dynamics_utils'],
)