from pyniryo import *

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":

    robot_ip_address = 'manual_ip'
    workspace_name = "workspace_1"  # Robot's Workspace Name
    robot = NiryoRobot(robot_ip_address) # Connect to robot

    # Clear collision if detected during a previous movement
    if robot.collision_detected:
        robot.clear_collision_detected()

    robot.calibrate_auto() # Calibrate robot if the robot needs calibration
    robot.update_tool()    # Updating tool
    robot.open_gripper()

    sensor_pin_id = 'DI5'  # Setting variables
    conveyor_id = robot.set_conveyor() # Activating connexion with the Conveyor Belt

    # --- --------- --- #
    # --- YOUR CODE --- #
    # --- --------- --- #

    initial_Pose = [0,0,0,0,0,0]
    observation_Pose = [0.1649,0.0154,0.17,2.714,1.395,2.907]
    colour_Approach_Pose = [-0.003375,0.203157,0.104960,2.391,1.489,-2.35]
    approach_Pick_Pose = [0.24,0.0154,0.08,2.714,1.395,2.907]
    blue_Place_Pose = [0.0938,0.234792,0.021003,2.323,1.464,-2.306]
    red_Place_Pose = [0.000589,0.230293,0.021543,2.994,1.454,-1.68]
    green_Place_Pose = [-0.084164,0.226782,0.019046,-2.38,1.493,-0.829]

    robot.move(initial_Pose)

    #setting values to be multiplied so that each offset for placing is calculated properly
    gPlace = 0
    bPlace = 0
    rPlace = 0

    #loop to go through each token and have them placed in the correct position
    for i in range(5):
        robot.move(observation_Pose)
        robot.run_conveyor(conveyor_id,speed=50,direction=ConveyorDirection.FORWARD)
        while True:
            obj_found, shape_ret, color_ret = robot.vision_pick(workspace_name)
           
            if obj_found:
                robot.stop_conveyor
                robot.move(approach_Pick_Pose)
                robot.close_gripper
                robot.move(observation_Pose)
                robot.move(colour_Approach_Pose)
                if color_ret == GREEN:
                    robot.move(green_Place_Pose.copy_with_offsets(x_offset=0.05 * gPlace))
                    gPlace + 1
                elif color_ret == RED:
                    robot.move(red_Place_Pose.copy_with_offsets(x_offset=0.05 * rPlace))
                    rPlace + 1
                elif color_ret == BLUE:
                    robot.move(blue_Place_Pose.copy_with_offsets(x_offset=0.05 * bPlace))
                    bPlace + 1
                else:
                    break
            robot.open_gripper
            robot.move(colour_Approach_Pose)
        robot.move(initial_Pose)

    robot.unset_conveyor(conveyor_id) # Deactivating connexion with the Conveyor Belt
    robot.close_connection()
