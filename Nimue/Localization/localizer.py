import pandas as pd
import logging
from discord import app_commands
import discord
from enum import Enum
import os

logger = logging.getLogger(" NIMUE ")

class Localizer:
  LANGUAGES = Enum('LANGUAGES', 'none english español')


  def __init__(self):
    self.lang = self.LANGUAGES.english
    self.__load_info__()
    self.__load_moves__()
    self.__load_playbooks__()
    self.__load_utils__()
    

  def __load_info__(self):
    self._info_dataframe = pd.read_csv(
      "Nimue/Localization/Base/localization_info.csv")
    self._info_dataframe.set_index("localization_id", drop=True, inplace=True)
    self._info_dataframe.fillna('-', inplace=True)
    self.dictionary_info = self._info_dataframe.to_dict(orient="index")
    
  def __load_moves__(self):
    self._moves_dataframe = pd.read_csv(
      "Nimue/Localization/Base/localization_moves.csv")

    for filename in os.listdir("Nimue/Localization/Playbooks"):
      file = os.path.join("Nimue/Localization/Playbooks", filename)
      if os.path.isfile(file):
        playbook_dataframe = pd.read_csv(file)
        self._moves_dataframe = pd.concat(
          [self._moves_dataframe, playbook_dataframe], ignore_index=True)

    self._moves_dataframe.set_index("localization_id", drop=True, inplace=True)
    self._moves_dataframe.fillna('-', inplace=True)
    self.dictionary_moves = self._moves_dataframe.to_dict(orient="index")

  def __load_playbooks__(self):
    self._playbooks_dataframe = pd.read_csv(
      "Nimue/Localization/Base/localization_playbooks.csv")
    self._playbooks_dataframe.set_index("localization_id",
                                        drop=True,
                                        inplace=True)
    self._playbooks_dataframe.fillna('-', inplace=True)
    self.dictionary_playbooks = self._playbooks_dataframe.to_dict(
      orient="index")

  def __load_utils__(self):
    self._utils_dataframe = pd.read_csv(
      "Nimue/Localization/localization_utils.csv")
    self._utils_dataframe.set_index("localization_id", drop=True, inplace=True)
    self._utils_dataframe.fillna('-', inplace=True)
    self.dictionary_utils = self._utils_dataframe.to_dict(orient="index")


  def get_info(self, key):
    return self.dictionary_info[key][self.lang.name]
  def get_move_with_key(self, key):
    move = self.dictionary_moves[key][self.lang.name]
    if (move == '-'):
      if ('name' in key):
        move = self.get_utils_with_key("empty_title")
      if ('blurb' in key):
        move = self.get_utils_with_key("empty_blurb")

    return move

  def get_playbook_with_key(self, key):
    try:
      playbook = self.dictionary_playbooks[key][self.lang.name]
      return playbook
    except KeyError:
      playbook = '-'
      return playbook

  def get_utils_with_key(self, key):
    return self.dictionary_utils[key][self.lang.name]


class Discord_Translator(app_commands.Translator):
  
  
  def __init__(self, data_manager):
    self.data_manager = data_manager

  async def load(self):
    logger.info("Load_ Discord_Translator")
    # this gets called when the translator first gets loaded!

  async def unload(self):
    logger.info("Unload_ Discord_Translator")
    # in case you need to switch translators, this gets called when being removed

  async def translate(self, string: app_commands.locale_str,
                      locale: discord.Locale,
                      context: app_commands.TranslationContext):
    """
    `locale_str` is the string that is requesting to be translated
    `locale` is the target language to translate to
    `context` is the origin of this string, eg TranslationContext.command_name, etc
    This function must return a string (that's been translated), or `None` to signal no available translation available, and will default to the original.
    """

    if (locale == discord.Locale.spain_spanish):      
      translation = self.data_manager.__get_command_in_message__(string.message)
      if(translation):
        message_str = translation.languages['español'] 
      else:        
        message_str = None
    else:
      message_str = None
    return message_str
