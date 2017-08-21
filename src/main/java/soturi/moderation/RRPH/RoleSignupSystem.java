package soturi.moderation.RRPH;

import net.dv8tion.jda.core.events.message.react.MessageReactionAddEvent;
import net.dv8tion.jda.core.events.message.react.MessageReactionRemoveEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;
import java.io.BufferedReader;
import java.io.FileReader;
import org.json.*;

/**
 * 
 * @author qanazoga
 * @version 08/20/2017
 */

public class RoleSignupSystem extends ListenerAdapter {
	
	@Override
	public void onMessageReactionAdd(MessageReactionAddEvent e) {
		if (e.getChannel().getId().equals("347916942335541248")) {
			try {
				String jsonData = readFile("data/message_roles.json");
				JSONObject jobj = new JSONObject(jsonData);
				
				if (jobj.keySet().contains(e.getMessageId())) {
					System.out.println("Adding role @" + jobj.getString(e.getMessageId()) + " to " + e.getMember().getEffectiveName());
					e.getGuild().getController().addRolesToMember(
							e.getMember(), e.getGuild().getRolesByName(jobj.getString(e.getMessageId()), true)
							).queue();
				}
				
			//TODO: Write better catches :P	
			} catch (Exception ex) {
				ex.printStackTrace();
			} 
		}
	}
	
	@Override
	public void onMessageReactionRemove(MessageReactionRemoveEvent e) {
		if (e.getChannel().getId().equals("347916942335541248")) {
			try {
				String jsonData = readFile("data/message_roles.json");
				JSONObject jobj = new JSONObject(jsonData);
				
				if (jobj.keySet().contains(e.getMessageId())) {
					System.out.println("Removing role @" + jobj.getString(e.getMessageId()) + " from " + e.getMember().getEffectiveName());
					e.getGuild().getController().removeRolesFromMember(
							e.getMember(), e.getGuild().getRolesByName(jobj.getString(e.getMessageId()), true)
							).queue();
				}
				
			//TODO: Write better catches :P	
			} catch (Exception ex) {
				ex.printStackTrace();
			} 
		}
	}
	
	public static String readFile(String filename) {
	    String result = "";
	    try {
	        BufferedReader br = new BufferedReader(new FileReader(filename));
	        StringBuilder sb = new StringBuilder();
	        String line = br.readLine();
	        while (line != null) {
	            sb.append(line);
	            line = br.readLine();
	        }
	        result = sb.toString();
	        br.close();
	    } catch(Exception e) {
	        e.printStackTrace();
	    }
	    return result;
	}

}
