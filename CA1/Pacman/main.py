import copy
import time
import heapq
import os


class Node:

    def __init__(self, game_map, parent, foods_count, p_x, p_y, q_x, q_y, cost):
        self.id = ''
        self.game_map = game_map
        self.foods_count = foods_count
        self.parent = parent
        self.p_x = p_x
        self.p_y = p_y
        self.q_x = q_x
        self.q_y = q_y
        self.cost = cost
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                self.id += game_map[i][j]

    def child_maker(self):
        childs = []

        # P moves; left, down, right, up
        if self.game_map[self.p_y][self.p_x - 1] == ' ':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.p_y][self.p_x - 1] = 'P'
            tmp[self.p_y][self.p_x] = ' '
            new_node = Node(tmp, self, self.foods_count, self.p_x - 1, self.p_y, self.q_x, self.q_y, self.cost + 1)
            childs.append(new_node)
        elif self.game_map[self.p_y][self.p_x - 1] == '1' or self.game_map[self.p_y][self.p_x - 1] == '3':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.p_y][self.p_x - 1] = 'P'
            tmp[self.p_y][self.p_x] = ' '
            new_node = Node(tmp, self, self.foods_count - 1, self.p_x - 1, self.p_y, self.q_x, self.q_y, self.cost + 1)
            childs.append(new_node)

        if self.game_map[self.p_y + 1][self.p_x] == ' ':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.p_y + 1][self.p_x] = 'P'
            tmp[self.p_y][self.p_x] = ' '
            new_node = Node(tmp, self, self.foods_count, self.p_x, self.p_y + 1, self.q_x, self.q_y, self.cost + 1)
            childs.append(new_node)
        elif self.game_map[self.p_y + 1][self.p_x] == '1' or self.game_map[self.p_y + 1][self.p_x] == '3':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.p_y + 1][self.p_x] = 'P'
            tmp[self.p_y][self.p_x] = ' '
            new_node = Node(tmp, self, self.foods_count - 1, self.p_x, self.p_y + 1, self.q_x, self.q_y, self.cost + 1)
            childs.append(new_node)

        if self.game_map[self.p_y][self.p_x + 1] == ' ':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.p_y][self.p_x + 1] = 'P'
            tmp[self.p_y][self.p_x] = ' '
            new_node = Node(tmp, self, self.foods_count, self.p_x + 1, self.p_y, self.q_x, self.q_y, self.cost + 1)
            childs.append(new_node)
        elif self.game_map[self.p_y][self.p_x + 1] == '1' or self.game_map[self.p_y][self.p_x + 1] == '3':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.p_y][self.p_x + 1] = 'P'
            tmp[self.p_y][self.p_x] = ' '
            new_node = Node(tmp, self, self.foods_count - 1, self.p_x + 1, self.p_y, self.q_x, self.q_y, self.cost + 1)
            childs.append(new_node)

        if self.game_map[self.p_y - 1][self.p_x] == ' ':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.p_y - 1][self.p_x] = 'P'
            tmp[self.p_y][self.p_x] = ' '
            new_node = Node(tmp, self, self.foods_count, self.p_x, self.p_y - 1, self.q_x, self.q_y, self.cost + 1)
            childs.append(new_node)
        elif self.game_map[self.p_y - 1][self.p_x] == '1' or self.game_map[self.p_y - 1][self.p_x] == '3':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.p_y - 1][self.p_x] = 'P'
            tmp[self.p_y][self.p_x] = ' '
            new_node = Node(tmp, self, self.foods_count - 1, self.p_x, self.p_y - 1, self.q_x, self.q_y, self.cost + 1)
            childs.append(new_node)

        # Q moves; left, down, right, up
        if self.game_map[self.q_y][self.q_x - 1] == ' ':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.q_y][self.q_x - 1] = 'Q'
            tmp[self.q_y][self.q_x] = ' '
            new_node = Node(tmp, self, self.foods_count, self.p_x, self.p_y, self.q_x - 1, self.q_y, self.cost + 1)
            childs.append(new_node)
        elif self.game_map[self.q_y][self.q_x - 1] == '2' or self.game_map[self.q_y][self.q_x - 1] == '3':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.q_y][self.q_x - 1] = 'Q'
            tmp[self.q_y][self.q_x] = ' '
            new_node = Node(tmp, self, self.foods_count - 1, self.p_x, self.p_y, self.q_x - 1, self.q_y, self.cost + 1)
            childs.append(new_node)

        if self.game_map[self.q_y + 1][self.q_x] == ' ':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.q_y + 1][self.q_x] = 'Q'
            tmp[self.q_y][self.q_x] = ' '
            new_node = Node(tmp, self, self.foods_count, self.p_x, self.p_y, self.q_x, self.q_y + 1, self.cost + 1)
            childs.append(new_node)
        elif self.game_map[self.q_y + 1][self.q_x] == '2' or self.game_map[self.q_y + 1][self.q_x] == '3':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.q_y + 1][self.q_x] = 'Q'
            tmp[self.q_y][self.q_x] = ' '
            new_node = Node(tmp, self, self.foods_count - 1, self.p_x, self.p_y, self.q_x, self.q_y + 1, self.cost + 1)
            childs.append(new_node)

        if self.game_map[self.q_y][self.q_x + 1] == ' ':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.q_y][self.q_x + 1] = 'Q'
            tmp[self.q_y][self.q_x] = ' '
            new_node = Node(tmp, self, self.foods_count, self.p_x, self.p_y, self.q_x + 1, self.q_y, self.cost + 1)
            childs.append(new_node)
        elif self.game_map[self.q_y][self.q_x + 1] == '2' or self.game_map[self.q_y][self.q_x + 1] == '3':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.q_y][self.q_x + 1] = 'Q'
            tmp[self.q_y][self.q_x] = ' '
            new_node = Node(tmp, self, self.foods_count - 1, self.p_x, self.p_y, self.q_x + 1, self.q_y, self.cost + 1)
            childs.append(new_node)

        if self.game_map[self.q_y - 1][self.q_x] == ' ':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.q_y - 1][self.q_x] = 'Q'
            tmp[self.q_y][self.q_x] = ' '
            new_node = Node(tmp, self, self.foods_count, self.p_x, self.p_y, self.q_x, self.q_y - 1, self.cost + 1)
            childs.append(new_node)
        elif self.game_map[self.q_y - 1][self.q_x] == '2' or self.game_map[self.q_y - 1][self.q_x] == '3':
            tmp = copy.deepcopy(self.game_map)
            tmp[self.q_y - 1][self.q_x] = 'Q'
            tmp[self.q_y][self.q_x] = ' '
            new_node = Node(tmp, self, self.foods_count - 1, self.p_x, self.p_y, self.q_x, self.q_y - 1, self.cost + 1)
            childs.append(new_node)

        return childs

    def __lt__(self, other):
        return self.cost + self.foods_count < other.cost + other.foods_count


    def bfs(self, start_node):
        global visited_nodes_cnt
        global already_visited_nodes_cnt
        visited = set()
        queue = []
        queue.append(start_node)
        visited.add(start_node.id)
        already_visited_nodes_cnt = 0
        while queue:
            s = queue.pop(0)
            for each in s.child_maker():
                if each.id in visited:
                    already_visited_nodes_cnt += 1
                else:
                    if is_goal(each):
                        visited_nodes_cnt = len(visited)
                        return each
                    queue.append(each)
                    visited.add(each.id)

    def dldfs(self, start_node, max_depth):
        global visited_nodes_cnt
        global already_visited_nodes_cnt
        visited = {}
        stack = []
        stack.append([start_node, 1])
        visited[start_node.id] = start_node.cost
        already_visited_nodes_cnt = 0
        while stack:
            node, depth = stack.pop()
            if is_goal(node):
                visited_nodes_cnt = len(visited)
                return node
            if depth == max_depth:
                continue
            else:
                for each in node.child_maker():
                    if each.id not in visited:
                        stack.append([each, depth + 1])
                        visited[each.id] = each.cost
                    elif (each.id in visited) and (each.cost < visited[each.id]):
                        visited[each.id] = each.cost
                        stack.append([each, depth + 1])
                    elif (each.id in visited) and (each.cost >= visited[each.id]):
                        already_visited_nodes_cnt += 1
        return False

    def ids(self, start_node):
        max_depth = 1
        while True:
            goal_node = self.dldfs(start_node, max_depth)
            if goal_node is False:
                max_depth += 1
            else:
                return goal_node

    def f(self, node, cost_up_to_now):
        return node.foods_count + cost_up_to_now

    def astar(self, start_node):
        global visited_nodes_cnt
        global already_visited_nodes_cnt
        visited = set()
        frontier = []
        heapq.heappush(frontier, [self.f(start_node, 0), start_node])
        heapq.heapify(frontier)
        visited.add(start_node.id)
        already_visited_nodes_cnt = 0
        while frontier:
            val, node = heapq.heappop(frontier)
            for each in node.child_maker():
                if each.id in visited:
                    already_visited_nodes_cnt += 1
                else:
                    if is_goal(each):
                        visited_nodes_cnt = len(visited)
                        return each
                    heapq.heappush(frontier, [self.f(each, each.cost), each])
                    visited.add(each.id)

    def another_f(self, node):
        return node.foods_count

    def another_astar(self, start_node):
        global visited_nodes_cnt
        global already_visited_nodes_cnt
        visited = set()
        frontier = []
        heapq.heappush(frontier, [self.another_f(start_node), start_node])
        heapq.heapify(frontier)
        visited.add(start_node.id)
        already_visited_nodes_cnt = 0
        while frontier:
            val, node = heapq.heappop(frontier)
            for each in node.child_maker():
                if each.id in visited:
                    already_visited_nodes_cnt += 1
                else:
                    if is_goal(each):
                        visited_nodes_cnt = len(visited)
                        return each
                    heapq.heappush(frontier, [self.another_f(each), each])
                    visited.add(each.id)

    def animate_path(self, v):
        path = []
        global cost
        while v.parent is not None:
            current_map = ""
            for i in range(len(v.game_map)):
                for j in range(len(v.game_map[i])):
                    current_map += v.game_map[i][j]
                current_map += '\n'
            #print(current_map)
            path.append(current_map)
            v = copy.deepcopy(v.parent)
        cost = len(path)
        for i in range(cost):
            os.system('cls')
            print(path[cost - 1 - i])
            time.sleep(0.25)
        return

    def print_path(self, node):
        path = []
        global cost
        while node.parent is not None:
            if node.p_x - node.parent.p_x == 1:
                path.append("P => Right")
            elif node.parent.p_x - node.p_x == 1:
                path.append("P => Left")
            elif node.p_y - node.parent.p_y == 1:
                path.append("P => Down")
            elif node.parent.p_y - node.p_y == 1:
                path.append("P => Up")
            elif node.q_x - node.parent.q_x == 1:
                path.append("Q => Right")
            elif node.parent.q_x - node.q_x == 1:
                path.append("Q => Left")
            elif node.q_y - node.parent.q_y == 1:
                path.append("Q => Down")
            elif node.parent.q_y - node.q_y == 1:
                path.append("Q => Up")

            node = copy.deepcopy(node.parent)
        cost = len(path)
        for i in range(cost):
            print(path[len(path) - 1 - i])

        return


