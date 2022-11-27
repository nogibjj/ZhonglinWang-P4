# project-4 Zhonglin Wang
Project #4: Continuous Delivery of FastAPI API hosted on AWS

Perform Continuous Integration with Github Actions

## 2. Create Docker Image
`docker build -t deploy-fastapi .` 

<img width="721" alt="image" src="https://user-images.githubusercontent.com/112585430/204142895-9381f37e-a2fd-4606-90fb-8ebdc6efa681.png"> 

`make build`  

<img width="721" alt="image" src="https://user-images.githubusercontent.com/112585430/204142999-671e7aae-dbd4-4593-a298-1693d5736529.png"> 

`docker run -p 127.0.0.1:8080:8080 b8d6c01d8a3d` 

<img width="721" alt="image" src="https://user-images.githubusercontent.com/112585430/204143816-3baa62f9-47b2-4890-9396-2de2bcad6560.png"> 

1
