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
    
    local("mkdir -p versions")
    
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'version/web_static_{}.tgz'.format(date)
    rtn = local('tar -cvzf {} web_static'.format(path))
    if rtn.succeeded:
        return path
    else:
        return None
