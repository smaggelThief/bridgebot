const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('logic')
		.setDescription('confusion'),
	async execute(interaction) {
		await interaction.reply('ok now im confused');
		
	},
};