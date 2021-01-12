import random


class Search:
    def __init__(self, n, g):
        self.n = n
        self.goal = g
        # Generate a sorted list (size n) of random numbers
        self.list = sorted(random.randint(0, self.n) for _ in range(0, self.n))
        # Set lower and higher values
        self.lower = 0
        self.higher = self.n-1
        # Create a variable to store the iterations
        self.iterations = 0

    # Create a function that search a number into an ordered list using binary search
    def binary_search(self, list, lower, higher, goal):
        self.iterations += 1
        # Set a medium value (integer)
        medium = (lower + higher) // 2

        # Validate if lower vale is higher than higher value, then return true
        if lower > higher:
            return False

        # Validate if medium, lower or higher vales are equal to goal, then return true
        if list[medium] == goal or list[lower] == goal or list[higher] == goal:
            return True
        # Otherwise, reduce the scope of the search
        else:
            lower += 1
            higher -= 1

        # Validate if goal is higher than medium value, then change lower value to medium value and call recursively.
        if goal > list[medium]:
            lower = medium + 1
            return self.binary_search(list, lower, higher, goal)

        # Validate if goal is lower than medium value, then change higher value to medium value and call recursively.
        if goal < list[medium]:
            higher = medium - 1
            return self.binary_search(list, lower, higher, goal)

if __name__ == "__main__":
    # I want to see the average of iterations in 1000 executions of the algorithm
    average = 0

    number_of_executions = 1000
    number_of_items = 1000
    print(f"Running a Binary Search algorithm to find a random number in a list of {number_of_items} items")
    for i in range(0, number_of_executions):
        # Generate a random number between 0 and 'number_of_items'
        goal = random.randint(0, number_of_items)
        # Instantiate Sort Class
        sort = Search(number_of_items, goal)
        # Call 'binary_search' method to find if previous number is in a random list of size n
        result = sort.binary_search(sort.list, sort.lower, sort.higher, sort.goal)
        # Increments the average value
        average += sort.iterations
        # I want to validate if the code is working good, I'm using 'in' to do that
        assert (sort.goal in sort.list) == result, "The algorithm doesn't work as expected."
    print(f"The average of iterations in {number_of_executions} executions is: {average / number_of_executions}")
