import os
from abc import ABC, abstractmethod
import langchain_core, langchain
from langchain_community.chat_models import Chatollama
from dotenv import load_dotenv

load_dotenv()

model = os.getenv("MODEL")
class BaseAgent(ABC):
    def __init__(self, name):
      self.name = name
      self.llm = Chatollama(model = model)


    @abstractmethod
    def run(self, state:dict)  -> dict:
       """process input state & return an updated state"""
       pass