import pulumi_kubernetes as k8s
import pulumi

config = pulumi.Config()

provider = k8s.Provider("k8s", render_yaml_to_directory="yaml")

k8s.core.v1.Pod(
    config.require("pod-name"),
    metadata=k8s.meta.v1.ObjectMetaArgs(name="nginx", namespace="default"),
    spec=k8s.core.v1.PodSpecArgs(
        containers=[
            k8s.core.v1.ContainerArgs(
                name=config.require("container-name"),
                image=config.require("image-name"),
                ports=[k8s.core.v1.ContainerPortArgs(container_port=80)],
            )
        ]
    ),
    opts=pulumi.ResourceOptions(provider=provider),
)
