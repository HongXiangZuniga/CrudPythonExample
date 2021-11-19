run:
	pip install -r requirements.txt
	python main.py

setup: requirements.txt
	pip install -r requirements.txt

docker-build:
	docker build \
	-f build/docker/Dockerfile \
	-t  portafolio:local .

docker-run:
	docker run --rm -it -p 5000:5000 \
	--env-file ./.env \
	portafolio:local