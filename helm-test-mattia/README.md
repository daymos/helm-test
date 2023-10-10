Mattia Spinelli's submission to Co:Helm coding challenge

How to run the notebook
The easiest way is to load the notebook in colab and follow the instructions in the notebook.

How to run the docker image
I tested the docker image on a Linux Fedora11, with 64 GB + RTX6000 GPU x2 and it ran fine without quantization.
I used these commands:

docker build . -t app
docker run -d app
docker logs app --follow to see the results. 


Note
The notebook and the docker image diverge a little due to refactoring in going from the notebook to python repo and to last-minute improvements applied to the notebook
that I didn't port to the python app.



