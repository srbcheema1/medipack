import os
import subprocess

class C: # for colours
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    E = '\033[0m'


def _get_supported_distros(dependency_map):
    supported_distros = set()
    for rules in dependency_map.values():
        for key in rules.keys():
            supported_distros.add(key)
    return supported_distros


def line_adder(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        lines = [x.strip() for x in f.readlines()]
        if(not line in lines):
            f.seek(0, 0)
            f.write(content + '\n' + line + '\n')


def get_distro(distros):
    try:
        p = subprocess.Popen(['uname','-a'], stdout=subprocess.PIPE)
        out = p.stdout.read().decode('utf-8').lower()
        for d in distros:
            if d in out:
                return d
        return None
    except:
        return None


def is_installed(soft):
    dump_out = ' > /dev/null 2>&1'
    help_opt = ' --help '
    a = os.system(soft + help_opt + dump_out)
    if a == 0 or a == 256:
        '''
        0 means return 0
        256 means return 1, generally for those who dont have --help
        if command not found it will return 32512
        '''
        return True
    return False


def install_arg_complete():
    if is_installed('register-python-argcomplete'):
        line = 'eval "$(register-python-argcomplete medipack)"'
        filename = os.environ['HOME'] + '/.bashrc'
        line_adder(filename,line)


def install_dependencies(dependency_map, verbose = False):
    supported_distros = _get_supported_distros(dependency_map)
    distro = get_distro(supported_distros)
    if(not distro and verbose):
        print(C.R+'unrecognised distro, please contact srbcheema2@gmail.com for full support for your distro'+C.E)
    elif(distro and verbose):
        print(C.G+'Distro detected to be '+distro+' based'+C.E)

    all_installed = True

    for d in dependency_map.keys():
        if is_installed(d):
            continue
        rules = dependency_map[d]
        if distro and distro in rules.keys():
            print(C.G+'installing '+d+' dependency'+C.E)
            os.system(rules[distro])
            if not is_installed(d):
                print(C.Y+'please install ' +d+ ' dependency manually'+C.E)
                print(C.Y+'try command : '+rules[distro]+C.E)
                all_installed = False
        else:
            print(C.Y+'Please install ' +d+' dependency manually'+C.E)
            all_installed = False

    return all_installed


if __name__ == '__main__':
    dependency_map = {
        'register-python-argcomplete':{
            'ubuntu':'sudo apt install python-argcomplete',
        },
        'ffmpeg':{
            'ubuntu':'sudo apt install ffmpeg',
        },
        'figlet':{
            'ubuntu':'sudo apt install figlet',
        },
    }
    install_dependencies(dependency_map,verbose=True)
    install_arg_complete()
