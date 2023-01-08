from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None




from enum import Enum

# class syntax
class Position(Enum):
    manager = 'MANAGER'
    hr = 'HR'
    intern = 'INTERN'
    ceo = 'CEO'

class Vulnerability(Enum):
    sev1 = 1
    sev2 = 2
    sev3 = 3
    sev4 = 4

import logging



class Intern(AbstractHandler):
    max_sev_handling_capacity = Vulnerability.sev4.value
    def handle(self, request) -> str:
        if self.max_sev_handling_capacity <= request:
            print(f'{__class__.__name__} Handling the Issue')
            return f"{__class__.__name__} Can handle this on Call."
        else:
            print(f'{__class__.__name__} Cannot resolve, passing it to super')
            return super().handle(request)


class Manager(AbstractHandler):
    max_sev_handling_capacity = Vulnerability.sev2.value
    def handle(self, request) -> str:
        if self.max_sev_handling_capacity <= request:
            print(f'{__class__.__name__} Handling the Issue')
            return f"{__class__.__name__} Can handle this on Call."
        else:
            print(f'{__class__.__name__} Cannot resolve, passing it to super')
            return super().handle(request)


class TechLead(AbstractHandler):
    max_sev_handling_capacity = Vulnerability.sev1.value
    def handle(self, request) -> str:
        if self.max_sev_handling_capacity <= request:
            print(f'{__class__.__name__} Handling the Issue')
            return f"{__class__.__name__} Can handle this on Call."
        else:
            print(f'{__class__.__name__} Cannot resolve, passing it to super')
            return super().handle(request)




def client_code(handler: Handler):
    requests = [1,2,3,4,5]
    for request in requests:
        print(f'Giving request to handlers -> {request}')
        if not handler.handle(request=request):
            print(f'Request {request} is not picked up by any of the team members')
        print('\n')


if __name__=='__main__':
    intern = Intern()
    manager = Manager()
    techlead = TechLead()
    #setting cor
    intern.set_next(manager).set_next(techlead)
    client_code(intern)