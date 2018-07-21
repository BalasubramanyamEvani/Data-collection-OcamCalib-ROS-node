ROS node for collecting Images for OcamCalib MATLAB toolbox, for calibration of Omni-Directional Camera.

see :- https://sites.google.com/site/scarabotix/ocamcalib-toolbox

1) Switch on the Ricoh Theta S camera in Live Mode
2) roslaunch launch file in omni_cam launch, it uses the usb_cam package node.
   you can uncomment the image view node, to see the output.
3) To collect the dual fish eye images run the collect.py script in scripts folder.
4) To separated out the images collected run the cv.py script
5) To use the separation and see the result as Image msg in ROS, use publisher.py

