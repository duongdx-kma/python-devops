import subprocess

command = ["ls", "-ltra"]  # when set shell = FALSE
command_true = "ls -ltra"  # when set shell = TRUE

sub = subprocess.Popen(
    command,
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True # convert binary to normal value
)

rt = sub.wait()

out, err = sub.communicate()
print("response is:")
print(sub.communicate())  # tuple
print(out)    # when command successfully
print(err)    # when command failure


command_ping = ['ping', '-c 5', 'google.com']
sub_process = subprocess.Popen(
    command_ping,
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True # convert binary to normal value
)

rc = sub_process.wait()
out_ping, err_ping = sub_process.communicate()
print(sub_process.communicate())  # tuple
print('ping output is: \n', out_ping)    # when command successfully
print('ping error is: \n',  err_ping)    # when command failure