class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        print(f'{self._position}: POSITION')
        print(self._item)

        if self._item == None:
           if self._position == 0:
               self.swap_item()
               self.move_right()
            else:
                self.position = 0
                
        if self._light == "OFF":
            if self.can_move_right() == True:
                if self.compare_item() == -1 or self.compare_item() == 0:
                    if self.can_move_left() == True:
                        self.move_left()
                        self.swap_item()
                        self._position = 0                       
                elif self.compare_item() == 1:
                    self.move_right()
                elif self.compare_item() == None:
                    self.swap_item()
            else: 
                if self.compare_item() == 1:
                    self.move_right()
                print(f'Are we here? ')

        
        print(f'ITEM: {self._item}')
        return self.sort()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


# I have a robot that can move left and right, turn his light off and on, compare and swap items.
            # I am going to want to Have a sort method that will track Where the None is

# I will write a recursive bubble sort for the robot to use as he traverses the list.
# I will also have the robot slowly go through the list and change numbers as indicated above To do that

    # I will want to have a if statement that checks the light. Which I am using to if the Robot has a None being held. 
        # If the light is on (None is being held) You will want to return the robot to 0 and put it there, taking the number from  position 0 and sorting that way
            # If the robot is holding none and is at 0 you want to swap the items there, move him to the right one 
            # Turn off the light and start your comparissons. 
        # Base case will be logic based on if the none is the last item that we have to swap, if so we will swap the items and return LIST
            # My current Idea for this is to check the 3 numbers to the right and compare them to see if the robot should move forward with more sorting.

    # While the robots light is off(SHould be most of the time)
        # The Robot will be carrying itms from left to right comparing items as he traverses the list swapping as he goes. 
            # If the item in the robots hands is less than the one he is comparing against he will slide to the left one, swap the items and then continue his pass.
                # Ideally with each pass of this the robot will have to make less and less swaps 

        



