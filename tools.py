from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun,TavilySearchResults
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime
import textwrap 

#1. Web search tool
search = TavilySearchResults()
search_tool = Tool(
    name = "searchWeb",
    func= search.run,
    description="Search the web for information",
)

#2. Wikipedia tool
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=2,doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper = wiki_api_wrapper)

#3. tool to save data to a file 
#Data is going to be a pydantic model
def save_to_text(data: str, filename: str = "research_output.txt"):
    timestam = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    data = textwrap.fill(data)
    formatted_text = f"- - - - - Research Output - - - - - \nTimestamp: {timestam}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data Successfully saved to {filename}"

save_tool = Tool(
    name = "save_text_to_file",
    func = save_to_text,
    description= " Saves structured research data to a text file"
)





