"""
Runway problem as defined in the README
"""
import math

class BinarySearchNode:
    def __init__(self, x, parent=None):
        self.x = x
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, that_x):
        # build / update the left tree
        if self.x > that_x:
            if self.left:
                self.left.insert(that_x)
            else:
                self.left = BinarySearchNode(that_x, parent=self)
        # build / update the right tree
        elif self.right:
            self.right.insert(that_x)
        else:
            self.right = BinarySearchNode(that_x, parent=self)

    def find(self, value):
        if self.x == value:
            return self
        elif self.left and self.x > value:
            return self.left.find(value)
        elif self.right:
            return self.right.find(value)
        return None

class Scheduling(BinarySearchNode):
    """Inherit the BinaySearchNode class with a slight change to insert"""
    def insert(self, that_x, k=3):
        if self._check_time_collision(self, that_x, k) or \
            self._check_time_collision(self.right, that_x, k) or \
            self._check_time_collision(self.left, that_x, k):
            return False
        # build / update the left tree
        if self.x > that_x:
            if self.left:
                self.left.insert(that_x)
            else:
                self.left = Scheduling(that_x, parent=self)
        # build / update the right tree
        elif self.right:
            self.right.insert(that_x)
        else:
            self.right = Scheduling(that_x, parent=self)

    def _check_time_collision(self, existing_schedule, prospect_time, k):
        """Check if there is a time collision between the schedules"""
        if existing_schedule and math.fabs(existing_schedule.x - prospect_time) < k:
            return True
        return False

    def __str__(self):
        val = str(self.x) + "\n"

        if self.left:
            val += self.left.__str__()

        if self.right:
            val += self.right.__str__()

        return val


def runway_test():
    # import pdb
    schedule = Scheduling(15)
    for i in range(3, 30, 3):
        schedule.insert(i)
    print(schedule)


if __name__ == "__main__":
    runway_test()
