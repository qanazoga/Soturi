package soturi;

import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/**
 * @author qanazoga
 * @version 11/20/2016
 */
public class MessageHandler {
	String chandler = "#";
	String shitbot = "#";
	String lcMessage;

	public MessageHandler(MessageReceivedEvent event) {
		lcMessage = event.getMessage().getContent().toLowerCase();
		
		if(
			lcMessage.contains("fuck u") || 
            lcMessage.contains("fuk u") ||
            lcMessage.contains("fuq u")
        ) event.getChannel().sendMessage("fuck u").queue();
		
		if (event.getGuild().getMemberById(shitbot) == event.getMember()) {
			event.getChannel().sendMessage(event.getAuthor().getAsMention() + " is fucking trash");
		}
		
		
		if (
			event.getGuild().getMemberById(chandler) == event.getMember() &&
			(lcMessage.contains("melly") || lcMessage.contains("mel")) &&
			(lcMessage.contains("need") || lcMessage.contains("want") || lcMessage.contains("ask"))
		) event.getChannel().sendMessage("\\*whip cracks*").queue();
	}
}
