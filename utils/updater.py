import requests
import logging
import sys
import os
from packaging import version

logger = logging.getLogger(__name__)
latest_version = True

__version__ = "v0.0.1"
GITHUB_REPO = "Marcellll/ReMatchInternal"
def check_for_update():
    API_url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    response = requests.get(API_url)

    if response.status_code != 200 and response.status_code != 403:
        logger.info(f"Failed to check for updates error : {response.status_code}, {response.content}")
        return

    latest_release = response.json()
    latest_version = latest_release["tag_name"]
    if version.parse(__version__) != version.parse(latest_version):
        logger.info(f"New version {latest_version} is available")
        latest_version = False
        executable_url = latest_release["assets"][0]["browser_download_url"]
        download_update(executable_url)
    else:
        logger.info("You are using the latest version")

def download_update(executable_url):
    logger.info("Downloading executable...")
    response = requests.get(executable_url)
    if response.status_code != 200:
        logger.info("Failed to download the executable")
        return
    
    new_executable_path = "new_test.exe"
    with open(new_executable_path, "wb") as f:
        f.write(response.content)
    logger.info("finished downloading the application")
    replace_and_restart(new_executable_path)

def replace_and_restart(new_executable_path):
    current_executable = sys.executable
    logger.info(f"current executable file location : {current_executable}")
    #os.replace(new_executable_path, current_executable)
    #logger.info(f"Replaced the current executable {current_executable} file with the downloaded one {new_executable_path}")
    os.execl(new_executable_path, new_executable_path, *sys.argv[1:])
    logger.info(f"executed the newly donwloaded file {current_executable}")