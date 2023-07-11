
class Queue:
    """
    singly linkedlist with FIFO settings
    """
    def __init__(self):
        self._container = Deque()

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

    def __repr__(self):
        return repr(self._container)


def bfs(initial, goal_test, successors):
    frontier = Queue()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node

        for i in successors(current_state):

            if i in explored:
                continue

            explored.add(i)
            frontier.push(Node(i, current_node))

    return None


