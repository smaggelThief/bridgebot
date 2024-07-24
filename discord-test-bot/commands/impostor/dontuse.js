const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('donotuse')
		.setDescription('Forbidden'),
	async execute(interaction, member) {
		await interaction.reply('Sucks to be you!');
        x = 2;
        while (x = 2){
            await interaction.followUp({ content: ("@everyone ur an L lol!"), ephemeral: true });
        }
	},
};