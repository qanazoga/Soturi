package soturi;

import java.util.HashMap;
import java.util.Scanner;

import net.dv8tion.jda.core.AccountType;
import net.dv8tion.jda.core.JDA;
import net.dv8tion.jda.core.JDABuilder;
import net.dv8tion.jda.core.entities.Game;
import soturi.commands.*;

/**
 * @author qanazoga
 * @version 11/20/2016
 */
public class Bot {
	private static String botToken = "#";
	private static JDA jda;
	private static HashMap<String, Command> commands = new HashMap<>();
	
	public static void main(String[] args) {
		// Add commands here.
        commands.put(">help", new HelpCommand());
        commands.put(">kickraider", new KickRaiderCommand());
        commands.put(">kms", new KillMyselfCommand());
        commands.put(">kys", new KillUrselfCommand());
        commands.put(">pepe", new PepeCommand());
        commands.put(">mfw", new MfwCommand());
        
		// Try logging in.
		try {
			 jda = new JDABuilder(AccountType.BOT).addListener(new BotListener()).setToken(botToken).buildBlocking();
			 jda.setAutoReconnect(true);
			 jda.getPresence().setGame(Game.of(">help"));
		 } catch(Exception e) {
			 System.out.println("[CRITICAL FAILURE] LOGIN FAILED!!!");
			 e.printStackTrace();
		 }
		
		// This section lets you send messages to RRPH.
        Scanner in = new Scanner(System.in);
        String line = " ";
        while (line.equalsIgnoreCase("quit") == false) {
            line = " ";
            line = in.nextLine();
            if (!line.isEmpty()) jda.getGuildById("#").getTextChannelById("#").sendMessage(line).queue();
        }
        in.close();
        System.exit(0);
	}
	
	public static HashMap<String, Command> getCommands() {
        return commands;
    }
}
