install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

post-install:
	python -m textblob.download_corpora

format:
	black *.py mylibrary/*.py

lint:
	pylint --disable=R,C *.py mylibrary/*.py

test:
	python -m pytest -vv --cov=mylibrary --cov=main test_*.py

build:
	docker build -t deploy-fastapi .

run:
	#run docker
	
deploy:
	#pushes container to ECR
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 766481746749.dkr.ecr.us-east-1.amazonaws.com
	docker build -t arxiv .
	docker tag arxiv:latest 766481746749.dkr.ecr.us-east-1.amazonaws.com/arxiv:latest
	docker push 766481746749.dkr.ecr.us-east-1.amazonaws.com/arxiv:latest
	docker login -u AWS -p $(aws ecr get-login-password --region the-region-you-are-in) xxxxxxxxx.dkr.ecr.the-region-you-are-in.amazonaws.com

all: install post-install lint test deploy