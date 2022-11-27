# project-4 Zhonglin Wang
Project #4: Continuous Delivery of FastAPI API hosted on AWS

Perform Continuous Integration with Github Actions  

## 1. Deploy microservices using FastAPI 
Define Arxivscraper function that gets papers published on Arxiv from 2022-05-27 to 2022-06-07 (the interval can be changed anytime)
<img width="809" alt="image" src="https://user-images.githubusercontent.com/112585430/204144434-1efbbcc0-128c-42bb-bbcd-140d2854af4b.png"> 

Then use FastAPI to build an Arxiv article searcher checking with command `python main.py` 
<img width="733" alt="image" src="https://user-images.githubusercontent.com/112585430/204144629-13270a38-063e-4476-b79b-708990f3a83d.png"> 

## 2. Test FastAPI app 

`python main.py` 

<img width="1366" alt="image" src="https://user-images.githubusercontent.com/112585430/204164891-e9374837-5a7e-4ede-990e-b54a53d04e81.png"> 
click"Open in Browser" 

<img width="1728" alt="image" src="https://user-images.githubusercontent.com/112585430/204164933-cf61ce02-b228-4d1f-850b-3a181128f580.png"> 
type /docs after .dev in the URL bar 

<img width="1422" alt="image" src="https://user-images.githubusercontent.com/112585430/204165004-9669b6a3-8bba-480e-8cc8-9fed428ca669.png"> 

Try it out by enter "physics:nucl-th" to see the collection of Nuclear Theory papers published on Arxiv through 2022-05-27 to 2022-06-07.  
<img width="1422" alt="image" src="https://user-images.githubusercontent.com/112585430/204165156-997c89d7-112d-4dbc-b457-a586510f287d.png">

## 3. Create Docker Image
`docker build -t deploy-fastapi .` 

<img width="721" alt="image" src="https://user-images.githubusercontent.com/112585430/204142895-9381f37e-a2fd-4606-90fb-8ebdc6efa681.png"> 

`make build`  

<img width="721" alt="image" src="https://user-images.githubusercontent.com/112585430/204142999-671e7aae-dbd4-4593-a298-1693d5736529.png"> 

`docker run -p 127.0.0.1:8080:8080 b8d6c01d8a3d` 

<img width="721" alt="image" src="https://user-images.githubusercontent.com/112585430/204143816-3baa62f9-47b2-4890-9396-2de2bcad6560.png"> 
