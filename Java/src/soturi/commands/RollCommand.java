package soturi.commands;

import java.util.ArrayList;
import java.util.Random;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/**
 * @author qanazoga
 * @version 12/17/2016
 */
public class RollCommand implements Command {

	@Override
	public String help() {
		return "<number of dice> d <sides on each die>: for example, '>roll 3d6' will roll 3 six sided dice.";
	}

	@Override
	public void action(MessageReceivedEvent event) {
		Random rand = new Random();
		int numberOfDice = 1;
		int sidesOnDie = 20;
		ArrayList<Integer> rolls = new ArrayList<>();
		String toInt = "";
		
		for (char c : event.getMessage().getContent().toLowerCase().toCharArray()) {
			if (c == "d".charAt(0)) {
				if (!toInt.isEmpty()) {
					numberOfDice = Integer.valueOf(toInt);
					toInt = "";
				}
			}
			if (Character.isDigit(c)) toInt += c;
		}
		
		if (!toInt.isEmpty()) sidesOnDie = Integer.valueOf(toInt);
	
		
		for (int i = 0; i < numberOfDice; i++) {
			rolls.add(rand.nextInt(sidesOnDie) +1);
		}
		
		event.getChannel().sendMessage(event.getAuthor().getAsMention() + " rolled " + rolls).queue();
	}
}
