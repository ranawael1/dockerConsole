
# docker build --tag name:tag .
IMAGE_ID=$(sudo docker build --tag ${1}:${2} . 2>/dev/null | awk '/Successfully built/{print $NF}')

