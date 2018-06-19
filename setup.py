from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='lazy_set',
    version='1.4.5',
    description='A collection that tries to imitate a "lazy" difference and union of sets.',
    url='https://github.cs.huji.ac.il/aviv-yaish/PHANTOM/tree/master/lazy_set',
    author='Aviv Yaish',
    author_email='aviv.yaish@mail.huji.ac.il',
    packages=['lazy_set'],
    long_description=readme(),
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
