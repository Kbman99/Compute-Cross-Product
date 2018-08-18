# Flask-Startup

## Setup

## Docker deployment

The current application can be deployed with Docker [in a few commands](https://realpython.com/blog/python/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/).

```sh
cd ~/path/to/application/
docker-machine create -d virtualbox --virtualbox-memory 1024 --virtualbox-cpu-count 1 dev
docker-machine env dev
eval "$(docker-machine env dev)"
docker-compose build
docker-compose up
docker-compose run web flask initdb --rm (remove container after running one off command)
```

Then access the IP address given by `docker-machine ip dev` and it should do the trick.

## License

The MIT License (MIT). Please see the [license file](LICENSE) for more information.
