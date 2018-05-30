try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    
setup(
    name='wagtail-ckeditor',
    version='0.9',
    description='CKEditor widget for Wagtail CMS',
    author='Martin Mastny',
    author_email='martin.mastny@vscht.cz',
    packages=find_packages(),
    install_requires=['wagtail'],
    include_package_data=True
)
