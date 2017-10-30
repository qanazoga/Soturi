package soturi.commands.RRPH;

import net.dv8tion.jda.core.entities.Guild;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;
import soturi.commands.Command;

public class AbooseModeCommand implements Command{

	@Override
	public String help() {
		return "Use this if you're qanazoga and you need to ABOOSE some chats";
	}

	@Override
	public void action(MessageReceivedEvent e) {
		System.out.println("Aboosemode command triggered...");
		
		if (e.getAuthor().getId().equals("135347294093443072") && e.getGuild().getId().equals("138687693193347073")) {
			System.out.println("It is qanazoga, we're in the right chat...");
			
			Guild rrph = e.getGuild();
			if (e.getGuild().getMembersWithRoles(e.getGuild().getRolesByName("admin", true)).contains(e.getMember())) {
				System.out.println("Removing admin role...");
				rrph.getController().removeRolesFromMember(e.getMember(), rrph.getRolesByName("admin", true)).queue();
			} else {
				System.out.println("Adding admin role...");
				rrph.getController().addRolesToMember(e.getMember(), rrph.getRolesByName("admin", true)).queue();
			}
			System.out.println("Done!");
		}
		
	}

}
