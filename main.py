from agents.agents import data_analyst_agent, trading_strategy_agent, execution_agent, risk_management_agent
from tasks.tasks import data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task
from utils.keys import get_openai_api_key, get_serper_api_key
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

import os
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ["OPENAI_API_KEY"] = get_openai_api_key()
os.environ["SERPER_API_KEY"] = get_serper_api_key()

financial_trading_crew = Crew(
    agents=[data_analyst_agent, trading_strategy_agent, execution_agent, risk_management_agent],
    tasks=[data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task],
    manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
    process=Process.hierarchical,
    verbose=True
)

if __name__ == "__main__":
    result = financial_trading_crew.kickoff(inputs={
        'stock_selection': 'AAPL',
        'initial_capital': '100000',
        'risk_tolerance': 'Medium',
        'trading_strategy_preference': 'Day Trading',
    })

    from IPython.display import Markdown
    print(Markdown(result))
