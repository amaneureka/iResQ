# Hack@NSIT

[![License](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat)](https://github.com/amaneureka/iResQ/blob/wol/LICENSE)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/amaneureka/iResQ/issues)

	.____________              ________   
	|__\______   \ ____   _____\_____  \  
	|  ||       _// __ \ /  ___//  / \  \ 
	|  ||    |   \  ___/ \___ \/   \_/.  \
	|__||____|_  /\___  >____  >_____\ \_/
	           \/     \/     \/       \__>

# Team `xkcd`

- [Manoj Pandey](https://github.com/manojpandey)
- [Aman Priyadarshi](https://github.com/amaneureka)
- [Laksh Arora](https://github.com/techedlaksh)
- [Akul Mehra](https://github.com/akul08)

---

# ABOUT THE PROJECT
---

#What it does
We are trying to solve the problem of locating people in times of any natural disaster or calamity.

We give the rescue teams who look into `disaster management`, some beacons, which are just `~3.3 inch` in size to carry with themselves to places where there is a disaster, and spread the beacons around the affected area.

Along with the beacons, we also have our Android Mobile App, which gives an interface leveraging the `heat maps` and display it on the app.

The heat maps is a generalization of the amount of activity which is directly linked with the probability of finding a person near a particular beacon.

In the back end, we get the temperature and motion data, which is being feeded to our server, where some `Machine Learning` is being done using some `Neural Networks`behind the scenes and we process and send the probabilistic data back to the `Android app` and then generating the heat maps correspondingly.

## Locating people in no time
	As we are using Estimote beacons right now, so it makes it pretty easy to detect any motion activity around the area where the beacons are spread across in the place of disaster.		

## Intimate rescue teams intelligently to act at the earliest
	

## 


---

# How I built it

## Android App
* Integrate Estimote SDK
* Gaussian Distribution for heat maps
* Google Maps API

## Web server and Dashboard
* Showcase of the app on the landing page
* Web server


## Machine Learning for predictions
	We are using Linear Classifier to train the data using a Sigmoid Layer neuron, and training the dataset for some good number of iterations.

---

# Challenges we ran into
* Working with Cloud Estimote SDK
* Building the DataSet
* Number of neurons in hidden layers




---

## What's next for iResQ

* We have made the complete product, so we are thinking to launch it in the market.
* Talk with Disaster Management teams in the Government
* Field Study with engineers and
* Access from anywhere
	* RPI
	* Internet
* Research Study
	* Earthquake study
	* Predictions on volcanic eruptions 

## Other Extensions 
* Security Sureveillance in banks
* Monitoring home



## Built With

* Python
* Flask
* Android
	* Google Maps API
		* Heat Maps
	* Estimote SDK
		* Low Bluetooth Energy (LBE)
* Estimote Beacons
	* Motion Sensors
	* Temperature Sensors
	* Waterproof encasing
* Machine Learning
	* Neural Networks
		* PyBrain
		* Linear Classifier
		* Sigmoid layers
* HTML5
* CSS3
* Javascript

# How to Contribute
> Feel free to ping and say `Hi ! :D`