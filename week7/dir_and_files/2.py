import os
path="C:/PP2/6week/6labs/dir_and_files"

print("Result:", os.access(path, os.F_OK))
print("Result:", os.access(path, os.R_OK))
print("Result:", os.access(path, os.W_OK))
print("Result:", os.access(path, os.X_OK))
