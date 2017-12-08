# Distributivecom
A Distributive Computing Project
## Claim
This project is devoted to create a **Distributive Computing Environment** for the public via web application. (Project proposed to fulfill class requirement for BU EC 601)

## Project Description
A cross platform software aiming at creating a distributive computing environment for demanding
program. Client either provides computers for helping executing program to obtain credits or propose a
program task to distribute amongst available units by paying credits. (Can be substituted by watching
commercials.)

## Motivation
We are motivated in developing this project because of our interest in distributive system among IoTs,
potential finical benefits, and needs for such service from our own experience. The cooperation
between IoTs is an absolute trend towards smart grid and this project, we believe, will prepare us for a general understanding. we do acknowledge the difference between distributive system and computing, but we believe distributive computing will help studying the distributive system model.

## Users and Consumers
Users are people who are not using their computers for a long period of time and have constant
stable Internet access. These users would be interested in providing their computers for this service for
credits that can be used to for our service or potentially exchanged to their local currency. In other words, users are people who are
interested in signing up their computers for work with fixed amount of credit income depending on their
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

As their name suggested, **Server Control** runs on server and is in charge of temporary file storage, client information reserving, and file splitting. 

**Local Web UI** is built for customers interested in leasing their computers for financial benefits. This Local Web UI, acting as a cross platform application, after activation, will automatically interact with server and perform tasks. 

The **Website**, currently hosted at http://medusapys.site, is a client side UI for customers looking for hiring computers on Medusa.pys clusters. Clients will upload their file for computing on other computers that are part of our cluster nodes.

Website Testing result avaliable at http://www.webpagetest.org/result/171208_8Z_78ef41e76aa9df6ef1cd5b6e9a5aa3b1/

To communicate with peer and master computers, the project uses **Swarm** to host **Redis** clusters.



