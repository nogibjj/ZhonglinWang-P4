# Project-4-AWS-Jiaxin-Ying
[![Python application test with Github Actions](https://github.com/nogibjj/Project-4-API-AWS-Jiaxin-Ying/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Project-4-API-AWS-Jiaxin-Ying/actions/workflows/test.yml)

This is project 4 from Jiaxin Ying for IDS706 course.

## Key Objectives of Project
In project 4, the purpose is to build continuous delivery of FastAPI Data Engineering on AWS. I scaffold a simple Wikipedia searcher project via Python. Users only need to use "search" to enter the topic they are interested in at the webpage port, they can see the keywords related to that topic, so that to select the subject they want to know. Secondly, users can use "phrase" to enter that subject, then they can get the entry related to that subject, and then select the entry they are intrested in. Finally, they use the "wiki" to search for such entry, after that, they can see the basic introduction or definition of this entry.  This API acts as a simple Wikipedia fetcher that allows us to learn basic information, concepts and definitions of something we are interested in.

## Structure Diagram
<img width="1025" alt="Screen Shot 2022-11-11 at 3 54 32 AM" src="https://user-images.githubusercontent.com/112274822/201303469-c12f14a2-f644-4e71-9796-07de12a93b7a.png">

## Demo Video Link
https://teams.microsoft.com/l/message/19:acc4415fc1474fc9975253c1caa8e192@thread.tacv2/1667871811154?tenantId=cb72c54e-4a31-4d9e-b14a-1ea36dfac94c&groupId=428262e3-7a97-45de-8ed6-eb751b9cb87c&parentMessageId=1667871811154&teamName=IDS.706.01.F22&channelName=Week%2011%20Demo&createdTime=1667871811154&allowXTenantAccess=false

## Advance Preparation
### 1. Setup virtual environment
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. 
* Type: `python3 -m venv ~/.venv`

### 2. Setup continuous integration via a new workflow at Github
A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.
* Go to the homepage of the repository, cilck the button "Actions", choose "set up a workflow yourself".
* Name it as "test.yml", type the code you need, then click the green button "start commit".
<img width="605" alt="Screen Shot 2022-11-10 at 11 53 45 PM" src="https://user-images.githubusercontent.com/112274822/201286707-a5994190-0805-4d2e-955f-85d7a26703bf.png">

* Once complete these steps, you can check the status of your workflows from "Actions" page, so that make sure your program could pass the tests. Otherwise, you need to fix the code where the bugs/errors arw reported.
* eg. Check out code for issues such as pylint and pytest errors:
<img width="894" alt="Screen Shot 2022-11-11 at 12 19 42 AM" src="https://user-images.githubusercontent.com/112274822/201286757-89650751-a24c-481a-9863-f2beefe16471.png">

### 3. Add requirements.txt
Requirement. txt file is a type of file that usually stores information about all the libraries, modules, and packages in itself that are used while developing a particular project. It also stores all files and packages on which that project is dependent or requires to run. Here are the packages I will use for this project:

<img width="179" alt="Screen Shot 2022-11-11 at 12 06 21 AM" src="https://user-images.githubusercontent.com/112274822/201286426-f855ec7b-dfa3-4d15-a138-c7f7f697ca21.png">

### 4. Create a Makefile
A makefile is a special file that lists a set of rules for compiling a project. These rules include targets, which can be an action make needs to take (eg. "clean" or "build") or the files/objects make will need to build, and the commands that need to be run in order to build that target. 
* Type: `touch Makefile` and `make install` after adding requirement.txt
<img width="1202" alt="Screen Shot 2022-11-10 at 11 59 57 PM" src="https://user-images.githubusercontent.com/112274822/201286091-80078ec4-6abf-4379-8a6b-5f2c91bcf5ba.png">

* Once Makefile is built, add the code you need. When you call the program make, it runs through each of these targets in your Makefile and executes them.

## Steps of Configure Build Server to Deploy Changes on build (Continuous Delivery)

### 1. Create a Microservice that returns a JSON payload and performs tasks
* Build three logic functions for Wikipedia scraper (search_wiki, phrase, and wiki) at logic.py:
<img width="592" alt="Screen Shot 2022-11-11 at 12 29 56 AM" src="https://user-images.githubusercontent.com/112274822/201287617-77aa2c39-f695-449e-aa15-1edad2714d40.png">

* Use Python Fire library to build CLI at cli-fire.py, get permission by typing `chmod +x cli-fire.py`, and use `./cli-fire.py --help` to test logic within it:
<img width="218" alt="Screen Shot 2022-11-11 at 2 21 50 AM" src="https://user-images.githubusercontent.com/112274822/201287846-6cfc6ff1-11c9-480a-878c-9f4651077f96.png">

* Use FastAPI to build a Microservice which scaffolds a simple Wikipedia searcher at main.py via `python main.py`:
<img width="652" alt="Screen Shot 2022-11-11 at 12 30 32 AM" src="https://user-images.githubusercontent.com/112274822/201287093-08fda7da-259c-428d-baea-f5e5e3fe06c4.png">
<img width="621" alt="Screen Shot 2022-11-10 at 11 48 58 PM" src="https://user-images.githubusercontent.com/112274822/201287140-086c4121-4bd1-4974-883d-2e7c8e380b22.png">

* Use `/docs` to check Microservice function:
<img width="1296" alt="Screen Shot 2022-11-10 at 11 44 46 PM" src="https://user-images.githubusercontent.com/112274822/201287227-0f47af99-9a3d-40be-b2e3-a7692d7c0047.png">
<img width="1140" alt="Screen Shot 2022-11-10 at 11 45 14 PM" src="https://user-images.githubusercontent.com/112274822/201287332-e452eec3-c566-42e8-ab9e-201ab464b168.png">
<img width="1142" alt="Screen Shot 2022-11-10 at 11 45 59 PM" src="https://user-images.githubusercontent.com/112274822/201287371-2b9047f9-7151-4d0c-a5ad-e7bee34f5d91.png">
<img width="1139" alt="Screen Shot 2022-11-10 at 11 46 42 PM" src="https://user-images.githubusercontent.com/112274822/201287418-eb29bbf0-5a11-48de-96fe-ce85faca7620.png">

* Direclty call `/search` or `/wiki` or `/phrase` after the website link to apply FastAPI:
<img width="1401" alt="Screen Shot 2022-11-10 at 11 47 34 PM" src="https://user-images.githubusercontent.com/112274822/201287528-bd7d87a7-76f0-41aa-b5b5-a233bece0b8a.png">
<img width="1499" alt="Screen Shot 2022-11-10 at 11 48 01 PM" src="https://user-images.githubusercontent.com/112274822/201287541-a12365c3-a9f5-44bf-806c-320d778999e5.png">
<img width="1484" alt="Screen Shot 2022-11-10 at 11 48 24 PM" src="https://user-images.githubusercontent.com/112274822/201287558-bc28635b-05f3-4d8b-8d64-ada2d33ee54b.png">

### 2. Containerized FastAPI
* Build container: type `docker build -t deploy-fastapi .` at Makefile, then run: `make build`
* Run docker: type `docker image ls` to find image id, then at Makefile, run: `docker run -p 127.0.0.1:8080:8080 b17ba0bd8c50`

### 3. Push the repo to ECR (Elastic Container Registry) at AWS
* Login to AWS, go to ECR and create a new repository at first, the go to repo image page, click "View push commands", copy all of the token at Makefile.
<img width="1459" alt="Screen Shot 2022-11-11 at 1 21 54 AM" src="https://user-images.githubusercontent.com/112274822/201290150-46b3e5cf-f920-421d-9fdc-c72e9f8d2983.png">
<img width="803" alt="Screen Shot 2022-11-11 at 1 24 33 AM" src="https://user-images.githubusercontent.com/112274822/201286501-2c3b1b18-19c3-4e9d-a2f2-be002bf401b7.png">

* Continuous delivery can be reached by `make deploy` command:
<img width="968" alt="Screen Shot 2022-11-11 at 1 27 23 AM" src="https://user-images.githubusercontent.com/112274822/201286839-ecc4a7ef-4785-471f-a0aa-1e9bc8d85f0b.png">

### 4. Use AWS CodeBuild to Check Continuous Delivery
* At AWS, got to CodeBuild, then click "Create build project":
<img width="1406" alt="Screen Shot 2022-11-11 at 1 33 20 AM" src="https://user-images.githubusercontent.com/112274822/201286912-1a4a524e-7303-47ee-8cc8-807b29ea371a.png">
<img width="813" alt="Screen Shot 2022-11-06 at 10 30 05 PM" src="https://user-images.githubusercontent.com/112274822/201288041-83a937ad-327e-4bc0-a134-5d5df4e5029f.png">
<img width="802" alt="Screen Shot 2022-11-06 at 10 30 19 PM" src="https://user-images.githubusercontent.com/112274822/201288114-35b56d16-f189-42b0-8cc7-52f2293def10.png">
<img width="791" alt="Screen Shot 2022-11-06 at 10 30 39 PM" src="https://user-images.githubusercontent.com/112274822/201288133-6905e2fe-009c-40d0-b450-f7304373227f.png">

* Continuous delivery can also be reached through setting up buildspec.yaml, we can copy the code from "Insert build commands" and then build a buildspec.yaml at repo. Once done, click "Use a buildsepc file":
<img width="786" alt="Screen Shot 2022-11-06 at 10 33 53 PM" src="https://user-images.githubusercontent.com/112274822/201288237-27f8edff-8dcb-45d4-9703-e12c9b89a3b9.png">
<img width="190" alt="Screen Shot 2022-11-11 at 1 17 46 AM" src="https://user-images.githubusercontent.com/112274822/201286268-8225381d-0e8f-43e0-a94f-d70cb17a6e50.png">

* When setting up environment image, we need to create ARN Role here, go to AWS, search "Identity and Access Management (IAM)" to manage access to AWS resources. On console, choose "Roles", click "Create role":
<img width="631" alt="Screen Shot 2022-11-06 at 10 52 44 PM" src="https://user-images.githubusercontent.com/112274822/201288492-9fef29c9-7037-4ceb-bcd1-1554ae5d2440.png">
<img width="1417" alt="Screen Shot 2022-11-11 at 2 30 05 AM" src="https://user-images.githubusercontent.com/112274822/201289132-a4671795-8c77-4b5b-add1-b766202ea89b.png">
<img width="1098" alt="Screen Shot 2022-11-06 at 10 45 28 PM" src="https://user-images.githubusercontent.com/112274822/201289155-87946cd8-32a3-4d38-824d-b31168058f0b.png">
<img width="1074" alt="Screen Shot 2022-11-06 at 10 46 58 PM" src="https://user-images.githubusercontent.com/112274822/201289173-333d43f3-adf1-43c2-a8dd-6eb4d8d82cfb.png">

* Once the ARN is created, match it at "Role ARN" when creating build project:
<img width="631" alt="Screen Shot 2022-11-06 at 10 52 44 PM" src="https://user-images.githubusercontent.com/112274822/201289249-2235247d-da27-434c-b888-88863b5f21ca.png">
<img width="589" alt="Screen Shot 2022-11-11 at 2 32 09 AM" src="https://user-images.githubusercontent.com/112274822/201289371-1b4421f1-3c7b-4bea-912d-a4d906bc0640.png">

* Finally, click "Start build", check the "Buid status", to make sure you pass all tests successfully. Otherwise, please find the errors from "Phase details" to debug.
<img width="1434" alt="Screen Shot 2022-11-06 at 10 55 32 PM" src="https://user-images.githubusercontent.com/112274822/201290892-6e965b73-40bc-4e68-ae21-512ebdfc5ed8.png">
<img width="1395" alt="Screen Shot 2022-11-11 at 1 50 18 AM" src="https://user-images.githubusercontent.com/112274822/201286353-aac3fe0b-7a2c-4a2d-986b-16e6a4d02f83.png">
