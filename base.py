import asyncio
import aiohttp
import requests


class HackerNews:
    """
    This is the base class
    """
    def __init__(self):
        """
        1. Initial URLs are defined
        2. API is called which fetches top stories
        3. Function is called which fetches details of each story
        """
        self.top_story_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        self.item_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json'
        self.top_stories = requests.get(self.top_story_url).json()
        self.data = []
        asyncio.run(self.get_item_details())

    async def get_item_details(self):
        """
        This function is used to call the item detail APIs asynchronously and sets self.data
        The number of API's depends in the length of self.top_stories
        :return: true
        """
        async with aiohttp.ClientSession() as session:
            print("**************** Calling item APIs asynchronously ****************")
            tasks = [session.get(self.item_url.format(item)) for item in self.top_stories]
            responses = await asyncio.gather(*tasks)
            for response in responses:
                item_response = await response.json()
                try:
                    item_data = (item_response['id'], item_response['type'], item_response['by'], item_response['url'],
                                 item_response['title'])
                    self.data.append(item_data)
                except KeyError:
                    pass
            return True
