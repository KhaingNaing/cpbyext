# cpbyext
This repo contains code that can recursively copy files with specified extensions. 

# Prerequisite
Requires python>=3.8

# Execution Using Python
1. Install this cpbyext package by:
    ```bash
    pip install git+https://github.com/KhaingNaing/cpbyext.git#egg=cpbyext
    ```
2. Navigate to the Directory: Change to the directory where you want to recursively copy files:
    ```bash
    cd /path/to/directory
    ```
3. Run the code using the following command:
    ```bash
    cpbyext <ext1> <ext2>
    ```

# Using Docker Image 
1. Install Docker: Use the following command to install Docker on Linux:
    ```bash
    sudo apt-get install -y docker.io
    ```
2. Enable docker:
    ```bash
    sudo systemctl start docker 
    ```
3. Pull Image:
    ```bash
    docker image pull khaing1226/cpbyext
    ```
4. Navigate to the Directory: Change to the directory where you want to recursively copy files:
    ```bash
    cd /path/to/directory
    ```
5. Execute Image:
    ```bash
    docker container run --rm -d -v $(pwd):/zone khaing1226/cpbyext <ext1> <ext2>
    ```

**Note**
Replace `<ext1>` with the file extension that you want to copy recursively.  

