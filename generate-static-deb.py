import os

package_name = 'piculator-sage-jupyter-mod'
name = 'piculator-sage-jupyter-mod'
desp = 'Mod to sagemath jupyter notebook'
version = input('Please input version')
package_path = f'{package_name}_{version}'
files_path = f'{package_path}/home/pi/sage/sage-9.2/local/lib/python3.7/site-packages/notebook/static/custom'
os.makedirs(files_path,exist_ok=True)
os.system(f'cp -r notebook/** {files_path}')
os.makedirs(f"{package_path}/DEBIAN",exist_ok=True)
control_content = f'''Package: {package_name}
Architecture: all
Name: {name}
Description: {desp}
Version: {version}
Section: base
Depends: piculator-sagemath
Author: Piculator Development Team <piculator@protonmail.com>
Maintainer: Piculator Development Team <piculator@protonmail.com>
HomePage: https://github.com/piculator/piculator-jupyter-mod
'''
ctl_file=open(f'{package_path}/DEBIAN/control',mode='w+')
ctl_file.write(control_content)
ctl_file.close()
for r, d, f in os.walk(package_path):
    os.chmod(r, 0o755)
os.system(f'dpkg-deb -b {package_path}')