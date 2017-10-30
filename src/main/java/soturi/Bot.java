package soturi;

import java.util.HashMap;
import java.util.Scanner;

import net.dv8tion.jda.core.AccountType;
import net.dv8tion.jda.core.JDA;
import net.dv8tion.jda.core.JDABuilder;
import net.dv8tion.jda.core.entities.Game;
import soturi.commands.*;
import soturi.commands.RRPH.AbooseModeCommand;
import soturi.commands.memes.MFWCommand;
import soturi.moderation.RRPH.AutoMod;
import soturi.moderation.RRPH.Librarian;
import soturi.moderation.RRPH.RoleSignupSystem;
import soturi.Tokens.*;

/**
 * 
 * @author qanazoga
 * @version 08/20/2017
 */
public class Bot {
	private static JDA jda;
	private static HashMap<String, Command> commands = new HashMap<>();
	
	public static void main(String[] args) {
		// Add commands here.
        commands.put(">help", new HelpCommand());
        commands.put(">mfw", new MFWCommand());
        commands.put(">roll", new RollCommand());
        commands.put(">vote", new VoteCommand());
        commands.put(">aboosemode", new AbooseModeCommand());
        
		// Try logging in.
		try {
			 jda = new JDABuilder(AccountType.BOT)
					 .setToken(Tokens.botToken)
					 .addEventListener(
							 new BotListener(),
							 new Librarian(),
							 new AutoMod(),
							 new RoleSignupSystem()
							 )					 
					 .setAutoReconnect(true)
					 .buildBlocking();
			 jda.getPresence().setGame(Game.of(">help"));
		 } catch(Exception e) {
			 System.out.println("[CRITICAL FAILURE] LOGIN FAILED!!!");
			 e.printStackTrace();
		 }
		
		// This section lets you send messages to RRPH.
        Scanner in = new Scanner(System.in);
        String line = " ";
        while (!line.equalsIgnoreCase("quit")) {
            line = " ";
            line = in.nextLine();
            if (!line.isEmpty()) {
            	jda.getGuildById(Tokens.guilds.get(Guilds.RRPH)).getTextChannelById(Tokens.channels.get(Channels.MEMEHELL)).sendMessage(line).queue();
            }
        }
        in.close();
        System.exit(0);
	}
	
	public static HashMap<String, Command> getCommands() {
        return commands;
    }
}
