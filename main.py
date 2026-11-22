from src.tools.tools import search_tool, scrape_url_tool
from rich import print


print(scrape_url_tool.invoke("https://en.wikipedia.org/wiki/Wiki"))
