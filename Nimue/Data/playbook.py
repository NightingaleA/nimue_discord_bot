from Utils.text_formatter import Text_Formatter
import discord

class Playbook:
  def __init__(self, id, command, name, blurb, source):
    self.formatter = Text_Formatter()
    self.id = id
    self.command = command
    self.name = name
    self.blurb = blurb
    self.source = source

  def parse_playbook(self, data_manager):
    notation_needed = False
    response = ''
    title = data_manager. localizer.get_utils_with_key('asking_for') + data_manager.localizer.get_playbook_with_key(self.name)
    if (data_manager.localizer.get_playbook_with_key(self.name) == '-'):
      title = data_manager.localizer.get_utils_with_key("empty_title")

    if (data_manager.localizer.get_playbook_with_key(self.blurb) == '-'):
      response = data_manager.localizer.get_utils_with_key("empty_blurb") 
    else:      
      response = data_manager.localizer.get_playbook_with_key(self.blurb) + self.formatter.newline
      
    response = response + self.formatter.newline + self.formatter.newline + self.formatter.newline 
    response = response + self.formatter.bold.format( data_manager. localizer.get_utils_with_key('moves'))
    response = response + self.formatter.newline 
    response = response + self.formatter.quote
    move_list = data_manager.commands_manager.get_playbook_move_list(data_manager, self.command)
    response, unussed_title, notation_needed = data_manager.commands_manager.get_formated_list( data_manager.localizer, response, '',move_list, notation_needed)
    
    embed = discord.Embed(title=title, colour=5450873, description = response)
    embed.set_author(name= data_manager.current_command.user_display_name )
    embed.set_thumbnail(url= data_manager.current_command.avatar)

    if (notation_needed):
      footer = self.formatter.newline + self.formatter.newline + self.formatter.notation + data_manager.localizer.get_utils_with_key(
        "notation_explanation")
      embed.set_footer(text=footer)
      
    return embed