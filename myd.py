from pickle import TRUE
from platform import python_version
from typing import Optional
from rich import print as print
import rich.markdown
from colorama import init, Fore, Back, Style
import typer
import os
import subprocess
import termcolor
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer(rich_markup_mode="rich")

def get_param(param: str):
    if param == "docker_url" or param == "docker" or param == "d":
        return 0
    if param == "python_version" or param == "python" or param == "p":
        return 1
    if param == "git_token" or param == "token" or param == "t":
        return 2
    if param == "git_repo" or param == "repo" or param == "r":
        return 3
    print("[[bold red]Error[/bold red]]: '" + param + "' is not valid parameter")
    raise typer.Exit(code=1)

def create_dir(dir: str, pwd: str):
    path: str = os.path.join(pwd, dir)
    os.mkdir(path)
    return

# Function use to create conf file
def init_conf():

    # Check if conf dir exist
    if not os.path.isdir("conf"):
        create_dir("conf", os.getcwd())
    
    # Get different value needed to create conf file
    conf_name: str = input("Input name you want for configuration file: ")
    conf_extension: str = os.path.splitext(conf_name)[-1].lower()
    repo_docker_url: str = input("\nInput Docker Repository URL: ")
    python_version: str = input("\nInput Python version (3.X.X): ")
    git_token: str = input("\nInput Github Token: ")
    git_repo: str = input("\nInput Github Repository: ")

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
    else:
        with open(conf_path, 'w')  as file:
            file.write("REPO_DOCKER_URL=" + repo_docker_url + "\n")
            file.write("PYTHON_VERSION=" + python_version + "\n")
            file.write("GIT_TOKEN=" + git_token + "\n")
            file.write("GIT_REPO=" + git_repo + "\n")
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

    # Ask user with wich params  he want to edit
    print("[green]\nParameters: docker_url, python_version, git_token, git_repo[/green]")
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
def create(edit: bool = typer.Option(False, help="Used to modify any existing configuration file")):
    """
    Create configuration file for Myd. :writing_hand:
    """
    init(autoreset=True)
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
    return

# Base value to navigate throw list with all parameter for more understanding
docker: int = 0
python: int = 1
git_token: int = 2
git_repo: int = 3


# Run shell scrit to build debian image
def build_debian(docker_url: str):
    subprocess.call(['sh', 'debian_myd/./build-debian.sh', docker_url])

# Run shell scrit to build python image
def build_python(python_version: str, docker_url: str):
    subprocess.call(['sh', 'python_myd/./build-python.sh', python_version, docker_url])

# Run shell scrit to build python image
def build_nginx(python_version: str, docker_url: str, git_token: str, git_repo: str):
    subprocess.call(['sh', 'nginx/./build-myd-docs.sh', python_version, docker_url, git_token, git_repo])

# Check if user want to build a specific container or all.

# Layer order: debian -> python -> nginx
def build_container(data: list, option: str):
    if (option != "debian") and (option != "python") and (option != "nginx") and (option != "all"):
        print("[[bold red]Error[/bold red]]: No such option '" + option + "'")
        raise typer.Exit(code=1)
    if (option == "debian"):
        build_debian(data[docker])
        print("[bold green]The debian container has been successfully built[/bold green]")
        print("[bold blue]Everything finished being built ![/bold blue]")
    if (option == "python"):
        build_debian(data[docker])
        print("[bold green]The debian container has been successfully built[/bold green]")
        build_python(data[python], data[docker])
        print("[bold green]The python container has been successfully built[/bold green]")
        print("[bold blue]Everything finished being built ![/bold blue]")
    if (option == "nginx") or (option == "all"):
        build_debian(data[docker])
        print("[bold green]The debian container has been successfully built[/bold green]")
        build_python(data[python], data[docker])
        print("[bold green]The python container has been successfully built[/bold green]")
        build_nginx(data[python], data[docker], data[git_token], data[git_repo])
        print("[bold green]The nginx container has been successfully built[/bold green]")
        print("[bold blue]Everything finished being built ![/bold blue]")
        
# Use to build container for server
@app.command(rich_help_panel="Commands :computer:")
def build(file: str = typer.Argument(...,help=help_build, metavar=termcolor.colored("File", 'red'), show_default=False), option: str = typer.Argument("all", help="Use to build specific container: debian, python, nginx", metavar=termcolor.colored("Option", 'red'))):
    """
    Build each Docker container as needed to run. :brick:
    """
    key_value: list = [docker, python, git_token, git_repo]
    file = error_conf_file(file)
    with open(file, 'r') as f:
        data: list = f.readlines()
    if (len(data) != 4):
        print("[[bold red]Error[/bold red]]: The configuration file is not well formatted, please regenerate one with the command 'python myd.py create'")
        raise typer.Exit(code=1)
    for i in key_value:
        check_valid_file(data, i)
        data[i] = data[i].split("=", 1)[1]
        data[i] = data[i].split("\n", 1)[0]
    build_container(data, option)

# ---------------------------------------------------------------------------

def check_ext_port(ext_port: str):
    if not ext_port.isnumeric():
        print("[[bold red]Error[/bold red]]: External port container other character than number, please put only number")
        raise typer.Exit(code=1)

@app.command(rich_help_panel="Commands :computer:")
def run(file: str = typer.Argument(...,help=help_build, metavar=termcolor.colored("File", 'red'), show_default=False), ext_port: str = typer.Argument(..., help="External port web server will use", metavar=termcolor.colored("External_port", 'red'), show_default=False)):
    """
    Launches the Nginx server. :rocket:
    """
    check_ext_port(ext_port)
    file = error_conf_file(file)
    docker: int = 0
    with open(file, 'r') as f:
        data: list = f.readlines()
    docker_url: str = data[docker].split("=", 1)[1]
    docker_url = docker_url.split("\n", 1)[0]
    subprocess.call(['sh', 'nginx/./run-nginx.sh', docker_url, ext_port])

if __name__ == "__main__":
    app()