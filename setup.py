# Copyright 2019 Atalaya Tech, Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

import versioneer

with open("README.md", "r", encoding="utf8") as f:
    long_description = f.read()

install_requires = [
    "aiohttp",
    "alembic",
    "urllib3<=1.25.11",
    "boto3",
    "cerberus",
    "certifi",
    "click>=7.0",
    "configparser",
    "docker",
    "flask",
    "grpcio",
    "gunicorn",
    "humanfriendly",
    "numpy",
    "packaging",
    "prometheus_client",
    "protobuf>=3.8.0,<3.19",
    "psutil",
    "py_zipkin",
    # python-dateutil required by pandas and boto3, this makes sure the version
    # works for both
    "python-dateutil>=2.7.3,<3.0.0",
    "python-json-logger",
    "requests",
    "ruamel.yaml>=0.15.0",
    "sqlalchemy-utils<0.36.8",
    "sqlalchemy>=1.3.0,<1.4.0",
    "tabulate",
    'contextvars;python_version < "3.7"',
    'dataclasses;python_version < "3.7"',
    "chardet",
]

install_requires = [
    "alembic",
    "packaging",
    "boto3",
    "psutil",
    "cerberus",
    "sqlalchemy",
    "sqlalchemy-utils",
    "tabulate",
    "humanfriendly",
    "flask",
    "chardet",
    "numpy",
    "multidict",
    "requests",
    "python-json-logger",
    "ruamel.yaml",
    "werkzeug",
    "protobuf>=3.8.0,<3.19",
    "prometheus_client"
]

setuptools.setup(
    name="bentoml",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="bentoml.org",
    author_email="contact@bentoml.ai",
    description="A framework for machine learning model serving",
    long_description=long_description,
    license="Apache License 2.0",
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    url="https://github.com/ersilia-os/ersilia-bentoml",
    packages=setuptools.find_packages(exclude=["tests*"]),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6.1",
    entry_points={"console_scripts": ["bentoml=bentoml.cli:cli"]},
    project_urls={
        "Bug Reports": "https://github.com/bentoml/BentoML/issues",
        "BentoML User Slack Group": "https://bit.ly/2N5IpbB",
        "Source Code": "https://github.com/ersilia/bentoml-ersilia",
    },
    include_package_data=True,  # Required for '.cfg' files under bentoml/config
)
