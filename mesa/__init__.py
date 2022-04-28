"""
Mesa Agent-Based Modeling Framework

Core Objects: Model, and Agent.

"""
import datetime

from mesa.model import Model
from mesa.agent import Agent

import mesa.time as time
import mesa.space as space
import mesa.flat.visualization as visualization
from mesa.datacollection import DataCollector

__all__ = ["Model", "Agent", "time", "space", "visualization", "DataCollector"]

__title__ = "mesa"
__version__ = "0.9.0"
__license__ = "Apache 2.0"
__copyright__ = f"Copyright {datetime.date.today().year} Project Mesa Team"
