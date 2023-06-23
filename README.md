# Bakbak
A flask based microservice that allows creating generative responses over a set of FAQs for an input. It doesnt maintain the session and uses a 1:1 QA response mechanism for now. 

### Dimensions
Key dimensions in building such a system using LLMs:
1. ```Loading the data for grounding```: Data gets stored in vector stores as embeddings allowing for similarity search(cosine similarity for now)
2. ``Generating prompt``: Using the ChatML from OpenAI to generate the prompt which relies on the retrieved data alone and doesnt hallucinate.
3. ``Using LLMs for forming sentences``: Sending the prompt to generate summarized output


### Things to explore
While the happy path works, the side effects for the system are huge:
1. ``MLOps aspect``: Daily rebuilding of data index can degrade the search quality by quiet a bit.Thing can impact response from LLMs and need to be tackled with some metric. Need to explore what that metric looks like.
2. ``Scale``: Scale of the data set consumed for vector search as well as number of tokens on the side of LLM dispatch need to be considered.
   
