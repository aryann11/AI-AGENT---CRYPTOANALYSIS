from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="mixtral-8x7b-32768")
)

agent.print_response("Tell me about today's  climate ")