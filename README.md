# OpenCube Simulator


A simulator for OpenCube.

At the moment the functionality is very, very, very limited.
But this will hopefully improve over time.

### Set-up.
If you are testing the simulator its better to set-up a  virtual environement.
This prevents the required python packages to mess up with your current python installation.

To create a virtual environment:

```
virtualenv env
```

Activate the virtual environment:

```
source env/bin/activate/
```

Install the SPG4 propagator for python:

```
pip install spg4
```

Install [RabbitMQ](http://www.rabbitmq.com/download.html).
Install the pika RabbitMQ python client:

```
pip install pika==0.9.8
```

### Starting the simulator.

If you are using a virtual environment activate it. 
Then start the propagator and the receiver in different terminal tabs or windows.

```
python Propagator.py
```

```
python Receiver.py
```

### License
The simulator is released under a BSD license.
