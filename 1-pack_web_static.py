#!/usr/bin/python3
"""
 Fabric script that generates a .tgz
"""

def do_pack():
    """
    files in the folder web_static
    """
    from fabric.api import local
    from datetime import datetime
    from os.path import isdir
    
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
