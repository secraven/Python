import subprocess
import optparse

def get_arguements():
    parser = optparse.OptionParser()
    parser.add_option("-o", "--owner", dest="owner", help="List directory and owner.")
    parser.add_option("-c", "--created", dest="created", help="List directory and created time.")
    (options, arguements) = parser.parse_args()
    print("option 1: " + options.owner)
    print("options 2: " + options.created)
    return parser.parse_args()


def get_dir(owner, created):
    print("[+] Starting directory listing with the following argument ")
    subprocess.call(["dir", owner, created], shell=True)

(options, arguements) = get_arguements()
get_dir(options.owner, options.created)


#subprocess.run('dir \/q', shell=True)