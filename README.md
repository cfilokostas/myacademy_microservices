Django Microservices eLearning Project

This is an e-learning course system built with Django and a microservices architecture.

Microservices Overview

The system is composed of the following microservices:

1. my_academy (MAIN)
Acts as the gateway, using proxies to route each request to the appropriate microservice.

2. users
Handles user management and authentication.

3. courses
Manages course creation, enrollment, and related operations.

4. virtual_payments
A virtual wallet service that allows users to purchase available courses.

Purpose

The project is designed to compare the advantages and disadvantages of using a microservices architecture versus a more traditional WordPress-based solution.

You can find the WordPress edition of this project here: www.myacademy.gr
