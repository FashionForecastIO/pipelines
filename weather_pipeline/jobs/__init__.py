"""
This module is used to import all the jobs in the pipeline.
"""

from . import request_weather_api

all_jobs = [request_weather_api.pipeline]

__all__ = ["all_jobs"]
