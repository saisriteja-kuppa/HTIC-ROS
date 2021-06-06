# RViz

User can see his custom robot in rviz file with GUI option depending on the constraints in the URDF file.
The urdf file is to be placed in the urdf folder inside hticros. Now go to the python folder and open a terminal. Then run the python script as shown below.

```
python rviz_viewer.py -robot <urdf_file_name>
```


|    Robot      | filename      |
| ------------- | ------------- |
| Staubli       | tx160         |
| UR5           | ur5           |
| Kuka          | kr16_2        |
| Elfin         | elfin5        |

The above one are those that come up with cloning this repo. Once you the above python file the visual looks like the image below.
![rviz_viewer](https://github.com/saisriteja-kuppa/HTIC-ROS/blob/main/images/rviz_viewer.png)
