from agents.agents import (
    data_analyst_agent, trading_strategy_agent,
    execution_agent, risk_management_agent
)
from tasks.tasks import (
    data_analysis_task, strategy_development_task,
    execution_planning_task, risk_assessment_task
)
from crewai import Crew, Process
import os


from crewai import LLM

llm = LLM(
    model="ollama/mistral",
    base_url="http://localhost:11434",
    api_key="ollama-placeholder"  # Still required by CrewAI but not used by Ollama
)

# Crew setup
financial_trading_crew = Crew(
    agents=[
        data_analyst_agent,
        trading_strategy_agent,
        execution_agent,
        risk_management_agent
    ],
    tasks=[
        data_analysis_task,
        strategy_development_task,
        execution_planning_task,
        risk_assessment_task
    ],
    manager_llm=llm,
    process=Process.hierarchical,
    verbose=True
)
# Run the pipeline
if __name__ == "__main__":
    result = financial_trading_crew.kickoff(inputs={
        'stock_selection': 'AAPL',
        'initial_capital': '100000',
        'risk_tolerance': 'Medium',
        'trading_strategy_preference': 'Day Trading',
    })

    print(result.raw)