from setuptools import setup, find_packages
from distutils.extension import Extension
import subprocess
import os
import os.path
import shutil
import platform

import packaging.tags

sys_tag = packaging.tags.sys_tags().__next__()
system_type = sys_tag.platform

license_text = b''
with open('LICENSE', 'rb') as fd:
    license_text = license_text + fd.read()
# with open(os.path.join('licenses', 'LICENSE.append.txt'), 'rb') as fd:
#     license_text = license_text + fd.read()
with open(os.path.join('pptk', 'LICENSE'), 'wb') as fd:
    fd.write(license_text)

def make_mod(x):
    if 'win' in system_type.lower():
        return x + '.pyd'
    elif "linux" in system_type.lower():
        return x + '.so'
    elif 'macos' in system_type.lower():
        return x + '.so'
    else:
        raise RuntimeError('Unknown system type %s' % system_type)


def make_lib(x, version_suffix=''):
    if 'win' in system_type.lower():
        return x + '.dll'
    elif "linux" in system_type.lower():
        return 'lib' + x + '.so' + version_suffix
    elif 'macos' in system_type.lower():
        return 'lib' + x + '.dylib'
    else:
        raise RuntimeError('Unknown system type %s' % system_type)


def make_exe(x):
    if system_type == 'Windows':
        return x + '.exe'
    else:
        return x


def list_libs():
    libs_dir = os.path.join('pptk', 'libs')
    exclude_list = ['Makefile', 'cmake_install.cmake']
    return [f for f in os.listdir(libs_dir)
            if os.path.isfile(os.path.join(libs_dir, f))
            and f not in exclude_list]


setup(
    name='pptk',
    version='0.1.1',
    description='A Python package for facilitating point cloud processing.',
    author='HERE Europe B.V.',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License'],
    license='MIT',
    install_requires=['numpy'],
    project_urls={
        'Source': 'https://github.com/heremaps/pptk'},
    packages=find_packages(),
    package_data={
        'pptk': [
            os.path.join('libs', f) for f in list_libs()] + [
            'LICENSE',
            os.path.join('libs',
                         'qt_plugins', 'platforms', make_lib('*', '*')),
            os.path.join('libs',
                         'qt_plugins', 'xcbglintegrations', make_lib('*', '*'))
            ],
        'pptk.kdtree': [make_mod('kdtree')],
        'pptk.processing.estimate_normals': [make_mod('estimate_normals')],
        'pptk.vfuncs': [make_mod('vfuncs')],
        'pptk.viewer': [make_exe('viewer'), 'qt.conf']},
    options={'bdist_wheel': {
        'python_tag': sys_tag.interpreter,
        'plat_name': sys_tag.platform}})
