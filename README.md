# UdaConnect-Microservices
Udacity's Monolith to Microservices Project

---
# Introduction

This repository contains one of the projects in the Cloud Native Application Architecture Nanodegree. It involves an application called UdaConnect used for professionals in conferences and conventions to create valuable business and professional connections between each other. To help attendees make connections, we are building the infrastructure for a service that can inform attendees if they have attended the same booths and presentations at an event. A proof of concept has already been developed in the form of a monolith architecture. The goal is refactor the application to microservices using message passing tools (REST, gRPC, and Kafka).

---
# Requirements

Please make sure that followings are setup:
- Helm
- Kubectl
- Virtual Box
- Vagrant

---
# Step-by-step Guide

## Step 1: Setting Up Virtual Machine

`cd` into the repository folder.

`cd UdaConnect Microservices`

Set up the virtual machine using Vagrant.

`vagrant up`

Enter the virtual machine.

`vagrant ssh`

Copy the content from `k3s.yaml` by running

`sudo cat /etc/rancher/k3s/k3s.yaml`

and paste it to `.kube/config` (if the `config` file does not exists, create one).

Note: to shutdown the virtual machine, run `vagrant halt`

## Step 2: Deploy Kafka Service using Helm

Run the following commands

`helm repo add bitnami https://charts.bitnami.com/bitnami`

`helm install --set externalAccess.enabled=true --set externalAccess.service.type=NodePort --set externalAccess.service.nodePorts[0]='9092' my-release bitnami/kafka`

Note: to remove the service, run `helm delete my-release`

## Step 3: Initialize Postgres Database

Deploy postgres service.

`kubectl apply -f deployment/postgres.yaml`

Retrieve the postgres pod name.

`kubectl get pods`

Seed the database.

`sh scripts/run_db_command.sh <POD_NAME>`

## Step 4: Deploy API and application services

Location gRPC service

`kubectl apply -f deployment/location-grpc.yaml`

Location Kafka Consumer Service

`kubectl apply -f deployment/location-consumer.yaml`

Person REST API Service

`kubectl apply -f deployment/person-api.yaml`

Person REST API Service

`kubectl apply -f deployment/person-api.yaml`

UdaConnect App Frontend Service

`kubectl apply -f deployment/frontend.yaml`
