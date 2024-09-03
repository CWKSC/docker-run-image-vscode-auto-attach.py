# Docker Container Runner with VS Code Integration

> [!NOTE]
> 
> Almost everythings is generate by GPT, even this README.md

This Python script provides a convenient way to run a Docker container and automatically attach it to Visual Studio Code for a seamless development environment setup.

## Usage

### Prerequisites
- Docker installed on your system
- Visual Studio Code installed on your system

### Running the Script
1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using the following command:
   ```bash
   python docker-run-image-vscode-auto-attach.py <image_name> [<additional_args>]
   ```

   - `<image_name>`: Name of the Docker image you want to run.
   - `[<additional_args>]` (optional): Additional arguments to pass to the Docker container.

The `--volume` is `./workspace/:/workspace/`

### Example
```bash
python docker-run-image-vscode-auto-attach.py my_docker_image --env DEBUG=1 --network host
```

## Features
- Checks if a container is already running with a given name and stops it if necessary.
- Runs a Docker container with specified configurations.
- Mounts a local workspace directory into the container.
- Automatically attaches the container to Visual Studio Code for code editing.

## Note
- Ensure that the specified Docker image is available on your system.
- Make sure to adjust the Docker run configurations in the script to match your requirements.

Feel free to customize the script according to your needs and contribute to its development!

