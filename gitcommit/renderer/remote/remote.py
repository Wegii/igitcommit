import os
import logging
import gitlab

logger = logging.getLogger("gitlab_bridge")

# Infer that from repo
GITLAB_INSTANCE_ADDR = "https://gitlab.lrz.de"
REPOSITORY = ""

# TODO: look for access token, otherwise try public api
GITLAB_PRIVATE_TOKEN = os.environ["GITLAB_PRIVATE_TOKEN"]


class GitlabRenderer:
    def __init__(self, template, variables, config):
        self.template = template
        self.variables = variables
        self.config = config

        # self.connect()
        # self.project = self.find_project()

    def connect(self):
        logger.info(
            "Connecting to {} with {} as token".format(
                GITLAB_INSTANCE_ADDR, GITLAB_PRIVATE_TOKEN
            )
        )
        self.connection = gitlab.Gitlab(
            GITLAB_INSTANCE_ADDR, private_token=GITLAB_PRIVATE_TOKEN
        )
        self.connection.auth()
        logger.info("Connecting succesful")

    def find_project(self):
        """Returns the id of a given project."""
        # TODO (till): find project dynamically
        return self.connection.projects.get("ge39rec/gitcommit")

    def find_mr(self):
        # TODO (till): use current branch for detecting merge request
        return self.project.mergerequests.list(
            source_branch="1-include-information-via-issue-trackers-to-commit-messages"
        )

    def parse_checklist(checklist):
        """Parses a checklist and returns the last unchecked item and a line number.

        If there's no (unchecked) checklist item, return None and -1
        """
        for i, line in enumerate(checklist.splitlines()):
            if line.startswith("* [ ]"):
                return line[5:].strip(), i

        return None, -1

    def crawl_mergerequest(self):
        mrs = find_mr()
        # If there's no merge request to a branch, we can't infer information from the remote
        if len(mrs) == 0:
            return
        # For now only work with the first mr in the result
        else:
            mr = mr[0]

    def render_template(self):
        pass
