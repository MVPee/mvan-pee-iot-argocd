# IoT Argo CD Configuration

Kubernetes manifests for Inception-of-Things Part 3.

## Project
Inception-of-Things (IoT) - K3d and Argo CD

## Structure

- `deployment.yaml` - Application Deployment
- `service.yaml` - Application Service
- `ingress.yaml` - Ingress configuration

## Application

Custom Flask application with two versions:
- v1: Basic JSON response
- v2: Enhanced with timestamp and /info endpoint

## Docker Images

- `mvpee/iot-app:v1`
- `mvpee/iot-app:v2`

## GitOps Workflow

This repository is monitored by Argo CD. Changes pushed to `main` branch are automatically deployed to the cluster.

To update application version:
1. Edit `deployment.yaml`
2. Change `image: mvpee/iot-app:v1` to `v2`
3. Commit and push
4. Argo CD will automatically sync
