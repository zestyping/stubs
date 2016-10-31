from setuptools import find_packages, setup

setup(
    name='stubs',
    version='1.0.0',
    description='Tools for setting up stubs and mocks.',
    author='Ka-Ping Yee',
    author_email='zestyping@gmail.com',
    url='http://github.com/zestyping/stubs',
    license='Apache 2.0',
    keywords='development testing mocking',
    packages=find_packages(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
)
