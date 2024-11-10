# Insider Automation Test Framework

## Overview
This system automates end-to-end testing by deploying a Test Controller Pod (which initiates and manages test execution) and Chrome Node Pods (where browser tests run) on a Kubernetes cluster. Using a Selenium Grid setup, the Test Controller Pod collects and sends test cases to the Chrome Node Pods, ensuring efficient and isolated test execution.


## System Architecture
### **Test Controller Pod**  
Manages test execution. Connects to Selenium Grid (hosted on the Selenium Hub Pod) and runs tests on Chrome instances in the Chrome Node Pods.  
### **Selenium Hub Pod**  
Manages the Selenium Grid, facilitating communication between test requests and available browser nodes.  
### **Chrome Node Pods**  
Each pod provides a Chrome browser instance for executing tests.  
### **Inter-Pod Communication**  
Enabled by Kubernetes' internal DNS and service discovery, allowing the Test Controller Pod to communicate with the Selenium Hub using its service name (`selenium-hub`).  
<br>
## Inter-Pod Communication
### **Service Discovery with Kubernetes DNS**  
Kubernetes DNS allows each pod to communicate using service names. The Test Controller Pod connects to the Selenium Hub Pod using the internal service name selenium-hub.

### **Sending Test Cases**  
The Test Controller Pod sends test execution commands to Selenium Grid by targeting the selenium-hub service on port 4444. The Selenium Hub then distributes test cases to available Chrome Node Pods.

### **Scaling Chrome Nodes**  
The system can scale Chrome Node Pods dynamically based on the node_count parameter in deploy_and_run_tests.py. This parameter adjusts the number of Chrome instances to handle the test load, allowing efficient parallel execution of test cases.  
<br>


## Deployment Guide

### Prerequisites
- Docker and `kubectl` installed locally
- An AWS account with access to EKS (if deploying on AWS)
- `eksctl` for AWS EKS setup

### Local Deployment (Using Minikube)
1. **Start Minikube**:
   ```bash
   minikube start
   
2. **Build Docker Images: Use Minikube’s Docker daemon to build images**:

   Linux
   ```bash
   val $(minikube docker-env)  
   ```
   
   Windows
   ```bash
   minikube -p minikube docker-env | Invoke-Expression

4. **Build Docker Images: Build the Docker images for the Test Controller and Chrome Node**:
   ```bash
   docker build -t test-framework:local .
5. **Run Tests: Execute the Python deployment script to initiate test execution**:
   ```bash
   python deploy_and_run_tests.py local

<br>

  ### AWS EKS Deployment
1. **Install eksctl**:
   ```bash
   curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
   sudo mv /tmp/eksctl /usr/local/bin
   
3. **Install kubectl**:
   ```bash
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.0/2024-09-12/bin/linux/amd64/kubectl
   chmod +x ./kubectl
   sudo mv ./kubectl /usr/local/bin
   kubectl version --client

4. **Create EKS Cluster: Create an EKS cluster with eksctl**:
   ```bash
   eksctl create cluster --name insider-automation-cluster --region <your-region> --nodes n

5. **Authenticate kubectl with EKS: Update kubectl context to connect to the EKS cluster**:
   ```bash
   aws eks --region <your-region> update-kubeconfig --name insider-automation-cluster
6. **Push Docker Images to ECR**:  
   - First, create an ECR repository if not already created.  
   - Log in to your AWS ECR and push the images.

   <br>
   
   ```bash
   aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<your-region>.amazonaws.com
   docker build -t test-framework:latest .
   docker tag test-framework-controller:latest <account-id>.dkr.ecr.<your-region>.amazonaws.com/insider-automation:test-framework-controller
   docker push <account-id>.dkr.ecr.<your-region>.amazonaws.com/insider-automation:test-framework-controller

7. **Update YAML Files for ECR: Ensure that the Kubernetes YAML files (k8s/) reference the ECR image URLs**.

8. **Run Tests: Run the Python script for deployment and test execution**:
   ```bash
   python3 deploy_and_run_tests.py


### Insider Automation Test Framework

This framework uses a **Page Object Model (POM)** pattern to automate tests on the [Insider website](https://useinsider.com/). It is designed to execute structured and modular tests with reporting capabilities.

---

#### Folder Structure

- **tests/** - Contains test cases that validate key features:
  - **Main tests include:**
    - `validate_insider_home_page_opens` - Verifies the Insider home page.
    - `test_validate_careers_page_opens` - Checks the Careers page, Locations, Teams, and Life at Insider sections.
    - `test_validate_insider_qa_page_opens` - Verifies the Quality Assurance page.
    - `test_validate_qa_jobs` - Filters jobs by location and department, and verifies the job list.
    - `test_validate_careers_page_sections` - Checks specific sections on the Careers page.

- **actions/** - Defines action classes with methods for detailed test steps:
  - Each action file (e.g., `careers_actions.py`) encapsulates test actions for specific pages.

- **pages/** - Contains page classes that define UI elements and interactions:
  - Each page file (e.g., `careers_page.py`) includes locators and interaction methods for a page.

- **utils/** - Utility files and configuration:
  - **custom_webdriver_manager.py** - Manages WebDriver setup.
  - **common_utils.py** - Common utilities like scrolling, dropdown handling, waits, and JS click functions.
  - **base_test.py** - Base test class inherited by all test cases.

---

#### Configuration and Dependencies

- **conftest.py** - Configures Pytest, enabling parallel test execution.
- **constants.py** - Stores constants used across the tests.
- **pytest.ini** - Configures Pytest options and enables Allure reporting:
  ```ini
  addopts = --html=reports/report.html --self-contained-html --alluredir=reports
  ```
  - **Allure reporting** is enabled by default.
  
- **requirements.txt** - Lists dependencies required for the framework.  

<br>

#### Alternative Method to Run the Infrastructure

The framework is designed to run on Kubernetes; however, you can also spin up the infrastructure locally without Kubernetes using **Docker Compose**:

```bash
docker-compose up --build
```

This will start the necessary containers, enabling you to run the tests locally
