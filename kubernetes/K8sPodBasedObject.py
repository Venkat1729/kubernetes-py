from kubernetes.K8sObject import K8sObject
from kubernetes.K8sContainer import K8sContainer
from kubernetes.K8sConfig import K8sConfig


class K8sPodBasedObject(K8sObject):
    def __init__(self, name, obj_type, config=None):
        K8sObject.__init__(self, config=config, obj_type=obj_type, name=name)

    def add_container(self, container):
        assert isinstance(container, K8sContainer)
        self.model.add_container(container=container.get_model())
        return self

    def add_host_volume(self, name, path):
        self.model.add_host_volume(name=name, path=path)
        return self

    def add_image_pull_secrets(self, name):
        self.model.add_image_pull_secrets(name=name)
        return self

    def get_pod_containers(self):
        return self.get_pod_containers()

    def set_active_deadline(self, seconds):
        self.model.set_active_deadline(seconds=seconds)
        return self

    def set_dns_policy(self, policy):
        self.model.set_dns_policy(policy=policy)
        return self

    def set_image(self, name, image):
        self.model.set_pod_image(name=name, image=image)
        return self

    def set_pod_generate_name(self, mode, name=None):
        self.model.set_pod_generate_name(mode=mode, name=name)
        return self

    def set_restart_policy(self, policy):
        self.model.set_restart_policy(policy=policy)
        return self

    def set_service_account(self, name):
        self.model.set_service_account(name=name)
        return self

    def set_termination_grace_period(self, seconds):
        self.model.set_termination_grace_period(seconds=seconds)
        return self
