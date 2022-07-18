#################################################################################
# Name of file : init-file.sh
#
# Create at      : 11/07/2022 9:00:28
# Create by     : [Lenny Delgado]
# -------------------------------------------------------------------------------------
# Description   : This script will generate for you a configuration file named config.txt used by build-myd-project in conf directory
#
# -------------------------------------------------------------------------------------
#
# Exemple       : ./init-file.sh
#
#################################################################################

# Get name of conf file
read -p "Input name you want for configuration file: " CONF_NAME

# Get Repository of your Docker conteiner and put it in config file
read -p "Input Docker Repository URL: " REPO_DOCKER_URL
echo "REPO_DOCKER_URL=$REPO_DOCKER_URL" > conf/$CONF_NAME.txt

# Get Python version you want for your Docker conteiner
read -p "Input Python version (3.X.X): " PYTHON_VERSION
echo "PYTHON_VERSION=$PYTHON_VERSION" >> conf/$CONF_NAME.txt

# Get tocken of your github account
read -p "Input Github Token: " GIT_TOKEN
echo "GIT_TOKEN=$GIT_TOKEN" >> conf/$CONF_NAME.txt

# Get your repository with mkdocs
read -p "Input Github Repository: " GIT_REPO
echo "GIT_REPO=$GIT_REPO" >> conf/$CONF_NAME.txt

# Get your external port you want use for nginx
read -p "Input external port: " EXT_PORT
echo "EXT_PORT=$EXT_PORT" >> conf/$CONF_NAME.txt