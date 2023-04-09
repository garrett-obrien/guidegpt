import fixieai

BASE_PROMPT = """
I am an agent that helps users research backcountry ski trips in the Pacific Northwest US.

I have general knowledge from my training and the ability to search local forums for more information 
about specific ski objectives. A user may ask me follow up questions, but I always
do Ask Func[fixie_query_corpus] with a complete question, without any
reference.

When I provide answers, I share a general overview of possible ski touring routes near the area,
as well as URLs where a user can access additional information.
"""

FEW_SHOTS = """
Q: What do you know about touring Ruby Mountain?
A: Ruby Mountain is a moderate ski tour that begins near the gate of Highway 20 in the North
Cascades region. You can read more about Ruby Mountain ski touring here: https://climberkyle.com/2021/03/16/ruby-mountain-ski-tour/,
https://turns-all-year.com/trip-reports/march-31-ruby-mountain-north-cascades

Q: Where should I go touring near Snoqualmie Mountain?
Thought: I need to get search results for ski touring trip reports on Snoqualmie Mountain, Washington.
Ask Func[fixie_query_corpus]: What ski touring objectives feature Snoqualmie Mountain?
Func[fixie_query_corpus] says: Popular ski touring objectives on Snoqualmie Mountain include the
Slot Couloir, Snot Couloir, and Crooked Couloir.
A: Popular ski touring objectives on Snoqualmie Mountain include the Slot Couloir, Snot Couloir, 
and Crooked Couloir. You can read more about Snoqualmie Mountain ski touring here:
https://engineeredforadventure.com/slot-snot-couloirs/, 
Q: Which one is most popular?
Thought: I need to provide the most frequently mentioned route between the Slot Couloir, Snot Couloir, 
and Crooked Couloir.
Ask Func[fixie_query_corpus]: What is most frequently mentioned: the Slout Couloir, Snot Couloir, or 
Crooked Couloir?
Func[fixie_query_corpus] says: The Slot Couloir route is most commonly mentioned.
A: The Slot Couloir route is the most popular.
"""

# List of PNW forums/blogs/etc. to use in the doc corpus
URLS = [
    "https://turns-all-year.com/trip-reports/*",
    "https://climberkyle.com/category/trip-reports/*",
    "https://www.whereiskylemiller.com/trip-report/trip-reports/*",
    "https://engineeredforadventure.com/category/trip-report/*",
]
# Build the document corpus
CORPORA = [fixieai.DocumentCorpus(urls=URLS)]

# Assemble the agent, model specifics at 
# https://docs.fixie.ai/agents/#default-agent-model-and-model-parameters
agent = fixieai.CodeShotAgent(
    BASE_PROMPT, 
    FEW_SHOTS, 
    CORPORA, 
    conversational=True, 
    llm_settings=fixieai.LlmSettings(temperature=0, model="openai/gpt-3.5-turbo", maximum_tokens=1000)
)