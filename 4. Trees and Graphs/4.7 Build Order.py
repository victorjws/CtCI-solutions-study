# base definition
class Graph:
    def __init__(self):
        self.nodes: list[Project] = []
        self.map: dict = {}

    def __repr__(self):
        return f"Graph({self.nodes})"

    def get_or_create_node(self, name: str) -> "Project":
        if not self.map.get(name):
            node = Project(name)
            self.nodes.append(node)
            self.map.update({f"{name}": node})
        return self.map[name]

    def add_edge(self, start_name: str, end_name: str):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)
        start.add_neighbor(end)

    def get_nodes(self) -> list["Project"]:
        return self.nodes


class Project:
    class State:  # for DFS Solution
        BLANK = 0
        PARTIAL = 1
        COMPLETE = 2

    def __init__(self, n: str):
        self.children = []
        self.map = {}
        self.name = n
        self.dependencies = 0
        self.state = self.State.BLANK  # for DFS Solution

    def __repr__(self):
        return f"Project({self.name})"

    def add_neighbor(self, node: "Project"):
        if not self.map.get(node.get_name()):
            self.children.append(node)
            self.map.update({f"{node.get_name()}": node})
            node.increment_dependencies()

    def increment_dependencies(self):
        self.dependencies += 1

    def decrement_dependencies(self):
        self.dependencies -= 1

    def get_name(self) -> str:
        return self.name

    def get_children(self) -> list["Project"]:
        return self.children

    def get_number_dependencies(self) -> int:
        return self.dependencies

    # for DFS Solution
    def get_state(self):
        return self.state

    def set_state(self, st):
        self.state = st


# Solution 1. O(P + D) time,
# where P is the number of projects and D is the number of dependency pairs.

# Find a correct build order.
def find_build_order(
    projects: list[str], dependencies: list[list[str]]
) -> list[Project]:
    graph = build_graph(projects, dependencies)
    return order_projects(graph.get_nodes())


def build_graph(projects: list[str], dependencies: list[list[str]]) -> Graph:
    graph = Graph()
    for project in projects:
        graph.get_or_create_node(project)

    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)

    return graph


# Return a list of the projects a correct build order.
def order_projects(projects: list[Project]) -> list[Project] | None:
    order: list[Project] = []

    # Add "roots" to the build order first.
    end_of_list = add_non_dependent(order, projects, 0)

    to_be_processed = 0
    while to_be_processed < len(order):
        current: Project = order[to_be_processed]

        # We have a circular dependency since there are no remaining projects
        # with zero dependencies.
        if current is None:
            return None

        # Remove myself as a dependency.
        children = current.get_children()
        for child in children:
            child.decrement_dependencies()

        # Add children that have no one depending on them.
        end_of_list = add_non_dependent(order, children, end_of_list)
        to_be_processed += 1
    return order


# A helper function to insert projects with zero dependencies into the order
# array, starting at index offset.
def add_non_dependent(
    order: list[Project], projects: list[Project], offset: int
) -> int:
    for project in projects:
        if project.get_number_dependencies() == 0:
            order.append(project)
            offset += 1  # for need order's offset language
    return offset


p = ["a", "b", "c", "d", "e", "f", "g"]
dep = [
    ["f", "b"],
    ["f", "c"],
    ["c", "a"],
    ["b", "a"],
    ["b", "e"],
    ["a", "e"],
    ["d", "g"],
]
print(find_build_order(p, dep))


# DFS Solution.
def find_build_order2(
    projects: list[str], dependencies: list[list[str]]
) -> list[Project]:
    graph = build_graph(projects, dependencies)
    return order_projects2(graph.get_nodes())


def order_projects2(projects: list[Project]):
    stack = []
    for project in projects:
        if project.get_state() == Project.State.BLANK:
            if not do_dfs(project, stack):
                return None
    return stack


def do_dfs(project: Project, stack: list[Project]) -> bool:
    if project.get_state() == Project.State.PARTIAL:
        return False  # Cycle

    if project.get_state() == Project.State.BLANK:
        project.set_state(Project.State.PARTIAL)
        children = project.get_children()
        for child in children:
            if not do_dfs(child, stack):
                return False
        project.set_state(Project.State.COMPLETE)
        stack.append(project)
    return True


print(find_build_order2(p, dep))


# My Solution.
def get_build_order(graph: dict):
    order = []
    node = None
    while graph:
        for k, v in graph.items():
            if not v:
                node = k
                break
        else:
            raise Exception("Can't build")
        order.append(node)
        graph.pop(node)
        for k, v in graph.items():
            if node in v:
                v.remove(node)
    return ", ".join(order)


g = {
    "a": ["f"],
    "b": ["f"],
    "c": ["d"],
    "d": ["a", "b"],
    "e": [],
    "f": [],
}
print(get_build_order(g))
