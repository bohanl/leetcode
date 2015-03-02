class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None

        new_node = UndirectedGraphNode(node.label)
        node_map = {node: new_node}

        q = collections.deque([node])
        while q:
            parent = q.popleft()

            for child in parent.neighbors:
                if not child in node_map:
                    q.append(child)
                new_child = node_map.setdefault(child, UndirectedGraphNode(child.label))
                node_map[parent].neighbors.append(new_child)

        return new_node