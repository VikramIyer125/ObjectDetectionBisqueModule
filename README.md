# ObjectDetectionBisqueModule
This is a BisQue Module that detects objects in images. 
It was made to test the BisQue Module developer found at https://github.com/UCSB-VRL/BQ_module_generator. 

Steps to run this module are as follows. 

1. Have a Directory structure as shown below, with a Modules folder, and each module as a subfolder within the Modules folder. In my case, the module is called EdgeDetection. 
`
<img width="726" alt="Screen Shot 2022-06-13 at 11 42 38 AM" src="https://user-images.githubusercontent.com/42392910/173422763-b0806d29-2b28-4a59-b37d-c2c7f6fede4f.png">

2. Clone the Repo 
```console 
user@machine: ~/Modules$ git clone -b master https://github.com/VikramIyer125/ObjectDetectionBisqueModule.git
```

3. Build the docker image 
```console 
vikram@lambda-quad:~/bisque_module_testing$ cd ObjectDetectionBisqueModule/

vikram@lambda-quad:~/Modules/ObjectDetectionBisqueModule$ docker build -t biodev.ece.ucsb.edu:5000/edgedetection:v1.0.0 .

```
4. Run the Bisque Image 

```console 
vikram@lambda-quad:~/Modules: docker run --name bisque --rm -p 8080:8080 -v $(pwd):/source/modules -v /var/run/docker.sock:/var/run/docker.sock amilworks/bisque-module-dev:git

```

5. Navigate to Bisque 

Go to this link: ```http://{your.private.ip.address}:8080/```

Instructions for using the module can be found at https://github.com/UCSB-VRL/BQ_module_generator
