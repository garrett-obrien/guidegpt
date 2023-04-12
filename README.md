# GuideGPT
A tool for searching mountain trip reports using LLMs, deployed using fixieai.

Consults local PNW forums, blogs, and general knowledge about backcountry skiing. Sometimes hallucinates, use at your own risk.

## Getting started

To get started:

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