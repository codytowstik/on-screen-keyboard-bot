from maple.interfaces.MapleAction import MapleAction


class AutomationTick:
	def __init__(self, action: MapleAction, duration: float):
		self.action = action
		self.duration = duration

	def get_action(self):
		return self.action

	def get_duration(self):
		return self.duration
