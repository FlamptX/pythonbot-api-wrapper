# Imports
import ast
import requests
import asyncio
import Message

class Client:
    def event(self, coro):
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError('event registered must be a coroutine function')

        setattr(self, coro.__name__, coro)
        # print('%s has successfully been registered as an event', coro.__name__)
        return coro

    async def receive(self, content):
        message = Message(content)

        try:
            await self.on_message(message)
        except AttributeError:
            pass

    def run(self, rate=0.5):

        async def runner():
            r = ast.literal_eval(requests.get("http://localhost:5000/api/messages").text)
            previous = r[len(r) - 1]
            while True:
                r = ast.literal_eval(requests.get("http://localhost:5000/api/messages").text)
                content = r[len(r) - 1]
                if content != previous:
                    await self.receive(content)
                previous = content
                await asyncio.sleep(rate)
        asyncio.run(runner())
