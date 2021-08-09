import hydra
from omegaconf import DictConfig
from hydra.utils import log


def f(x):
    return (x - 1) ** 2 + 5


@hydra.main(config_path="configs/", config_name="config.yaml")
def main(config: DictConfig) -> None:
    x = config.x
    y = f(x)
    log.info(f"x={x}, y={y}")
    return y


if __name__ == "__main__":
    main()
