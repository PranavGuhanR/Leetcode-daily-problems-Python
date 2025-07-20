class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        def serialize(node):
            if not node:    return "()"
            child_s = "".join(child + serialize(child_node) for child, child_node in sorted(node.items()))
            serial = "(" + child_s + ")"
            duplicates[serial].append(node)
            return serial

        def collect_paths(node, path):
            for child_name, child_node in node.items():
                if "#" in child_node:   continue
                new_path = path + [child_name]
                ret.append(new_path)
                collect_paths(child_node, new_path)

        tree, ret, duplicates = {}, [], defaultdict(list)
        for path in paths:
            node = tree
            for folder in path:
                node = node.setdefault(folder, {})
        serialize(tree)
        for nodes in duplicates.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.clear()
                    node["#"] = True
        collect_paths(tree, [])
        return ret