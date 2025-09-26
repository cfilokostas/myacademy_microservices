Django Microservices eLearning Project

This is an e-learning course system built with Django and a microservices architecture.

Microservices Overview

The system is composed of the following microservices:

my_academy (MAIN)
Acts as the gateway, using proxies to route each request to the appropriate microservice.

users
Handles user management and authentication.

courses
Manages course creation, enrollment, and related operations.

virtual_payments
A virtual wallet service that allows users to purchase available courses.

Purpose

The project is designed to compare the advantages and disadvantages of using a microservices architecture versus a more traditional WordPress-based solution.

You can find the WordPress edition of this project here: www.myacademy.gr
