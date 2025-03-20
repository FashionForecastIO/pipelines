from dagster import Definitions

from weather_pipeline.jobs import all_jobs

defs = Definitions(
    jobs=all_jobs,
)
