from setuptools import find_namespace_packages, setup

with open('./readme.md') as f:
    long_description = f.read()

setup(
    name='unified',
    version='1.0.0',
    license='PRIVATE',
    url='https://finder.io', 
    author='Manohar Chapalamadugu',
    author_email='manohar.chapalamadugu@500apps.com',
    description='unified2 app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    zip_safe=False,
    keywords = ['unified'],
    install_requires=[
        'werkzeug',
        'boto3',
        'flask',
        'flask-cors',
        'flask-jwt-extended',
        'flask-httpauth',
        'flask-apiexceptions',
        'waitress',
        'mysql-connector-python',
        'requests',
        'requests_oauthlib',
        'cachetools',
        'aiohttp',
        'PyJWT<2.0,>=1.6.4',
        'distro',
        'psutil',
        'feedparser',
        # 'https://github.com/mobolic/facebook-sdk/archive/v3.1.0.zip',
        'python-twitter',
        'names-dataset',
        'PyYAML',
        'python-json-logger',
        'Flask-Log-Request-ID',
    ],
    package_data = {
        '': ['*.txt'],
    },
    packages=find_namespace_packages()
)