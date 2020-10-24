import configparser
import os
import pathlib

from Logger import Logger
from XException import XException

class ConfigLoader:
	logger = Logger()

	CONFIG_DIR = 'config'
	CONFIG_FILE = 'config.ini'

	_script_path = pathlib.Path(__file__).parent.absolute()

	_config_path = os.path.join(_script_path, CONFIG_DIR, CONFIG_FILE)

	_config = configparser.ConfigParser()


	@staticmethod
	def get(property_key: str, config_section='DEFAULT'):
		# if config not loaded
		if len(ConfigLoader._config.sections()) == 0 or len(ConfigLoader._config['DEFAULT']) == 0:
			ConfigLoader._load()

		property_value = ConfigLoader._config.get(config_section, property_key)

		ConfigLoader.logger.debug(
			"Loading property: {0}={1}",
			property_key,
			property_value)

		return property_value


	@staticmethod
	def _load():
		ConfigLoader.logger.debug("Loading config file.")
		ConfigLoader._load_config_file(ConfigLoader._config_path)

	@staticmethod
	def _load_config_file(path: str):
		ConfigLoader._read_existing_config_file(path)

		# config file already exists
		if len(ConfigLoader._config.sections()) > 1 or len(ConfigLoader._config['DEFAULT']) > 0:
			# see if a different property file is specified
			default_config = ConfigLoader._config['DEFAULT']

			config_file_to_load_dir = default_config['config.file.to.load.dir']
			config_file_to_load = default_config['config.file.to.load']

			full_path = os.path.join(ConfigLoader._script_path, config_file_to_load_dir, config_file_to_load)

			# different config file specified to load
			if full_path not in ConfigLoader._config_path:
				ConfigLoader.logger.debug('New file specified: {0}', full_path)
				ConfigLoader._load_config_file(full_path)

		else:
			ConfigLoader._generate_new_config_file(path)
			ConfigLoader._read_existing_config_file(path)


	@staticmethod
	def _read_existing_config_file(path: str):
		"""
		Try to read the config file at the specified path
		.. if we fail to read it
		:param path:
		:return:
		"""
		ConfigLoader._config = configparser.ConfigParser()

		ConfigLoader.logger.info("Reading from file: {0}", path)

		try:
			ConfigLoader._config.read(path)

		except XException as ex:
			ConfigLoader.logger.debug(
				"No config file ({0}) was found. ({1})",
				path,
				ex.print_message())


	@staticmethod
	def _generate_new_config_file(path: str):
		ConfigLoader._config['DEFAULT'] = {
			'config.file.to.load.dir': 'config',
			'config.file.to.load': 'config.ini',
			'key.image.base.path': 'onscreenkeyboard',
			'osk.file.name': 'onscreenkeyboard.png'
		}

		script_path = pathlib.Path(__file__).parent.absolute()

		full_path = os.path.join(script_path, path)

		with open(full_path, 'w') as configfile:
			ConfigLoader._config.write(configfile)


config = ConfigLoader()

print(config.get('config.file.to.load'))
print(config.get('osk.file.name'))