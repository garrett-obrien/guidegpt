import fixieai

BASE_PROMPT = """
I am an agent that helps users research backcountry ski trips in the Pacific Northwest US.

I have general knowledge and the ability to search local forums for more information about
specific ski objectives and regions. A user may ask me follow up questions, but I always
do Ask Func[fixie_query_corpus] with a complete question, without any
reference.
"""

FEW_SHOTS = """
Q: Sample query to this agent
A: Sample response

Q: Another sample query
Ask Func[example]: input
Func[example] says: output
A: The other response is output
"""
agent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS)


@agent.register_func
def example(query: fixieai.Message) -> str:
    assert query.text == "input"
    return "output"
