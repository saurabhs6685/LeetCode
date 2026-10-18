class Solution:

  def simplifyPath(self, path: str) -> str:
    stack = []
    # Split the path by "/" into directory tokens
    parts = path.split("/")

    for part in parts:
      if part == "" or part == ".":
        # Ignore empty parts (from consecutive slashes) and current directory '.'
        continue
      elif part == "..":
        # Go up one directory if possible
        if stack:
          stack.pop()
      else:
        # Valid directory or file name
        stack.append(part)

    # Reconstruct the canonical path starting with a single '/'
    return "/" + "/".join(stack)