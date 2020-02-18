from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='hello-world',
    version='0.0',
    description='ridiculous tinkering',
    author='John Edwards',
    author_email='notavailableformisuse@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)