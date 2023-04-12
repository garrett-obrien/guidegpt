# GuideGPT

An agent for searching mountain trip reports using LLMs, deployed using fixieai.

Consults local PNW forums, blogs, and general knowledge about backcountry skiing. Sometimes hallucinates, use at your own risk.

## Using the agent

To use the currently deployed GuideGPT agent:

1. Create an account at app.fixie.com
2. Start a new session with the agent at https://app.fixie.ai/agents/g.thomasobrien/guidegpt

## Creating your own GuideGPT agent

To deploy a copy of the agent to your own Fixie account:

1. Clone the repo
2. `cd` into the directory
3. Verify access to fixie.ai using Google or your GitHub email
4. Install the Fixie CLI using `pip install fixieai`
5. Run `fixie auth` to ensure authentication
6. Update the `agent.yaml` file to reflect your copy of the agent
7. Run the agent with `fixie agent deploy`

Fixie docs: https://docs.fixie.ai/

## To-do

1. Improve prompt to stop hallucinating URLs
2. Add TAY trip reports once XML site crawling is supported in `fixieai.DocumentCorpus`
3. Add additional PNW ski blogs/forums to document corpus
4. Test if more powerful models improve search results (once parsing issues are fixed)