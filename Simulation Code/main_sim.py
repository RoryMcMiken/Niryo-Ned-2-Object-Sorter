from helpers_sim import *
""" 
 # ----------------------------------------------------------------------------------------------------------------------------------------------------------
 # ----------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__=="__main__": 

     robot = NiryoRobot()
     robot.open_gripper()

     initial_pose = robot.get_target_pose('Initial Pose')         # [380.221, 0.0, 429.030, 0.0, 0.003, 0.0]
     observation_pose = robot.get_target_pose('Observation Pose') # [235.0, 160.0, 200.0, 0.0, 90.0, 35.0]
     approach_pose = robot.get_target_pose('Approach Pick Pose')       # [10.0, 325.0, 120.0, 0.0, 90.0, 90.0]
     red_place_pose = robot.get_target_pose('Red Place Pose')     # [80.0, 325.0, 27.5, 0.0, 90.0, 90.0]
     green_place_pose = robot.get_target_pose('Green Place Pose') # [10.0, 325.0, 27.5, 0.0, 90.0, 90.0]
     blue_place_pose = robot.get_target_pose('Blue Place Pose')   # [-60.0, 325.0, 27.5, 0.0, 90.0, 90.0]

     # --- --------- --- #
     # --- YOUR CODE --- #
     # --- --------- --- #

     initial_joints = robot.inverse_kinematics(initial_pose)
     #print(initial_pose)
     #print(initial_joints)
     #print(robot.forward_kinematics(initial_joints))
     #observation_joints = robot.inverse_kinematics(observation_pose)
     #print(observation_joints)
     #robot.move_joints(observation_joints)
     #robot.move_joints(robot.inverse_kinematics(initial_pose))
    
     # Task 1 - find joint angles of initial pose
     initial_joints = robot.inverse_kinematics(initial_pose)
     print("1: " + str(initial_joints))

     # Task 2 - find joint angles of observation pose and move there
     observation_joints = robot.inverse_kinematics(observation_pose)
     print("2: " + str(observation_joints))
     robot.move_joints(observation_joints)

     # Task 3 - Jacobian matrix of observation pose
     print("3: " + str(robot.jacobian_matrix(observation_joints)))

     # Task 4 - Place object on convayor


   
     # Task 7 - return to start 
     #robot.move_joints(initial_joints)
     robot.close_connection()
from helpers_sim import * """

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":

    robot = NiryoRobot()
    robot.open_gripper()

    initial_pose = robot.get_target_pose('Initial Pose')         # [380.221, 0.0, 429.030, 0.0, 0.003, 0.0]
    observation_pose = robot.get_target_pose('Observation Pose') # [235.0, 160.0, 200.0, 0.0, 90.0, 35.0]
    approach_pose = robot.get_target_pose('Approach Pick Pose')  # [10.0, 325.0, 120.0, 0.0, 90.0, 90.0]
    red_place_pose = robot.get_target_pose('Red Place Pose')     # [80.0, 325.0, 27.5, 0.0, 90.0, 90.0]
    green_place_pose = robot.get_target_pose('Green Place Pose') # [10.0, 325.0, 27.5, 0.0, 90.0, 90.0]
    blue_place_pose = robot.get_target_pose('Blue Place Pose')   # [-60.0, 325.0, 27.5, 0.0, 90.0, 90.0]
    approachPlace_pose = robot.get_target_pose('Approach Place Pose')

    # --- --------- --- #
    # --- YOUR CODE --- #
    # --- --------- --- #

    initial_joints = robot.inverse_kinematics(initial_pose)

    observation_joints = robot.inverse_kinematics(observation_pose)

    #print(robot.jacobian_matrix(observation_joints))

    for x in range(6):
        print("initial :" + str(robot.inverse_kinematics(initial_pose)))
        robot.move_joints(observation_joints)
        print("Observation :" + str(robot.inverse_kinematics(observation_pose)))
       
        robot.put_on_conveyor()
        robot.run_conveyor()

        while True:
            if robot.detect_part() == True:
                robot.stop_conveyor()
                break
       
        block_position = robot.get_color_and_pose()
        #print(block_position)
        block_colour = block_position[0]
        block_position = block_position[1]
        robot.move_joints(robot.inverse_kinematics(approach_pose))
        print("Approach Pick :" + str(robot.inverse_kinematics(approach_pose)))

        #print(block_position)

        robot.move_joints(robot.inverse_kinematics(block_position))
        print("Object :" + str(robot.inverse_kinematics(block_position)))
        robot.close_gripper()   # Close gripper around block
        robot.move_joints(observation_joints)
        print("Observation :" + str(robot.inverse_kinematics(observation_pose)))
        robot.move_joints(robot.inverse_kinematics(approachPlace_pose))
        print("Approach place :" + str(robot.inverse_kinematics(approachPlace_pose)))

        if block_colour == "BLUE":
            robot.move_joints(robot.inverse_kinematics(blue_place_pose))
            print("Blue :" + str(robot.inverse_kinematics(blue_place_pose)))
        elif block_colour == "GREEN":
            robot.move_joints(robot.inverse_kinematics(green_place_pose))
            print("Green :" + str(robot.inverse_kinematics(green_place_pose)))
        elif block_colour == "RED":
            robot.move_joints(robot.inverse_kinematics(red_place_pose))
            print("Red :" + str(robot.inverse_kinematics(red_place_pose)))
        else:
            print("Colour not recognised")
       
        robot.open_gripper()
        robot.move_joints(robot.inverse_kinematics(approachPlace_pose))
        print("Approach place :" + str(robot.inverse_kinematics(approachPlace_pose)))
    robot.move_joints(robot.inverse_kinematics(initial_pose))
    print("initial :" + str(robot.inverse_kinematics(initial_pose)))
robot.close_connection()