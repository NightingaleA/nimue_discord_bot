from discord import app_commands
from typing import Union
from discord.app_commands import locale_str as _T
import discord

class Slash_Command_Manager:
  def __init__(self, tree, input):
    
    for command in input.data_manager.commands_manager.list:
      #Help
      if (command.type == input.data_manager.COMMAND_TYPE.command_help_list.name):
        @tree.command(name=_T( command.languages['english'] ))
        async def help_command(interaction: discord.Interaction):
          name = interaction.command.name 
          if(interaction.locale ==discord.Locale.spain_spanish):
            name = input.data_manager.__get_command_in_message__(name).languages['español']

          response = await input.get_response(name, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
          await interaction.response.send_message(embed=response)
    #Info
      if(command.type == input.data_manager.COMMAND_TYPE.command_info_list.name):
        list = input.data_manager.commands_manager.__get_list__( input.data_manager.COMMAND_TYPE.command_info.name)
        choice_list = []
        for info in list:
          choice_list.append(app_commands.Choice(name=info.languages['english'], value=info.languages['english']))

        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(info = choice_list )
        async def info_command(interaction: discord.Interaction, info: app_commands.Choice[str]):
          name = info.value
          if(interaction.locale ==discord.Locale.spain_spanish):
            input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
            name =input.data_manager.__get_command_in_message__(name).languages['español']
            
          response = await input.get_response(name, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
          await interaction.response.send_message(embed=response)    
          
    #Basic Moves
      if(command.type == input.data_manager.COMMAND_TYPE.command_basic_move_list.name):
        list = input.data_manager.commands_manager.__get_list__( input.data_manager.COMMAND_TYPE.command_basic_move.name)
        choice_list = []
        for move_command in list:
          choice_list.append(app_commands.Choice(name=move_command.languages['english'], value=move_command.languages['english']))

        modifier_list = []  
        modifier_list.append(app_commands.Choice(name="+4", value="+4"))
        modifier_list.append(app_commands.Choice(name="+3", value="+3"))
        modifier_list.append(app_commands.Choice(name="+2", value="+2"))
        modifier_list.append(app_commands.Choice(name="+1", value="+1"))
        modifier_list.append(app_commands.Choice(name="0", value="0"))
        modifier_list.append(app_commands.Choice(name="-1", value="-1"))
        modifier_list.append(app_commands.Choice(name="-2", value="-2"))
        modifier_list.append(app_commands.Choice(name="-3", value="-3"))
        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(basic = choice_list )
        @app_commands.choices(modifier = modifier_list)
        
        async def basic_move_command(interaction: discord.Interaction, basic: app_commands.Choice[str], modifier: app_commands.Choice[str]=None):
            command = basic.value
            mod = '+0'
            if (modifier != None):
              mod = modifier.value
          
            if(interaction.locale ==discord.Locale.spain_spanish):
              input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
              command =input.data_manager.__get_command_in_message__(command).languages['español']

            command = command + mod
            response = await input.get_response(command, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
            await interaction.response.send_message(embed=response)
#Circle Moves
      if(command.type == input.data_manager.COMMAND_TYPE.command_circles_move_list.name):
        list = input.data_manager.commands_manager.__get_list__( input.data_manager.COMMAND_TYPE.command_circles_move.name)
        choice_list = []
        for move_command in list:
          choice_list.append(app_commands.Choice(name=move_command.languages['english'], value=move_command.languages['english']))

        modifier_list = []  
        modifier_list.append(app_commands.Choice(name="+4", value="+4"))
        modifier_list.append(app_commands.Choice(name="+3", value="+3"))
        modifier_list.append(app_commands.Choice(name="+2", value="+2"))
        modifier_list.append(app_commands.Choice(name="+1", value="+1"))
        modifier_list.append(app_commands.Choice(name="0", value="0"))
        modifier_list.append(app_commands.Choice(name="-1", value="-1"))
        modifier_list.append(app_commands.Choice(name="-2", value="-2"))
        modifier_list.append(app_commands.Choice(name="-3", value="-3"))
        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(basic = choice_list )
        @app_commands.choices(modifier = modifier_list)
        
        async def circles_move_command(interaction: discord.Interaction, basic: app_commands.Choice[str], modifier: app_commands.Choice[str]=None):
            command = basic.value
            mod = '+0'
            if (modifier != None):
              mod = modifier.value
          
            if(interaction.locale ==discord.Locale.spain_spanish):
              input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
              command =input.data_manager.__get_command_in_message__(command).languages['español']

            command = command + mod
            response =await input.get_response(command, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
            await interaction.response.send_message(embed=response)
 #Debt Moves
      if(command.type == input.data_manager.COMMAND_TYPE.command_debt_move_list.name):
        list = input.data_manager.commands_manager.__get_list__( input.data_manager.COMMAND_TYPE.command_debt_move.name)
        choice_list = []
        for move_command in list:
          choice_list.append(app_commands.Choice(name=move_command.languages['english'], value=move_command.languages['english']))

        modifier_list = []  
        modifier_list.append(app_commands.Choice(name="+4", value="+4"))
        modifier_list.append(app_commands.Choice(name="+3", value="+3"))
        modifier_list.append(app_commands.Choice(name="+2", value="+2"))
        modifier_list.append(app_commands.Choice(name="+1", value="+1"))
        modifier_list.append(app_commands.Choice(name="0", value="0"))
        modifier_list.append(app_commands.Choice(name="-1", value="-1"))
        modifier_list.append(app_commands.Choice(name="-2", value="-2"))
        modifier_list.append(app_commands.Choice(name="-3", value="-3"))
        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(basic = choice_list )
        @app_commands.choices(modifier = modifier_list)
        
        async def debts_move_command(interaction: discord.Interaction, basic: app_commands.Choice[str], modifier: app_commands.Choice[str]=None):
            command = basic.value
            mod = '+0'
            if (modifier != None):
              mod = modifier.value
          
            if(interaction.locale ==discord.Locale.spain_spanish):
              input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
              command =input.data_manager.__get_command_in_message__(command).languages['español']

            command = command + mod
            response = await input.get_response(command, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
            await interaction.response.send_message(embed=response)
#City Status One Moves
      if(command.type == input.data_manager.COMMAND_TYPE.command_city_move_status_1_list.name):
        list = input.data_manager.commands_manager.__get_list__( input.data_manager.COMMAND_TYPE.command_city_move_status_1.name)
        choice_list = []
        for move_command in list:
          choice_list.append(app_commands.Choice(name=move_command.languages['english'], value=move_command.languages['english']))

        modifier_list = []  
        modifier_list.append(app_commands.Choice(name="+4", value="+4"))
        modifier_list.append(app_commands.Choice(name="+3", value="+3"))
        modifier_list.append(app_commands.Choice(name="+2", value="+2"))
        modifier_list.append(app_commands.Choice(name="+1", value="+1"))
        modifier_list.append(app_commands.Choice(name="0", value="0"))
        modifier_list.append(app_commands.Choice(name="-1", value="-1"))
        modifier_list.append(app_commands.Choice(name="-2", value="-2"))
        modifier_list.append(app_commands.Choice(name="-3", value="-3"))
        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(basic = choice_list )
        @app_commands.choices(modifier = modifier_list)
        
        async def city_status_one_move_command(interaction: discord.Interaction, basic: app_commands.Choice[str], modifier: app_commands.Choice[str]=None):
            command = basic.value
            mod = '+0'
            if (modifier != None):
              mod = modifier.value
          
            if(interaction.locale ==discord.Locale.spain_spanish):
              input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
              command =input.data_manager.__get_command_in_message__(command).languages['español']

            command = command + mod
            response = await input.get_response(command, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
            await interaction.response.send_message(embed=response)
          #City Status Two Moves
      if(command.type == input.data_manager.COMMAND_TYPE.command_city_move_status_2_list.name):
        list = input.data_manager.commands_manager.__get_list__( input.data_manager.COMMAND_TYPE.command_city_move_status_2.name)
        choice_list = []
        for move_command in list:
          choice_list.append(app_commands.Choice(name=move_command.languages['english'], value=move_command.languages['english']))

        modifier_list = []  
        modifier_list.append(app_commands.Choice(name="+4", value="+4"))
        modifier_list.append(app_commands.Choice(name="+3", value="+3"))
        modifier_list.append(app_commands.Choice(name="+2", value="+2"))
        modifier_list.append(app_commands.Choice(name="+1", value="+1"))
        modifier_list.append(app_commands.Choice(name="0", value="0"))
        modifier_list.append(app_commands.Choice(name="-1", value="-1"))
        modifier_list.append(app_commands.Choice(name="-2", value="-2"))
        modifier_list.append(app_commands.Choice(name="-3", value="-3"))
        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(basic = choice_list )
        @app_commands.choices(modifier = modifier_list)
        
        async def city_status_two_move_command(interaction: discord.Interaction, basic: app_commands.Choice[str], modifier: app_commands.Choice[str]=None):
            command = basic.value
            mod = '+0'
            if (modifier != None):
              mod = modifier.value
          
            if(interaction.locale ==discord.Locale.spain_spanish):
              input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
              command =input.data_manager.__get_command_in_message__(command).languages['español']

            command = command + mod
            response = await input.get_response(command, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
            await interaction.response.send_message(embed=response)
          #City Status Three Moves
      if(command.type == input.data_manager.COMMAND_TYPE.command_city_move_status_3_list.name):
        list = input.data_manager.commands_manager.__get_list__( input.data_manager.COMMAND_TYPE.command_city_move_status_3.name)
        choice_list = []
        for move_command in list:
          choice_list.append(app_commands.Choice(name=move_command.languages['english'], value=move_command.languages['english']))

        modifier_list = []  
        modifier_list.append(app_commands.Choice(name="+4", value="+4"))
        modifier_list.append(app_commands.Choice(name="+3", value="+3"))
        modifier_list.append(app_commands.Choice(name="+2", value="+2"))
        modifier_list.append(app_commands.Choice(name="+1", value="+1"))
        modifier_list.append(app_commands.Choice(name="0", value="0"))
        modifier_list.append(app_commands.Choice(name="-1", value="-1"))
        modifier_list.append(app_commands.Choice(name="-2", value="-2"))
        modifier_list.append(app_commands.Choice(name="-3", value="-3"))
        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(basic = choice_list )
        @app_commands.choices(modifier = modifier_list)
        
        async def city_status_three_move_command(interaction: discord.Interaction, basic: app_commands.Choice[str], modifier: app_commands.Choice[str]=None):
            command = basic.value
            mod = '+0'
            if (modifier != None):
              mod = modifier.value
          
            if(interaction.locale ==discord.Locale.spain_spanish):
              input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
              command =input.data_manager.__get_command_in_message__(command).languages['español']

            command = command + mod
            response = await input.get_response(command, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
            await interaction.response.send_message(embed=response)
          #Faction Moves
      if(command.type == input.data_manager.COMMAND_TYPE.command_faction_move_list.name):
        list = input.data_manager.commands_manager.__get_list__( input.data_manager.COMMAND_TYPE.command_faction_move.name)
        choice_list = []
        for move_command in list:
          choice_list.append(app_commands.Choice(name=move_command.languages['english'], value=move_command.languages['english']))

        modifier_list = []  
        modifier_list.append(app_commands.Choice(name="+4", value="+4"))
        modifier_list.append(app_commands.Choice(name="+3", value="+3"))
        modifier_list.append(app_commands.Choice(name="+2", value="+2"))
        modifier_list.append(app_commands.Choice(name="+1", value="+1"))
        modifier_list.append(app_commands.Choice(name="0", value="0"))
        modifier_list.append(app_commands.Choice(name="-1", value="-1"))
        modifier_list.append(app_commands.Choice(name="-2", value="-2"))
        modifier_list.append(app_commands.Choice(name="-3", value="-3"))
        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(basic = choice_list )
        @app_commands.choices(modifier = modifier_list)
        
        async def faction_move_command(interaction: discord.Interaction, basic: app_commands.Choice[str], modifier: app_commands.Choice[str]=None):
            command = basic.value
            mod = '+0'
            if (modifier != None):
              mod = modifier.value
          
            if(interaction.locale ==discord.Locale.spain_spanish):
              input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
              command =input.data_manager.__get_command_in_message__(command).languages['español']

            command = command + mod
            response = await input.get_response(command, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
            await interaction.response.send_message(embed=response)
          #Playbooks
      if(command.type == input.data_manager.COMMAND_TYPE.command_playbook_list.name):
        list = input.data_manager.commands_manager.__get_list__( input.data_manager.COMMAND_TYPE.command_playbook.name)
        choice_list = []
        for playbook in list:
          choice_list.append(app_commands.Choice(name=playbook.languages['english'], value=playbook.languages['english']))

        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(playbooks = choice_list )
        async def playbooks_command(interaction: discord.Interaction, playbooks: app_commands.Choice[str]):
          name = playbooks.value
          if(interaction.locale ==discord.Locale.spain_spanish):
            input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
            name =input.data_manager.__get_command_in_message__(name).languages['español']
            
          response = await input.get_response(name, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
          await interaction.response.send_message(embed=response)    
#Playbooks Moves
      if(command.type == input.data_manager.COMMAND_TYPE.command_playbook.name):
        playbook = input.data_manager.playbooks_manager.get_playbook(command.id)
        list = input.data_manager.commands_manager.get_playbook_move_list(input.data_manager, playbook.command )
        choice_list = []
        for move_command in list:
          choice_list.append(app_commands.Choice(name=move_command.languages['english'], value=move_command.languages['english']))
    
        modifier_list = []  
        modifier_list.append(app_commands.Choice(name="+4", value="+4"))
        modifier_list.append(app_commands.Choice(name="+3", value="+3"))
        modifier_list.append(app_commands.Choice(name="+2", value="+2"))
        modifier_list.append(app_commands.Choice(name="+1", value="+1"))
        modifier_list.append(app_commands.Choice(name="0", value="0"))
        modifier_list.append(app_commands.Choice(name="-1", value="-1"))
        modifier_list.append(app_commands.Choice(name="-2", value="-2"))
        modifier_list.append(app_commands.Choice(name="-3", value="-3"))

        @tree.command(name=_T(command.languages['english']))
        @app_commands.choices(playbook = choice_list )
        @app_commands.choices(modifier = modifier_list)
        async def playbook_move_command(interaction: discord.Interaction, playbook: app_commands.Choice[str], modifier: app_commands.Choice[str]=None):
          command = playbook.value
          mod = '0'
          if(modifier != None):
            mod = modifier.value
          
          if(interaction.locale ==discord.Locale.spain_spanish):
              input.data_manager.localizer.lang = input.data_manager.localizer.LANGUAGES.español
              command =input.data_manager.__get_command_in_message__(command).languages['español']

          command = command + mod
          response = await input.get_response(command, interaction.user.display_name ,interaction.user.display_avatar, interaction.guild.name )
          await interaction.response.send_message(embed=response)