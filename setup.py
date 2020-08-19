from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="paypayopa",
    version="0.3.8",
    description="PayPay OPA SDK",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Team PayPay",
    author_email="opensource@paypay-corp.co.jp",
    license="Apache 2.0",
    project_urls={
        'Documentation': 'https://github.com/paypay/paypayopa-sdk-python/README.md',
        'Source': 'https://github.com/paypay/paypayopa-sdk-python',
    },
    install_requires=["requests", "uuid", "pyjwt"],
    include_package_data=True,
    package_dir={'paypayopa': 'paypayopa',
                 'paypayopa.resources': 'paypayopa/resources',
                 'paypayopa.constants': 'paypayopa/constants'},
    packages=['paypayopa', 'paypayopa.resources', 'paypayopa.constants'],
    keywords='paypay payment gateway japan',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",

        # List of supported Python versions
        # Make sure that this is reflected in .travis.yml as well
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
