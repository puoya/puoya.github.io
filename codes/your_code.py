import re
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Sample jemdoc content
b = """
The Tree class can be initialized with either a file path or a treeswift.Tree object, along with an optional parameter to enable logging.

%%print 'Interactive Python code.'%%
"""

# Regular expression to find %%monospace%% and replace with syntax-highlighted code
r = re.compile(r'%%\s*(.*?)\s*%%', re.M | re.S)

# Function to highlight the Python code
def highlight_python_code(match):
    code = match.group(1)
    return highlight(code, PythonLexer(), HtmlFormatter(nowrap=True))

# Replace the %%code%% with highlighted Python code
b = re.sub(r, highlight_python_code, b)

# Print the result
print(b)
