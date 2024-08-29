from setuptools import find_packages, setup
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='flask-app-prod-pipeline',
    version='1.0.0',
    description='A Flask web app with database interaction, authentication, rate limiting, and CI/CD pipeline integration.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    entry_points={
        'console_scripts': [
            'run-app = run:app.run',
        ],
    },
)