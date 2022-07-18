from pickle import TRUE
from platform import python_version
from typing import Optional
from rich import print as print
import rich.markup
import rich.markdown
from colorama import init, Fore, Back, Style
import typer
import os
import subprocess
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer(rich_markup_mode="markdown")

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

@app.command(rich_help_panel="Commands :computer:")
def create(edit: bool = False):
    """
    Create configuration file for Myd. :writing_hand:
    """
    init(autoreset=True)
    if not edit:
        if not os.path.isdir("conf"):
            create_dir("conf", os.getcwd())
        conf_name: str = input("Input name you want for configuration file: ")
        conf_extension: str = os.path.splitext(conf_name)[-1].lower()
        repo_docker_url: str = input("\nInput Docker Repository URL: ")
        python_version: str = input("\nInput Python version (3.X.X): ")
        git_token: str = input("\nInput Github Token: ")
        git_repo: str = input("\nInput Github Repository: ")
        if not conf_extension or conf_extension != ".conf":
            conf_name = conf_name.split(".", 1)[0]
            conf_name = conf_name + ".conf"
        conf_path: str = os.getcwd() + '/conf/' + conf_name
        if not os.path.exists(conf_path):
            with open(conf_path, 'a')  as file:
                file.write("REPO_DOCKER_URL=" + repo_docker_url + "\n")
                file.write("PYTHON_VERSION=" + python_version + "\n")
                file.write("GIT_TOKEN=" + git_token + "\n")
                file.write("GIT_REPO=" + git_repo + "\n")
            raise typer.Exit(code=0)
        else:
            with open(conf_path, 'w')  as file:
                file.write("REPO_DOCKER_URL=" + repo_docker_url + "\n")
                file.write("PYTHON_VERSION=" + python_version + "\n")
                file.write("GIT_TOKEN=" + git_token + "\n")
                file.write("GIT_REPO=" + git_repo + "\n")
            raise typer.Exit(code=0)
    else:
        if not os.path.isdir("conf"):
            create_dir("conf", os.getcwd())
        print("[green]Files: ", os.listdir(os.getcwd() + "/conf"))
        file_name: str = input("\nPlease enter which file you want edit: ")
        file_path: str = os.getcwd() + "/conf/" + file_name
        if not os.path.exists(file_path) or not file_name:
            print("[[bold red]Error[/bold red]]: No such file '" + file_name + "'")
            raise typer.Exit(code=1)
        print("[green]\nParameters: docker_url, python_version, git_token, git_repo[/green]")
        param: str = input("\nPlease select which parameter you want edit: ")
        line: int = get_param(param)
        with open(file_path, 'r') as file:
            data = file.readlines()
        print(data[line])
        data[line] = data[line].split("=", 1)[0] + "="
        param_value: str = input("\n\nPlease enter new value: ")
        data[line] = data[line] + param_value + "\n"
        print(data[line])
        with open(file_path, 'w') as file:
            file.writelines(data)
        raise typer.Exit(code=0)

@app.command(rich_help_panel="Commands :computer:")
def build():
    """
    Build each Docker container as needed to run. :brick:
    """
    j = 12

@app.command(rich_help_panel="Commands :computer:")
def run():
    """
    Launches the Nginx server. :rocket:
    """
    j = 12

if __name__ == "__main__":
    app()