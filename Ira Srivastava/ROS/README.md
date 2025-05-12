ira@ira-IdeaPad-Pro-5-14IMH9:~$ source /opt/ros/humble/setup.bash
ira@ira-IdeaPad-Pro-5-14IMH9:~$ mkdir -p ~/ros2_ws/src
ira@ira-IdeaPad-Pro-5-14IMH9:~$ cd ~/ros2_ws
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ source /opt/ros/humble/setup.bash
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ cd src
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src$ ros2 pkg create --build-type ament_python py_talker
going to create a new package
package name: py_talker
destination directory: /home/ira/ros2_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['ira <ira@todo.todo>']
licenses: ['TODO: License declaration']
build type: ament_python
dependencies: []
creating folder ./py_talker
creating ./py_talker/package.xml
creating source folder
creating folder ./py_talker/py_talker
creating ./py_talker/setup.py
creating ./py_talker/setup.cfg
creating folder ./py_talker/resource
creating ./py_talker/resource/py_talker
creating ./py_talker/py_talker/_init_.py
creating folder ./py_talker/test
creating ./py_talker/test/test_copyright.py
creating ./py_talker/test/test_flake8.py
creating ./py_talker/test/test_pep257.py

[WARNING]: Unknown license 'TODO: License declaration'.  This has been set in the package.xml, but no LICENSE file has been created.
It is recommended to use one of the ament license identitifers:
Apache-2.0
BSL-1.0
BSD-2.0
BSD-2-Clause
BSD-3-Clause
GPL-3.0-only
LGPL-3.0-only
MIT
MIT-0
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src$ cd ~/ros2_ws/src/py_talker/py_talker
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ touch talker.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ chmod +x talker.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ nano talker.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ chmod +x talker.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ cd ~/ros2_ws/src/py_talker
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker$ nano setup.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker$ cd ~/ros2_ws
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ colcon build
Starting >>> py_talker
Starting >>> py_talker_listener
Finished <<< py_talker [0.66s]                                                  
Finished <<< py_talker_listener [0.92s]          

Summary: 2 packages finished [1.12s]
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ source install/setup.bash
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ ros2 pkg executables py_talker
py_talker listener
py_talker talker
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ touch listener.py
chmod +x listener.py
nano listener.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ cd ~/ros2_ws/src/py_talker/py_talker
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ touch talker.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ chmod +x talker.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ nano talker.py
bash: ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$: No such file or directory
bash: ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$: No such file or directory
bash: ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$: No such file or directory
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ ^C
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ cd ~/ros2_ws/src/py_talker/py_talker
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ ^C
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$  nano talker.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ mkdir ~/ros2_ws/src/py_talker_listener/launch
mkdir: cannot create directory ‘/home/ira/ros2_ws/src/py_talker_listener/launch’: File exists
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ mkdir ~/ros2_ws/src/py_talker/launch
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/py_talker$ cd ~/ros2_ws/src/py_talker/launch
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/launch$ touch talker_listener.launch.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/launch$ nano talker_listener.launch.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker/launch$ cd ~/ros2_ws
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ colcon build
Starting >>> py_talker
Starting >>> py_talker_listener
Finished <<< py_talker [0.62s]                                                  
Finished <<< py_talker_listener [0.62s]

Summary: 2 packages finished [0.75s]
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ source install/setup.bash
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ ros2 launch py_talker talker_listener.launch.py
file 'talker_listener.launch.py' was not found in the share directory of package 'py_talker' which is at '/home/ira/ros2_ws/install/py_talker/share/py_talker'
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ chmod +x ~/ros2_ws/src/py_talker_listener/launch/talker_listener.launch.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ ~/ros2_ws/src/py_talker/setup.py
bash: /home/ira/ros2_ws/src/py_talker/setup.py: Permission denied
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ cd ~/ros2_ws/src/py_talker_listener
nano setup.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker_listener$ ^C
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker_listener$ cd ~/ros2_ws/src/py_talker         
nano setup.py
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws/src/py_talker$ cd ~/ros2_ws
colcon build
source install/setup.bash
Starting >>> py_talker
Starting >>> py_talker_listener
Finished <<< py_talker [0.61s]                                                  
Finished <<< py_talker_listener [0.61s]

Summary: 2 packages finished [0.74s]
ira@ira-IdeaPad-Pro-5-14IMH9:~/ros2_ws$ ros2 launch py_talker talker_listener.launch.py message:="Your custom message here"