import discord
from discord.ext import commands
from discordbot import Module
from discordbot import modules_load, modules_remove

class Load(Module):
	'''Loads, unloads and reloads packages.'''

	@commands.command(usage='<package>')
	async def load(self, ctx: commands.Context, extension: str = None) -> None:
		'''Loads new package.'''
		if extension is not None:
			if not extension == 'all':
				try:
					self.bot.load_extension("discordbot.cogs.{}".format(extension))
				except commands.ExtensionError as e:
					await ctx.send(e.__str__().replace('discordbot.cogs.', ''))
			else:
				modules_load(self.bot)

	@commands.command(usage='<package>')
	async def reload(self, ctx, extension: str = None) -> None:
		'''Reloads package.'''
		if extension is not None:
			if not extension == 'all':
				try:
					self.bot.unload_extension("discordbot.cogs.{}".format(extension))
					self.bot.load_extension("discordbot.cogs.{}".format(extension))
				except commands.ExtensionError as e:
					await ctx.send(e.__str__().replace('discordbot.cogs.', ''))
			else:
				modules_remove(self.bot)
				modules_load(self.bot)

	@commands.command(usage='<package>')
	async def unload(self, ctx, extension: str = None):
		'''Remove package'''
		if extension is not None:
			if not extension == 'all':
				try:
					self.bot.unload_extension("discordbot.cogs.{}".format(extension))
				except commands.ExtensionError as e:
					await ctx.send(e.__str__().replace('discordbot.cogs.', ''))
			else:
				modules_remove(self.bot)

def setup(bot: commands.Bot) -> None:
	bot.add_cog(Load(bot))