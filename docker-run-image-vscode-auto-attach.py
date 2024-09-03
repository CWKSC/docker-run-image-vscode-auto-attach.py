import sys
import subprocess
import os

def check_and_stop_container(container_name):
    # Check if the container is running
    check_cmd = ["docker", "container", "inspect", "-f", "{{.State.Running}}", container_name]
    try:
        result = subprocess.run(check_cmd, capture_output=True, text=True, check=True)
        is_running = result.stdout.strip().lower() == 'true'
    except subprocess.CalledProcessError:
        # Container doesn't exist
        return False

    if is_running:
        print(f"Container {container_name} is already running. Stopping it...")
        stop_cmd = ["docker", "container", "stop", container_name]
        subprocess.run(stop_cmd, check=True)
        print(f"Container {container_name} stopped.")
        return True
    return False

def run_docker_and_attach(additional_args, image_name):
    # Append "-container" to the image name for the container name
    container_name = f"{image_name}-container"
    
    # Check and stop the container if it's already running
    check_and_stop_container(container_name)

    # Base Docker run command
    docker_cmd = [
        "docker", "container", "run",
        "--detach",
        "--gpus", "all",
        "--hostname", container_name,
        "--interactive",
        "--ipc=host",
        "--name", container_name,
        "--privileged",
        "--rm",
        "--stop-timeout", "0",
        "--tty",
        "--volume", f"./workspace/:/workspace/",
    ]
    
    # Append additional arguments if provided before the image name
    if additional_args:
        docker_cmd.extend(additional_args)
    
    # Add the image name at the end
    docker_cmd.append(image_name)

    # Run the Docker container
    subprocess.run(docker_cmd, check=True)
    
    # Convert container name to hex
    container_name_hex = container_name.encode('ascii').hex()
    
    # Run VS Code command
    os.system(f'code --folder-uri vscode-remote://attached-container+{container_name_hex}/workspace')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <image_name> [<additional_args>]")
        sys.exit(1)
    
    # Capture additional arguments and image name
    image_name  = sys.argv[1]  
    additional_args = sys.argv[2:] 

    print("image_name: ", image_name)
    print("additional_args: ", additional_args)

    run_docker_and_attach(additional_args, image_name)
