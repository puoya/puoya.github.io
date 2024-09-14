from your_package import Tree

# Example 1: Load tree from a file
tree = Tree("path_to_tree_file.tre")

# Example 2: Initialize with a treeswift.Tree object
import treeswift as ts
tree_obj = ts.read_tree_newick("((A,B),(C,D));")
tree = Tree("MyTree", tree_obj)

# Logging can be enabled with the 'enable_logging' parameter
tree_with_logging = Tree("path_to_tree_file.tre", enable_logging=True)
