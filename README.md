# soybot_simulator
Simulator for soybot robot using Gazebo.
This package contains the soybot robot and its agricultural environment in Gazebo.

## Installing the model
Previouly, download the robot model from <https://github.com/bettoigor/soybot_model.git>, and install it following the instruction in the README file.

Before this, clone this repository to your ros workspace and run ```catkin_make``` command to compile the package.


## Testing the model
The model can be launched from the launch file ```soybot_simulator.launch```, using the following command:
```
roslaunch soybot_model soybot_model.launch
```
Before this, Gazebo will be launched and the simulation environment can be seen.
![Configurator](/doc/soybot_model_1.jpg)

## Checking the Environment
### Checking the published topics
To check all the topics type:

```
rostopic list
```

### Send control commands to the robot
The robot is controlled using the topic cmd_vel, that can be tested using the following command:
```
rostopic pub -1 /soybot/cmd_vel geometry_msgs/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: -0.0"
```
where x and z are the linear and angular velocities, respectively.
![Configurator](/doc/soybot_model_v1.mp4)

### Show image
It is possible to see the images generated by the simulator using ros image view:
```
rosrun image_view image_view image:=image_topic
```
where ```image_topic``` is the desired topic.
![Configurator](/doc/soybot_model_4.jpg)

