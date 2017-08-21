package soturi.commands;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

public class VoteCommand implements Command {

	@Override
	public String help() {
		return "Adds up and down arrow reactions to your message.";
	}

	@Override
	public void action(MessageReceivedEvent e) {
		e.getMessage().addReaction("⬆").complete();
		e.getMessage().addReaction("⬇").complete();		
	}
}
