from setuptools import find_packages, setup

setup(
    name='monitor-exporter',
    version='0.0.3',
    packages=find_packages(),
    author='thenodon',
    author_email='anders@opsdis.com',
    url='https://github.com/opsdis/monitor-exporter',
    license='GPLv3',
    include_package_data=True,
    zip_safe=False,
)
