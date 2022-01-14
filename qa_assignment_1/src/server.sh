# building image
docker build server -t lab1_image --build-arg "PORT=$1"

# creating volume
docker volume create lab1_volume

# run container with port $1
docker run -it --rm -p $1:$1 -d -v lab1_volume:/serverdata --name server lab1_image

$SHELL