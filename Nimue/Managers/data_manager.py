import discord
import re

from Managers.commands_manager import Commands_Manager
from Managers.moves_manager import Moves_Manager
from Managers.playbooks_manager import Playbooks_Manager
from Localization.localizer import Localizer
from enum import Enum
from Data.command import Command


class DataManager:
  COMMAND_TYPE = Enum(
    'COMMAND_TYPE',
    'command_help_list command_info_list command_info command_basic_move_list command_basic_move command_circles_move_list command_circles_move command_debt_move_list command_debt_move command_city_move_status_1_list command_city_move_status_1 command_city_move_status_2_list command_city_move_status_2 command_city_move_status_3_list command_city_move_status_3 command_faction_move_list command_faction_move command_playbook_list command_playbook command_playbook_move command_basic_move_extended'
  )

  def __init__(self):
    self.commands_manager = Commands_Manager()
    self.localizer = Localizer()
    self.moves_manager = Moves_Manager()
    self.playbooks_manager = Playbooks_Manager()
    self.current_command = None

  def message_contains_command(self, message_content):
    messageText = message_content
    messageText = messageText.lower()
    messageText = messageText.replace(" ", "")
    messageText = re.sub('[$]', '', messageText)
    messageText = re.sub(r'<.+?>', '', messageText)
    list_mod = re.findall(r'[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?',
                          messageText)
    messageText = re.sub(r'[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?', '',
                         messageText)

    if not list_mod:
      mod = 0
    else:
      mod = int(list_mod[0])

    self.current_command = self.__get_command_in_message__(messageText)

    if (self.current_command != None):
      self.localizer.lang = self.current_command.active_language
      self.current_command.modifier = mod
      return True

    return False

  def __get_command_in_message__(self, text_command):
    command_in_message = None

    for command in self.commands_manager.list:
      if (command.languages[self.localizer.LANGUAGES.english.name] ==
          text_command):
        command_in_message = Command(command.id, command.languages['english'],
                                     command.languages['español'],
                                     command.type, command.status)
        command_in_message.active_language = self.localizer.LANGUAGES.english
        return command_in_message
      if (command.languages[self.localizer.LANGUAGES.español.name] ==
          text_command):
        command_in_message = Command(command.id, command.languages['english'],
                                     command.languages['español'],
                                     command.type, command.status)
        command_in_message.active_language = self.localizer.LANGUAGES.español
        return command_in_message
    return command_in_message

  def parse_info(self):
    command_id =self.current_command.id.replace('command','')
    title = self.localizer.get_utils_with_key(
      'asking_for') + self.localizer.get_info("name" + command_id)
    if (self.localizer.get_info("name" + command_id) == '-'):
      title = self.localizer.get_utils_with_key("empty_title")

    blurb = self.localizer.get_info("blurb" + command_id)
    if (blurb == '-'):
     blurb = self.localizer.get_utils_with_key("empty_blurb") 

    embed = discord.Embed(title=title, colour=5450873, description=blurb)

    embed.set_author(name=self.current_command.user_display_name)
    embed.set_thumbnail(url=self.current_command.avatar)

    return embed