def inputting(file_name):
    file_name = "testcases/" + file_name
    game_board = open(file_name, "r")
    game_board_lines = game_board.read().splitlines()
    game_board_lines_splitted = []
    for i in range(len(game_board_lines)):
        game_board_lines_splitted.append([char for char in game_board_lines[i]])
    return game_board_lines_splitted


def is_goal(node):
    return node.foods_count == 0


splitted = inputting("test5")

# counting foods
foods_cnt = 0
for i in range(len(splitted)):
    for j in range(len(splitted[i])):
        if splitted[i][j] == '1' or splitted[i][j] == '2' or splitted[i][j] == '3':
            foods_cnt += 1

# initializing P and Q coordinates
p_x = 0
p_y = 0
q_x = 0
q_y = 0

# finding P and Q coordinates
for i in range(len(splitted)):
    for j in range(len(splitted[i])):
        if splitted[i][j] == 'P':
            p_x = j
            p_y = i
        if splitted[i][j] == 'Q':
            q_x = j
            q_y = i


start_node = Node(splitted, None, foods_cnt, p_x, p_y, q_x, q_y, 0)
start_time = time.time()

# bfs, ids, and astar functions can be called
answer = start_node.bfs(start_node)

end_time = time.time()
answer.animate_path(answer)

print('\n time : ' + str(end_time - start_time) + ' seconds')
print(" cost : " + str(cost))
print(" visited states : " + str(visited_nodes_cnt))
print(" ignored already visited states : " + str(already_visited_nodes_cnt))
