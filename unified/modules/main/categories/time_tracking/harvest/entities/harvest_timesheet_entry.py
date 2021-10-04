from dataclasses import dataclass
from unified.modules.lib import util


@dataclass
class HarvestTimesheetEntry:
    notes: str = None
    hours: str = None
    project: str = None
    task: str = None
    spent_at: str = None

    def __post_init__(self):
        self.spent_at_epoch()

    def spent_at_epoch(self):
        if self.spent_at is None or "-" in self.spent_at:
            self.spent_at = self.spent_at
        else:
            format = "%Y-%m-%d"
            self.spent_at = util.epoch_to_format(
                format, self.spent_at)