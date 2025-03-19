#SERPER_API_KEY=""

from crewai_tools import SerperDevTool
import os
serper_api_key = os.getenv("SERPER_API_KEY")
# Setup the tool for internet searching capabilities
google_search_tool = SerperDevTool(api_key=serper_api_key)



