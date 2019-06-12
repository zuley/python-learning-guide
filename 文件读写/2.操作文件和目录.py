import os
nowDir = os.path.abspath('.')
newDir = os.path.join(nowDir, 'testdir')
os.rmdir(newDir)
print(newDir)

