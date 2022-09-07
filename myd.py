#################################################################################
# File name : myd.py
#
# Create at     : 17/07/2022 10:35:28
# Create by     : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : Push web server for documentation generated by MkDocs
#
#################################################################################

from rich import print as print
import typer
import os
import subprocess
import termcolor
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

app = typer.Typer(rich_markup_mode="rich")

def get_param(param: str):
    if param == "docker_url" or param == "docker" or param == "d":
        return 0
    if param == "python_version" or param == "python" or param == "py":
        return 1
    if param == "git_token" or param == "token" or param == "t":
        return 2
    if param == "git_repo" or param == "repo" or param == "r":
        return 3
    if param == "ext_port" or param == "ext" or param == "e":
        return 4
    print("[[bold red]Error[/bold red]]: '" + param + "' is not valid parameter")
    raise typer.Exit(code=1)

def create_dir(dir: str, pwd: str):
    path: str = os.path.join(pwd, dir)
    os.mkdir(path)
    return
def check_ext_port(ext_port: str):
    if not ext_port.isnumeric():
        print("[[bold red]Error[/bold red]]: External port container other character than number, please put only number")
        raise typer.Exit(code=1)
# Function use to create conf file
def init_conf():

    # Check if conf dir exist
    if not os.path.isdir("conf"):
        create_dir("conf", os.getcwd())
    
    # Get different value needed to create conf file
    conf_name: str = input("Input name you want for configuration file: ")
    conf_extension: str = os.path.splitext(conf_name)[-1].lower()
    repo_docker_url: str = input("\nInput Docker Repository URL: ")


    # Check if docker file with python version specify exist
    python_version: str = input("\nInput Python version (3.X.X): ")
    python_docker_path: str = os.getcwd() + "/python_myd/python" + python_version + ".dockerfile"
    while not (os.path.exists(python_docker_path)):
        print("[bold red]Error[/bold red]: No such dockerfile with python version '" + python_version + "'")
        python_version: str = input("\nInput Python version (3.X.X): ")
        python_docker_path: str = os.getcwd() + "/python_myd/python" + python_version + ".dockerfile"

    git_token: str = input("\nInput Github Token: ")
    git_repo: str = input("\nInput Github Repository: ")

    # Check if external port contains other character than number
    external_port: str = input("\nInput external port will be used to run server: ")
    while not (external_port.isnumeric()):
        print("[bold red]Error[/bold red]: External port container other character than number, please put only number")
        external_port = input("\nInput external port will be used to run server: ")

    # Check if the user add .conf at the end of name or not
    if not conf_extension or conf_extension != ".conf":
        conf_name = conf_name.split(".", 1)[0]
        conf_name = conf_name + ".conf"
    
    # Get path to the new file created before
    conf_path: str = os.getcwd() + '/conf/' + conf_name
    # Check if file is already exist, if not we create it
    if not os.path.exists(conf_path):
        with open(conf_path, 'a')  as file:
            file.write("REPO_DOCKER_URL=" + repo_docker_url + "\n")
            file.write("PYTHON_VERSION=" + python_version + "\n")
            file.write("GIT_TOKEN=" + git_token + "\n")
            file.write("GIT_REPO=" + git_repo + "\n")
            file.write("EXT_PORT=" + external_port + "\n")
    else:
        with open(conf_path, 'w')  as file:
            file.write("REPO_DOCKER_URL=" + repo_docker_url + "\n")
            file.write("PYTHON_VERSION=" + python_version + "\n")
            file.write("GIT_TOKEN=" + git_token + "\n")
            file.write("GIT_REPO=" + git_repo + "\n")
            file.write("EXT_PORT=" + external_port + "\n")
    return conf_name

def edit_conf():
    # Check if dir conf is exist
    if not os.path.isdir("conf"):
            create_dir("conf", os.getcwd())
    
    # Show all files in conf directory
    print("[green]Files: ", os.listdir(os.getcwd() + "/conf"))

    # Get input of user and check if file is existing
    file_name: str = input("\nPlease enter which file you want edit: ")
    file_path: str = os.getcwd() + "/conf/" + file_name
    if not os.path.exists(file_path) or not file_name:
        print("[[bold red]Error[/bold red]]: No such file '" + file_name + "'")
        raise typer.Exit(code=1)

    # Ask user with wich parameter he want to edit
    print("[green]\nParameters: docker_url, python_version, git_token, git_repo, ext_port[/green]")
    param: str = input("\nPlease select which parameter you want edit: ")
    line: int = get_param(param)

    # Modify the parameter choose by the user
    with open(file_path, 'r') as file:
        data: list = file.readlines()
    print(data[line])
    data[line] = data[line].split("=", 1)[0] + "="
    param_value: str = input("\n\nPlease enter new value: ")
    data[line] = data[line] + param_value + "\n"
    print(data[line])
    with open(file_path, 'w') as file:
        file.writelines(data)
    return file_name


