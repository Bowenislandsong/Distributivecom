# Distributivecom
EC 601 Group Distributive Computing 
## Claim
This Project is devoted to class EC 601 as a Distributive Computing software for the public.
Project Proposal

## Project Description
A cross platform software tool aiming at creating a distributive computing environment for demanding
programs. Client either provide computers for helping executing program to obtain credits or propose a
program task to distribute amongst available units by paying credits. (Can be substituted by watching
commercials.)
## Motivation
I am motivated in developing this project because of my interest in distributive system among IoTs,
potential finical benefits, and my previous needs for such service. I have previously designed a
demanding medical image processing software on MATLAB. The processing time for a simple picture can
take up to hours and a complicated high definition picture of cells can take up to days. The cooperation
between IoTs is an absolute trend towards smart grid and this project, I believe, will prepare me for my
interest. I do acknowledge the difference between distributive system and computing, but I believe
distributive computing will help me to study the distributive system model.
## Users and Consumers
Users are mainly people who are not using their computers for a long period of time and have constant
stable Internet access. These users will be interested in providing their computers for this service for
credits that can be exchanged to their local currency. In other words, users are people who are
interested in signing up their computers for work with fixed amount of salaries depending on their
computing powers. The consumers, who will be paying for the service, can execute their program on
multiple computers to speed up the program execution process.
## Competitors
Current leading competitors are BOINC and MATLAB. BOINC only allows well founded super labs be the
proposing side while volunteering clients are only motivated for the contribution for big topic science.
General public is not allowed to propose a program for the service. MATLAB only supports MATLAB
scripted programs.
## Minimum Value Product (MVP)
The Minimum Value Product is the version of a new product with a collection of essential features that satisfy
the early users. Our MVP is a *User Interface* with **Low Latency** response to **Real-Time** machine learning 
and other **Iterative** tasks.
## Current Project Structure
The project is currently split into three components: Server Control, Local Web UI, and Website. 

As their name suggested, *Sever Control* runs on server and is in charge of temporary file storage, client information reserving, and file splitting. 

*Local Web UI* is built for customers interested lensing their computers for financial benefits. This Local Web UI, acting as a cross platform application, after activation, will automatically interact with server and perform tasks. 

The *Website*, currently hosted at http://medusapys.ml, is a client side UI for customers looking for hiring computers on Medusa.pys clusters. Clients will upload their file for computing on other computers that are part of our cluster nodes. 

To communicate with peer and master computers, the project uses *Swarm* to host *Redis* clusters.
