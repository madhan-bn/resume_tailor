#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from resume_tailor.crew import ResumeTailor

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """

    inputs = {
        'product_description': 'AI-powered CRM automation tool for startups',
        'target_audience': 'Startup founders and small business owners'
    }

    try:
        ResumeTailor().crew().kickoff(inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """

    inputs = {
        'product_description': 'AI-powered CRM automation tool for startups',
        'target_audience': 'Startup founders and small business owners',
        'current_year': str(datetime.now().year)
    }

    try:
        ResumeTailor().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """

    try:
        ResumeTailor().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """

    inputs = {
        'product_description': 'AI-powered CRM automation tool for startups',
        'target_audience': 'Startup founders and small business owners',
        'current_year': str(datetime.now().year)
    }

    try:
        ResumeTailor().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")