from crewai import Task
from agents.agents import (
    data_analyst_agent,
    trading_strategy_agent,
    execution_agent,
    risk_management_agent,
)



# Market Data Analysis
data_analysis_task = Task(
    name="Market Data Analysis",
    description=(
        "Continuously monitor and analyze market data for the selected stock ({stock_selection}). "
        "Use statistical modeling and machine learning to identify trends and predict market movements."
    ),
    expected_output=(
        "Insights and alerts about significant market opportunities or threats for {stock_selection}."
    ),
    agent=data_analyst_agent,
)

# Strategy Development
strategy_development_task = Task(
    name="Strategy Development",
    description=(
        "Develop and refine trading strategies based on the insights from the Data Analyst and "
        "user-defined risk tolerance ({risk_tolerance}). "
        "Consider trading preferences ({trading_strategy_preference})."
    ),
    expected_output=(
        "A set of potential trading strategies for {stock_selection} "
        "that align with the user's risk tolerance."
    ),
    agent=trading_strategy_agent,
)

# Execution Plan
execution_planning_task = Task(
    name="Execution Planning",
    description=(
        "Analyze approved trading strategies to determine the best execution methods for {stock_selection}, "
        "considering current market conditions and optimal pricing."
    ),
    expected_output=(
        "Detailed execution plans suggesting how and when to execute trades for {stock_selection}."
    ),
    agent=execution_agent,
)

# Risk Analysis
risk_assessment_task = Task(
    name="Risk Assessment",
    description=(
        "Evaluate the risks associated with the proposed trading strategies and execution plans for {stock_selection}. "
        "Provide a detailed analysis of potential risks and suggest mitigation strategies."
    ),
    expected_output=(
        "A comprehensive risk analysis report detailing potential risks and mitigation recommendations "
        "for {stock_selection}."
    ),
    agent=risk_management_agent,
)