@app.command(rich_help_panel="Commands :computer:")
def config(edit: bool = typer.Option(False, help="Used to modify any existing configuration file")):
    """
    Create configuration file for Myd. :writing_hand:
    """
    if not edit:
        file: str = init_conf()
        print("[bold green]Success: [/bold green]" "The file '[bold red]" + file + "[/bold red]' has been created successfully")
    else:
        file: str = edit_conf()
        print("[bold green]Success: [/bold green]" "The file '[bold red]" + file + "[/bold red]' has been edited successfully")
    

# ---------------------------------------------------------------------------


# Create better --help for the build option (it list all files in conf directory with color)
if not os.path.isdir("conf"):
        create_dir("conf", os.getcwd())
help_build: str = ', '.join(os.listdir(os.getcwd() + "/conf"))
help_build = help_build.replace(help_build, termcolor.colored(help_build, 'green'))
help_build = "Enter which configuration file you want use: [" + help_build + "]"

# Check user input and check if the file mentioned exist even if the directory is missing at the beginning of input
def error_conf_file(file: str):
    dir: str = file.split("/", 1)[0] + "/"
    if (dir != "conf/"):
        file_path: str = os.getcwd() + "/conf/" + file
        if not os.path.exists(file_path):
            print("[[bold red]Error[/bold red]]: No such file '" +  file + "'")
            raise typer.Exit(code=1)
        else:
            return file_path
    elif (dir == "conf/"):
        file_path: str = os.getcwd() + "/" + file
        if not os.path.exists(file_path):
            print("[[bold red]Error[/bold red]]: No such file '" +  file + "'")
            raise typer.Exit(code=1)
        else:
            return file_path

# Check if conf file is correctly formated and if is not empty
def check_valid_file(data: list, line: int):
    param: str = data[line].split("=", 1)[1]
    name_val: str = data[line].split("=", 1)[0]
    if ((len(param) == 1) and (line == 0)) or ((line == 0) and (name_val != "REPO_DOCKER_URL")):
        print("[[bold red]Error[/bold red]]: The configuration file is correct but the data '[bold red]REPO_DOCKER_URL[/bold red]' is badly formatted, please regenerate one with the command 'python myd.py create'")
        raise typer.Exit(code=1)
    if ((len(param) == 1) and (line == 1)) or ((line == 1) and (name_val != "PYTHON_VERSION")):
        print("[[bold red]Error[/bold red]]: The configuration file is correct but the data '[bold red]PYTHON_VERSION[/bold red]' is badly formatted, please regenerate one with the command 'python myd.py create'")
        raise typer.Exit(code=1)
    if ((len(param) == 1) and (line == 2)) or ((line == 2) and (name_val != "GIT_TOKEN")):
        print("[[bold red]Error[/bold red]]: The configuration file is correct but the data '[bold red]GIT_TOKEN[/bold red]' is badly formatted, please regenerate one with the command 'python myd.py create'")
        raise typer.Exit(code=1)
    if ((len(param) == 1) and (line == 3)) or ((line == 3) and (name_val != "GIT_REPO")):
        print("[[bold red]Error[/bold red]]: The configuration file is correct but the data '[bold red]GIT_REPO[/bold red]' is badly formatted, please regenerate one with the command 'python myd.py create'")
        raise typer.Exit(code=1)
    if ((len(param) == 1) and (line == 4)) or ((line == 4) and (name_val != "EXT_PORT")):
        print("[[bold red]Error[/bold red]]: The configuration file is correct but the data '[bold red]EXT_PORT[/bold red]' is badly formatted, please regenerate one with the command 'python myd.py create'")
        raise typer.Exit(code=1)
    return

# Base value to navigate throw list with all parameter for more understanding
docker: int = 0
python: int = 1
git_token: int = 2
git_repo: int = 3
external_port: int = 4

# Run shell scrit to build debian image
def build_debian(docker_url: str):

# Create directory to store logs files
    if not os.path.isdir("logs"):
        create_dir("logs", os.getcwd())

# Write in file for log and add spinning bar during docker build process
    with open("logs/debian_build_log.txt", "w+") as log, Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Building Debian container...", total=None)
        raw_output: subprocess.CompletedProcess = subprocess.run(['sh', 'debian_myd/./build-debian.sh', docker_url], capture_output=True)
        log.write("----------------------------------DEBIAN LOG----------------------------------\n\n")
        log.write(raw_output.stdout.decode())

# Print error if build failed
        if raw_output.stderr.decode():
            print("[bold red]Error:[/bold red] " + raw_output.stderr.decode() + "[bold green]Please check debian_build_log.txt into logs directory for futher informations[/bold green]")
            raise typer.Exit(code=1)

# Run shell scrit to build python image
def build_python(python_version: str, docker_url: str):

# Create directory to store logs files
    if not os.path.isdir("logs"):
        create_dir("logs", os.getcwd())
    with open("logs/python_build_log.txt", "w+") as log, Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Building Python container...", total=None)
        raw_output: subprocess.CompletedProcess = subprocess.run(['sh', 'python_myd/./build-python.sh', python_version, docker_url], capture_output=True)
        log.write("----------------------------------PYTHON LOG----------------------------------\n\n")
        log.write(raw_output.stdout.decode())

