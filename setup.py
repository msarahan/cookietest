from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='cookietest',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Short description",
    author="Full Name",
    author_email='Email Address',
    url='https://github.com/msarahan/cookietest',
    packages=['cookietest'],
    entry_points={
        'console_scripts': [
            'cookietest=cookietest.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='cookietest',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
