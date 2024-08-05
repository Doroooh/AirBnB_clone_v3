#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers.
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

# Define the hosts where the script will be executed
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_pack():
    """
    Generates a tgz archive from the contents of the web_static folder.
    
    Returns:
        str: The archive path if successful, otherwise None.
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


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    
    Args:
        archive_path (str): The path to the archive to be distributed.
    
    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    # Check if the archive exists
    if not exists(archive_path):
        return False
    
    try:
        # Extract the file name and name without extension
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        release_path = "/data/web_static/releases/"
        
        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, '/tmp/')
        
        # Create the directory where the archive will be extracted
        run(f'mkdir -p {release_path}{no_ext}/')
        
        # Extract the archive to the newly created directory
        run(f'tar -xzf /tmp/{file_name} -C {release_path}{no_ext}/')
        
        # Remove the archive from the /tmp/ directory
        run(f'rm /tmp/{file_name}')
        
        # Move the contents from the web_static folder to the parent directory
        run(f'mv {release_path}{no_ext}/web_static/* {release_path}{no_ext}/')
        
        # Remove the now empty web_static folder
        run(f'rm -rf {release_path}{no_ext}/web_static')
        
        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')
        
        # Create a new symbolic link
        run(f'ln -s {release_path}{no_ext}/ /data/web_static/current')
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers.
    
    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    # Create an archive
    archive_path = do_pack()
    
    # Deploy the archive if creation was successful
    if archive_path is None:
        return False
    return do_deploy(archive_path)
