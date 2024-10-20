# cpbyext
This repo contains code that can recursively copy files with specified extensions. 

# Execution Using Python
Clone the repository and run the code using the following command:
```bash
python -m cpbyext
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
    docker image pull 
    ```
4. Execute Image:
    ```bash
    docker container run -d -v $(pwd): 
    ```

