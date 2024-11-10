from kubernetes import client, config, utils
from kubernetes.client.rest import ApiException
import time
import subprocess
import os
import sys

config.load_kube_config()

v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

namespace = "default"
selenium_hub_deployment = "k8s/selenium-hub-deployment.yaml"
selenium_hub_service = "k8s/selenium-hub-service.yaml"
chrome_node_deployment = "k8s/chrome-node-deployment.yaml"
test_framework_controller = "k8s/test-framework-controller-deployment.yaml"
test_framework_controller_local = "k8s/test-framework-controller-local-deployment.yaml"
node_count = 1  
max_retries = 3

def apply_k8s_yaml(yaml_file):
    """Applies a Kubernetes YAML file."""
    try:
        utils.create_from_yaml(client.ApiClient(), yaml_file)
        print("Applied {} successfully.".format(yaml_file))
    except ApiException as e:
        print("Failed to apply {}: {}".format(yaml_file, e))

def scale_chrome_node_deployment(count):
    """Scales the Chrome Node deployment based on the node_count."""
    try:
        deployment = apps_v1.read_namespaced_deployment(name="chrome-node", namespace=namespace)
        
        deployment.spec.replicas = count
        apps_v1.patch_namespaced_deployment(name="chrome-node", namespace=namespace, body=deployment)
        
        print("Scaled Chrome Node deployment to {} replicas.".format(count))
    except ApiException as e:
        print("Error scaling Chrome Node deployment: {}".format(e))

def deploy_resources(test_framework_yaml):
    """Deploy necessary Kubernetes resources."""
    print("Deploying Selenium Hub deployment...")
    apply_k8s_yaml(selenium_hub_deployment)

    print("Deploying Selenium Hub service...")
    apply_k8s_yaml(selenium_hub_service)

    print("Deploying Chrome Node deployment...")
    apply_k8s_yaml(chrome_node_deployment)
    
    print("Deploying Test Framework Controller...")
    apply_k8s_yaml(test_framework_yaml)
    
    print("Scaling Chrome Node Pods...")
    scale_chrome_node_deployment(node_count)

def is_pod_ready(label_selector):
    """Check if a pod with a specific label is ready."""
    try:
        pods = v1.list_namespaced_pod(namespace, label_selector=label_selector)
        for pod in pods.items:
            if all(cond.status == 'True' for cond in pod.status.conditions if cond.type == 'Ready'):
                return True
    except ApiException as e:
        print("Error while checking pod readiness: {}".format(e))
    return False

def wait_for_pod_ready(label_selector, retries=5, delay=10):
    """Wait for a pod to be ready with retries."""
    for _ in range(retries):
        if is_pod_ready(label_selector):
            print("Pod is ready.")
            return True
        print("Waiting for pod to be ready...")
        time.sleep(delay)
    print("Pod is not ready after retries.")
    return False

def run_tests_in_pod():
    """Executes Selenium tests in the Test Framework Controller Pod."""
    pod_name = None
    try:
        pods = v1.list_namespaced_pod(namespace, label_selector="app=test-framework-controller")
        pod_name = pods.items[0].metadata.name
        print("Running tests in pod {}".format(pod_name))
        
        command = [
            "kubectl", "exec", pod_name, "-n", namespace, "--",
            "sh", "-c", "pytest --alluredir=reports -v && sleep infinity"
        ]
        subprocess.run(command, check=True)

    except (ApiException, subprocess.CalledProcessError) as e:
        print("Failed to run tests in pod {}: {}".format(pod_name, e))

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "local":
        deploy_resources(test_framework_controller_local)
    else:
        deploy_resources(test_framework_controller)
    
    if not wait_for_pod_ready("app=selenium-hub"):
        print("Selenium Hub is not ready. Exiting.")
        return
    
    if not wait_for_pod_ready("app=chrome-node"):
        print("Chrome Node is not ready. Exiting.")
        return
    
    run_tests_in_pod()

if __name__ == "__main__":
    main()
