from gitcommit.renderer import BaseRenderer
import logging

logger = logging.getLogger()

class GitHubRenderer(BaseRenderer):
    def __init__(self, config, variables):
        self.config = config
        self.variables = variables
