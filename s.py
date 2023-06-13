from pprint import pprint
import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests

cookies = {
    'signup_info': 'aHR0cHM6Ly93d3cuZ29vZ2xlLmNvLnVrLyAtLS0tIGh0dHBzOi8vd3d3LnRyYWRld2hlZWwuY29tIC0tLS0gMjAyMy0wNi0xMyAwMjoyMzo0OQ^%^3D^%^3D',
    'u_iden': '0398626001686605029',
    '_ga_X5KFV0DBD5': 'GS1.1.1686685619.2.0.1686685619.0.0.0',
    '_ga': 'GA1.2.1684477698.1686605037',
    '_gcl_au': '1.1.1923846938.1686605037',
    '_gid': 'GA1.2.37679994.1686605038',
    'popup': '3',
    'XSRF-TOKEN': 'eyJpdiI6IlVaOUR0RFdFaVZtZlJhN2xsdmNHbnc9PSIsInZhbHVlIjoiTzNoK1MzTGVvNUF6REZWUjB4QVd0NkdCd2NkOEVxSk5LTElTWm9HWlJJV0FhZytMQUxSQzIyanU4RERwTFFwNSIsIm1hYyI6ImE5ZDI4ODhmYWM3NzAyYmY0OGQ1M2VlNjQ1ODE5ZDZhZjE0MjYzN2IyNTBlNDZhNWQ0YzZjMWI3NzIzMjQ4OTUifQ^%^3D^%^3D',
    'tradewheel_session': 'eyJpdiI6InBncUZxcWlXVW9HYlFDTExmbDNiR0E9PSIsInZhbHVlIjoidStyWEhFdEl3SlMwT0tKd0hjYkVBcFZYV3FxeXdyZU1VTnJUcjZONisydlwvUVJiXC9ZT09kYTNGeTJDWHZnUWRlIiwibWFjIjoiMTVlMzYzZjRiMDdmMjNhNThjYmU0NWZmYjVlNjA0Nzk3YzY1MTFiNDllYmE3MDE5MzUzMjQ2MTljYjQ1MmI1ZCJ9',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'signup_info=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvLnVrLyAtLS0tIGh0dHBzOi8vd3d3LnRyYWRld2hlZWwuY29tIC0tLS0gMjAyMy0wNi0xMyAwMjoyMzo0OQ^%^3D^%^3D; u_iden=0398626001686605029; _ga_X5KFV0DBD5=GS1.1.1686685619.2.0.1686685619.0.0.0; _ga=GA1.2.1684477698.1686605037; _gcl_au=1.1.1923846938.1686605037; _gid=GA1.2.37679994.1686605038; popup=3; XSRF-TOKEN=eyJpdiI6IlVaOUR0RFdFaVZtZlJhN2xsdmNHbnc9PSIsInZhbHVlIjoiTzNoK1MzTGVvNUF6REZWUjB4QVd0NkdCd2NkOEVxSk5LTElTWm9HWlJJV0FhZytMQUxSQzIyanU4RERwTFFwNSIsIm1hYyI6ImE5ZDI4ODhmYWM3NzAyYmY0OGQ1M2VlNjQ1ODE5ZDZhZjE0MjYzN2IyNTBlNDZhNWQ0YzZjMWI3NzIzMjQ4OTUifQ^%^3D^%^3D; tradewheel_session=eyJpdiI6InBncUZxcWlXVW9HYlFDTExmbDNiR0E9PSIsInZhbHVlIjoidStyWEhFdEl3SlMwT0tKd0hjYkVBcFZYV3FxeXdyZU1VTnJUcjZONisydlwvUVJiXC9ZT09kYTNGeTJDWHZnUWRlIiwibWFjIjoiMTVlMzYzZjRiMDdmMjNhNThjYmU0NWZmYjVlNjA0Nzk3YzY1MTFiNDllYmE3MDE5MzUzMjQ2MTljYjQ1MmI1ZCJ9',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get(
    'https://www.tradewheel.com/buyers/looking-for-ball-screw-sfu1610/682812/',
    cookies=cookies,
    headers=headers,
)

soup = BeautifulSoup(response.content, 'html.parser')
