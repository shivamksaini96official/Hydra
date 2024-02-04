import hydra
from omegaconf import DictConfig
from hydra.utils import instantiate
import torch

class MyClass:
  def __init__(self,name:str)->None:
    self.name = name

  def say_hello(self)->None:
    print(f"Hello, {self.name}")

@hydra.main(config_path=".",config_name="config")
def main(config: DictConfig)->None:
  myclass = MyClass(name='John')
  myclass.say_hello()
  
  my_class_hydra = instantiate(config.myclass)
  my_class_hydra.say_hello()

  # -- let's instantiate torch optimizer using hydra
  parameters = torch.nn.Parameter(torch.randn(10,10))
  paratial_optimizer = instantiate(config.optimizer)
  optimizer = paratial_optimizer([parameters])
  print(optimizer)


if __name__ == "__main__":
  main()
