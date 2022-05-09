import aiohttp
import asyncio
import json

from config import LOAD_PATH, SAVE_PATH, TRESHOLD, SLEEP_TIME, HEADERS, START_FROM, END_AT, PRETTIFY_JSON, SORT_KEYS, FAILED_PATH

JSON_INDENT = 2 if PRETTIFY_JSON else None

failed_urls = []

def load_urls():    
    with open(LOAD_PATH) as file:
        return json.load(file)[START_FROM:END_AT]

async def get(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=HEADERS) as response:
                return {'url': url, 'html': await response.text()}
        except Exception as e:
            failed_urls.append(
                {'url': url, 'error': str(e)}
            )

def save_as_json(obj, path, **kwargs):
    with open(path, 'w') as file:
        json.dump(obj, file, sort_keys=SORT_KEYS, **kwargs)

async def main():
    urls = load_urls()
    
    index = 0
    LENGTH = len(urls)
    results = []

    while not index >= LENGTH:
        coroutines = [get(url) for url in urls[index:index + TRESHOLD]]
        results += list(await asyncio.gather(*coroutines))
        index += TRESHOLD
        
        print(f'Progress: {len(results)}/{LENGTH}')
        
        await asyncio.sleep(SLEEP_TIME)
    
    results = [result for result in results if result is not None]
    
    save_as_json(results, path=SAVE_PATH, indent=JSON_INDENT)

    if failed_urls:
        save_as_json(failed_urls, path=FAILED_PATH, indent=2)

    print(f'Process is done with {len(results)} successful and {len(failed_urls)} failed attempts.')

if __name__ == '__main__':
    asyncio.run(main())
