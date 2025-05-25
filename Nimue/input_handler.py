import discord
import datetime
from Managers.data_manager import DataManager
import logging

logger = logging.getLogger(" NIMUE ")

class input_handler:

  def __init__(self, client:discord.Client):
    self.data_manager = DataManager()
    self.client = client

  async def get_response(self, message_content,display_name,  display_avatar, server_name):
    logger.info(f'Server: {server_name}')
    now = datetime.datetime.now()
    logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))
    logger.info(f'With presence in {len(self.client.guilds)} servers')
    game = discord.Game(f"Playing Urban Shadow 2E in {len(self.client.guilds)} servers!")
    await self.client.change_presence(status=discord.Status.online, activity=game)

    response = self.get_message_from_command(message_content, display_name, display_avatar)
    if (response == None):
      response = discord.Embed(
          title=self.data_manager.localizer.get_utils_with_key(
            "ups_title"),
          color=0xFF5733, description=self.data_manager.localizer.get_utils_with_key(
            "ups"))
    return response
  
  def get_message_from_command(self, message_content, user_display_name, user_avatar):
    has_command = self.data_manager.message_contains_command(message_content)

    if (has_command):
      self.data_manager.current_command.user_display_name = user_display_name
      self.data_manager.current_command.avatar = user_avatar
      
      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_help_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_help_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_info_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_info.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_basic_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_basic_move.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_circles_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_circles_move.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_debt_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_debt_move.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_1_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_1.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_2_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_2.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_3_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_3.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_faction_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_faction_move.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_playbook_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_playbook.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_info_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_info_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_info.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_basic_move_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_basic_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_basic_move.name)
        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response
            
      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_circles_move_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_circles_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_circles_move.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response

      

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_debt_move_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_debt_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_debt_move.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_city_move_status_1_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_1_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_1.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_city_move_status_2_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_2_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_2.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_city_move_status_3_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_3_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_city_move_status_3.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_faction_move_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_faction_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_faction_move.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_playbook_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_playbook_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_playbook.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_playbook.name):
          response = self.data_manager.playbooks_manager.do_playbook(self.data_manager)
          return response

      if(self.data_manager.current_command.type == self.data_manager.COMMAND_TYPE.command_info.name):
        response = self.data_manager.parse_info()
        return response
      else: 
        response = self.data_manager.moves_manager.do_move(self.data_manager)
        return response

      embed = discord.Embed(title=self.data_manager.current_command.languages[self.data_manager.localizer.lang.name], color=0xFF5733)
      embed.add_field(name='**—————————**',
                      value=self.data_manager.localizer.get_utils_with_key(
                        "missing_command"))
      return embed