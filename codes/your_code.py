import re

# Sample jemdoc content
b = """
The Tree class can be initialized with either a file path or a treeswift.Tree object, along with an optional parameter to enable logging.

%% print 'Interactive Python code.' %%
"""

# Regular expression to find %%monospace%% and replace with <tt>monospace</tt>
r = re.compile(r'%%(.*?)%%', re.M | re.S)
b = re.sub(r, r'<tt>\1</tt>', b)

# Print the result
print(b)
