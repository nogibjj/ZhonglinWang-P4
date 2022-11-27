# project-4 Zhonglin Wang
Project #4: Continuous Delivery of FastAPI API hosted on AWS

Perform Continuous Integration with Github Actions  

## 1. Distribute microservices using FastAPI 
Define Arxivscraper function that gets papers published on Arxiv from 2022-05-27 to 2022-06-07 (the interval can be changed anytime)
<img width="809" alt="image" src="https://user-images.githubusercontent.com/112585430/204144434-1efbbcc0-128c-42bb-bbcd-140d2854af4b.png"> 



## 2. Create Docker Image
`docker build -t deploy-fastapi .` 

<img width="721" alt="image" src="https://user-images.githubusercontent.com/112585430/204142895-9381f37e-a2fd-4606-90fb-8ebdc6efa681.png"> 

`make build`  

<img width="721" alt="image" src="https://user-images.githubusercontent.com/112585430/204142999-671e7aae-dbd4-4593-a298-1693d5736529.png"> 

`docker run -p 127.0.0.1:8080:8080 b8d6c01d8a3d` 

<img width="721" alt="image" src="https://user-images.githubusercontent.com/112585430/204143816-3baa62f9-47b2-4890-9396-2de2bcad6560.png"> 

1
