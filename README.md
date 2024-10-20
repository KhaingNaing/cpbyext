# cpbyext
This repo contains code that can recursively copy files with specified extensions. 

# Execution Using Python
Clone the repository and run the code using the following command:
```bash
python -m cpbyext <ext1> <ext2>
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
5. Execute Image:
    ```bash
    docker container run --rm -d -v $(pwd):/zone khaing1226/cpbyext <ext1> <ext2>
    ```

**Note**
Replace `<ext1>` with the file extension that you want to copy recursively.  

