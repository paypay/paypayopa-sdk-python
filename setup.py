
from setuptools import setup, find_packages

package_name = "copilot_example_pip_travis"
package_version = "1.0.0"

setup(
    name=package_name,
    version=package_version,
    author="Black Duck CoPilot",
    author_email="copilot@blackducksoftware.com",
    url="https://github.com/BlackDuckCoPilot/example-pip-travis",
    install_requires=["requests", "numpy", "Django==1.9.6"],
    entry_points={
      'console_scripts': [
          'example-pip-travis=Main:main'
      ]
    }
)