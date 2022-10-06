FROM ubuntu:20.04

RUN apt update -y
RUN apt install -y python3 python3-pip git
RUN pip3 install numpy matplotlib

WORKDIR /diffusion_sod

RUN git clone https://github.com/sozgundemir/diffusion2D-testing-exercise.git
CMD ["echo", "Hi there!"]
CMD ["echo", "Now `diffusion2d.py` code will be run automatically."]
CMD ["python3 diffusion2d.py"]
CP output.png .
CMD ["echo", "See you later."]
