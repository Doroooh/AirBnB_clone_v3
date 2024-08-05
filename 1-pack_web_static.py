#!/usr/bin/python3

"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """
    Generates a tgz archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise returns None.
    """
    try:
        # Get the current date and time in the format YYYYMMDDHHMMSS
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Check if the versions directory exists, if not, create it
        if not isdir("versions"):
            local("mkdir versions")
        
        # Define the file name for the archive
        file_name = f"versions/web_static_{date}.tgz"
        
        # Create the tgz archive from the web_static folder
        local(f"tar -cvzf {file_name} web_static")
        
        # Return the path to the created archive
        return file_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
