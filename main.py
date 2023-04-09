import fixieai

BASE_PROMPT = """
I am an agent that helps users research backcountry ski trips in the Pacific Northwest US.

I have general knowledge from my training and the ability to search local forums for more information 
about specific ski objectives and regions. A user may ask me follow up questions, but I always
do Ask Func[fixie_query_corpus] with a complete question, without any
reference.

When I provide answers, I share a general overview of possible ski touring routes near the area,
as well as URLs where a user can access additional information.
"""

FEW_SHOTS = """
Q: What do you know about touring Ruby Mountain?
A: Ruby Mountain is a popular ski tour that begins near the gate of Highway 20 in the North
Cascades National Park.

Q: Another sample query
Ask Func[fixie_query_corpus]: input
Func[fixie_query_corpus] says: output
A: The other response is output
"""

# List of PNW forums/blogs/etc. to use in the doc corpus
URLS = [
    "https://turns-all-year.com/trip-reports/*",
    "https://climberkyle.com/category/trip-reports/*",
    "https://www.whereiskylemiller.com/trip-report/trip-reports/*",
]
# Build the document corpus
DOCS = [fixieai.DocumentCorpus(urls=URLS)]

# Assemble the agent
agent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS, DOCS)