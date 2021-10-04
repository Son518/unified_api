import json
from unified.core.actions import Actions
from project_management.pivotal_tracker import util
from project_management.pivotal_tracker.entities.pivotal_tracker_project import PivotaltrackerProject
from project_management.pivotal_tracker.entities.pivotal_tracker_story import PivotaltrackerStory

class PivotaltrackerActions:

    def create_project(self, context, payload):
        '''Creates a project.'''

        project_entity = PivotaltrackerProject(**payload)
        endpoint = 'projects'
        data = {
                "name": project_entity.project_name
            }
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)

    def create_story(self, context, payload):
        '''Creates a story.'''

        story_entity = PivotaltrackerStory(**payload)
        endpoint = f"projects/{story_entity.project_id}/stories"
        data = {
                "name": story_entity.name,
                "description": story_entity.description
            }
        if story_entity.deadline:
            data["story_type"]="release"
            data["deadline"]=story_entity.deadline
        if story_entity.requested_by:
            data["requested_by_id"]=int(story_entity.requested_by)
        if story_entity.labels:
            data["labels"]=[story_entity.labels]
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)