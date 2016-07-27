import os

from fnmatch import fnmatch
from subprocess import call

# Variables
_GAME_DIR = r'D:\Games\Minecraft'
_SERVER_PROPERTIES_FILE_NAME = r'server.properties'
_SERVER_PROPERTIES_PATH = '\\'.join([_GAME_DIR, _SERVER_PROPERTIES_FILE_NAME])
_DIR_PREFIX = r'world-'
_LEVEL_NAME_PREFIX = r'level-name='
_NEW_LINE = '\n'

def clear_screen():
    for i in range(20):
        print ''

def print_menu(worlds):
    # Print Worlds
    print 'Worlds:'
    for i in range(len(worlds)):
        print '[{}] {}'.format((i + 1), worlds[i][len(_DIR_PREFIX):])

# Change to _GAME_DIR
os.chdir(_GAME_DIR)

# Collect Worlds
worlds = []
for d in os.listdir('.'):
    if d.startswith(_DIR_PREFIX):
        worlds.append(d)
    elif fnmatch(d, 'minecraft_server*.jar'):
        _SERVER_NAME = d

# Detect Current World
with open(_SERVER_PROPERTIES_PATH, 'r') as f:
    server_properties_file = f.read().splitlines()
    for i in range(len(server_properties_file)):
        line = server_properties_file[i]
        if line.startswith(_LEVEL_NAME_PREFIX):
            current_world = line[len(_LEVEL_NAME_PREFIX) + len(_DIR_PREFIX):]
            level_name_line = i
            break

# Clear Screen and Print Worlds
clear_screen()
print_menu(worlds)

# Get User Input
while(True):
    in_char = raw_input("\nStart which world?: ").strip()
    if in_char.isdigit() and int(in_char) > 0 and int(in_char) <= len(worlds):
        world_to_start = (int(in_char) - 1)
        print '\nStarting World: {}'.format(worlds[world_to_start][len(_DIR_PREFIX):])
        break
    else:
        clear_screen()
        print_menu(worlds)

# Check if need to edit server_properties_file
if current_world != worlds[world_to_start][len(_DIR_PREFIX):]:
    server_properties_file[level_name_line] = _LEVEL_NAME_PREFIX + worlds[world_to_start]
    # Rewrite Server_Properties_File
    with open(_SERVER_PROPERTIES_PATH, 'w') as f:
        for line in server_properties_file:
            print >> f, line

# Start Server
print '\nInvoking Java Subprocess...'
call(['java', '-Xmx1024M', '-Xms1024M', '-jar', _SERVER_NAME, 'nogui'])