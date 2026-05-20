from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ResumeTailor():
    """Cold Email Campaign Writer Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def audience_profiler(self) -> Agent:
        return Agent(
            config=self.agents_config['audience_profiler'],
            verbose=True
        )

    @agent
    def hook_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['hook_writer'],
            verbose=True
        )

    @agent
    def sequence_assembler(self) -> Agent:
        return Agent(
            config=self.agents_config['sequence_assembler'],
            verbose=True
        )

    @task
    def profile_audience_task(self) -> Task:
        return Task(
            config=self.tasks_config['profile_audience_task'],
        )

    @task
    def write_hooks_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_hooks_task'],
        )

    @task
    def assemble_sequence_task(self) -> Task:
        return Task(
            config=self.tasks_config['assemble_sequence_task'],
            output_file='email_sequence.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )