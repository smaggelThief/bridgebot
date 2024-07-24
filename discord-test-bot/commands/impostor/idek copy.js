const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('no')
		.setDescription('a classic'),
	async execute(interaction) {
		await interaction.reply('im correct no?');
		
	},
};