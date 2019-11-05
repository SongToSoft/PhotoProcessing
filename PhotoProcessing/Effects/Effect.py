from abc import ABC, abstractmethod

class Effect(ABC):
    @abstractmethod
    def Execute(self, opennedImage):
        pass