import os 
def main():
    os.system("ros2 run py_pubsub talker & ros2 run py_pubsub listener")
if __name__ == "__main__":
    main()
