from stack import Stack

class Node:

    def __init__(self, name: str, children: list[str] = []):
        self.__name = name
        self.__children = children

    @property
    def name(self):
        return self.__name

    @property
    def children(self):
        return iter(self.__children)

    def add_child(self, child_name: str):
        self.__children.append(child_name)


class Graph:

    def __init__(self, directional = False):
        self.__directional = directional
        self.__root_node = None
        self.__node_list: dict[str, Node] = {}

    def add_node(self, node: Node):
        if self.__root_node == None:
            self.__root_node = node
        
        self.__node_list[node.name] = node

        # Add link to child node if the graph is bi-directional
        if self.__directional == False:
            for child_name in node.children:
                if child_name in self.__node_list:
                    self.__node_list[child_name].add_child(node.name)

    def get_node(self, node_name: str) -> Node | None:
        return self.__node_list[node_name] if node_name in self.__node_list else None

    def depth_first(self, dfs: list[str] = [], root = None) -> list[str] :
        if root == None:
            root = self.__root_node

        if root.name not in dfs:
            dfs.append(root.name)
            for c in root.children:
                dfs = self.depth_first(dfs, self.get_node(c))
            
        return dfs


    def comp_con(self):
        pass

    def path(self):
        pass