# Print error if build failed
        if raw_output.stderr.decode():
            print("[bold red]Error:[/bold red] " + raw_output.stderr.decode() + "[bold green]Please check python_build_log.txt into logs directory for futher informations[/bold green]")
            raise typer.Exit(code=1)

# Run shell scrit to build python image
def build_nginx(python_version: str, docker_url: str, git_token: str, git_repo: str):

# Create directory to store logs files
    if not os.path.isdir("logs"):
        create_dir("logs", os.getcwd())

# Write in file for log and add spinning bar during docker build process
    with open("logs/nginx_build_log.txt", "w+") as log, Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Building Nginx container...", total=None)
        raw_output: subprocess.CompletedProcess = subprocess.run(['sh', 'nginx/./build-myd-docs.sh', python_version, docker_url, git_token, git_repo], capture_output=True)
        log.write("----------------------------------NGINX LOG----------------------------------\n\n")
        log.write(raw_output.stdout.decode())

# Print error if build failed
        if raw_output.stderr.decode():
            print("[bold red]Error:[/bold red] " + raw_output.stderr.decode() + "[bold green]Please check nginx_build_log.txt into logs directory for futher informations[/bold green]")
            raise typer.Exit(code=1)

# Check if user want to build a specific container or all.
# Layer order: debian -> python -> nginx
def build_container(data: list, container: str):
    if (container != "debian") and (container != "python") and (container != "nginx") and (container != "all"):
        print("[[bold red]Error[/bold red]]: No such option '" + container + "'")
        raise typer.Exit(code=1)
    if (container == "debian"):
        build_debian(data[docker])
        print("[bold green]The debian container has been successfully built[/bold green]")
        build_python(data[python], data[docker])
        print("[bold green]The python container has been successfully built[/bold green]")
        build_nginx(data[python], data[docker], data[git_token], data[git_repo])
        print("[bold green]The nginx container has been successfully built[/bold green]")
        print("[bold blue]Everything finished being built ![/bold blue]")
    if (container == "python"):
        build_python(data[python], data[docker])
        print("[bold green]The python container has been successfully built[/bold green]")
        build_nginx(data[python], data[docker], data[git_token], data[git_repo])
        print("[bold green]The nginx container has been successfully built[/bold green]")
        print("[bold blue]Everything finished being built ![/bold blue]")
    if (container == "nginx"):
        build_nginx(data[python], data[docker], data[git_token], data[git_repo])
        print("[bold green]The nginx container has been successfully built[/bold green]")
        print("[bold blue]Everything finished being built ![/bold blue]")
        
# Use to build container for server
@app.command(rich_help_panel="Commands :computer:")
def build(file: str = typer.Argument(..., help=help_build, metavar=termcolor.colored("File", 'red'), show_default=False), container: str = typer.Option("debian", help="Use to build specific container: debian, python, nginx", metavar="Container")):
    """
    Build each Docker container as needed to run. :brick:
    """

# Store config file index value in list and prepare argument for build
    key_value: list = [docker, python, git_token, git_repo]
    file = error_conf_file(file)
    with open(file, 'r') as f:
        data: list = f.readlines()
    if (len(data) != 5):
        print("[[bold red]Error[/bold red]]: The configuration file is not well formatted, please regenerate one with the command 'python myd.py create'")
        raise typer.Exit(code=1)
    for i in key_value:
        check_valid_file(data, i)
        data[i] = data[i].split("=", 1)[1]
        data[i] = data[i].split("\n", 1)[0]
    build_container(data, container)

# ---------------------------------------------------------------------------

@app.command(rich_help_panel="Commands :computer:")
def run(file: str = typer.Argument(...,help=help_build, metavar=termcolor.colored("File", 'red'), show_default=False)):
    """
    Launches the Nginx server. :rocket:
    """
# Error handling
    file = error_conf_file(file)

# Get in a list all parameters and well formatted
    with open(file, 'r') as f:
        data: list = f.readlines()
    ext_port: str = data[external_port].split("=", 1)[1]
    ext_port = ext_port.split("\n", 1)[0]
    docker_url: str = data[docker].split("=", 1)[1]
    docker_url = docker_url.split("\n", 1)[0]

# Create directory to store logs files
    if not os.path.isdir("logs"):
        create_dir("logs", os.getcwd())

# Write in file for log and add spinning bar during docker build process
    with open("logs/nginx_run_log.txt", "w+") as log, Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Running Nginx container on external port: " + ext_port + "...", total=None)
        raw_output: subprocess.CompletedProcess = subprocess.run(['sh', 'nginx/./run-nginx.sh', docker_url, ext_port], capture_output=True)
        log.write("----------------------------------NGINX LOG----------------------------------\n\n")
        log.write(raw_output.stdout.decode())
        if raw_output.stderr.decode():
            print("[bold red]Error:[/bold red] " + raw_output.stderr.decode() + "[bold green]Please check nginx_run_log.txt into logs directory for futher informations[/bold green]")
            raise typer.Exit(code=1)
    print("[bold green]Success: The server is running on external port " + ext_port +"[/bold green]")

if __name__ == "__main__":
    app()