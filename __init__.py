from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests
import xml.etree.cElementTree

__author__ = 'mason88'
LOGGER = getLogger(__name__)

class FederalClosingsSkill(MycroftSkill):
	def __init__(self):
		super(FederalClosingsSkill, self).__init__(name="FederalClosingsSkill")

	def initialize(self):
		intent = IntentBuilder("FederalClosingsIntent").require("FederalClosingsKeyword").build()
		self.register_intent(intent, self.handle_intent)

	def handle_intent(self, message):
		try:
			r = requests.get("https://www.opm.gov/xml/operatingstatus.xml")
			xml_root = xml.etree.cElementTree.fromstring(r.content)
			self.speak_dialog("federal.closings", data={'closings': xml_root.find('ShortStatusMessage').text})
		except:
			self.speak_dialog("not.found")

	def stop(self):
		pass


def create_skill():
	return FederalClosingsSkill()

