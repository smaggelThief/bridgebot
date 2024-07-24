const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('question')
		.setDescription('more confusion'),
	async execute(interaction) {
		await interaction.reply('??');
		
	},
};