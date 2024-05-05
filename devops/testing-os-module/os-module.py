import os
import shutil

# running system command:
os.system("ls -ltra")

output = os.system("ls -ltra")

print("output of ls -ltra: {}".format(output))

# make directory:
if not os.path.isdir("duongdx"):
    os.mkdir("duongdx")

# make directory recursively:
os.makedirs("testing1/testing2/testing2.1", exist_ok=True)
os.makedirs("testing1/testing3/testing3.1", exist_ok=True)
os.makedirs("testing1/testing4/testing4.1", exist_ok=True)
os.makedirs("testing1/testing5/testing5.1", exist_ok=True)

# change directory
print("change directory")
os.chdir("/")

# list directory
print("list directory")
directories = os.listdir('./testing1')
for dir in directories:
    print("folder: {}".format(dir))

# get all environment variable:
print("get all environment variable:", os.environ)
print("get DESKTOP_SESSION env: {}".format(os.environ.get("DESKTOP_SESSION")))

# get user id
print("get user id: {}".format(os.getuid()))
print("get user name: {}".format(os.getlogin()))

# get group id
print("get group id: {}".format(os.getgid()))

# remove dir
print("remove empty dir")
os.rmdir("./duongdx")

# remove recursive directory
print("remove recursive directory - directory have children")
os.removedirs("./testing1/testing2/testing2.1")
shutil.rmtree("./testing1")

# os.path:
print('---------------------------')
print('|      os.path             |')
print('---------------------------')
print("list all build in function of os.path")
print("check path /etc/hosts exist: {}".format(os.path.exists('/etc/hosts')))
print("check path /etc/hosts is file: {}".format(os.path.isfile('/etc/hosts')))
print("check path /etc/rc0.d/K01spice-vdagent is symbolic link: {}".format(os.path.isfile('/etc/rc0.d/K01spice-vdagent')))
print("get size of file /home/duongdx/Downloads/Dinh-Xuan-Duong-devops.pdf : {}".format(os.path.getsize('/home/duongdx/Downloads/Dinh-Xuan-Duong-devops.pdf')))
print("get basename : {}".format(os.path.basename('/home/duongdx/Downloads/Dinh-Xuan-Duong-devops.pdf')))
print("get path name : {}".format(os.path.dirname('/home/duongdx/Downloads/Dinh-Xuan-Duong-devops.pdf')))
print("concat to exactly path: {}".format(os.path.join("/tmp", "minikube_67d00ef5d4c3577df1643389c4fc65117ae87183_0.log")))

# os.walk:
print('---------------------------')
print('|      os.walk             |')
print('---------------------------')

print("list all file in directory:")
file = list(os.walk("/home/duongdx/Downloads")) # convert to list
print(file)

for directory_path, folder_inside_path, file_inside_path in file:
    print("path: {}".format(directory_path))
    print("list folders:")
    for folder in folder_inside_path:
        print("/".join([directory_path, folder]))

    print("list files:")
    for sub_file in file_inside_path:
        print("/".join([directory_path, sub_file]))
