package soturi.commands;

import java.io.File;
import java.util.ArrayList;
import java.util.Random;
import net.dv8tion.jda.core.events.message.MessageReceivedEvent;

/**
 * @author qanazoga
 * @version 11/20/2016
 */
public class MfwCommand implements Command {
    @Override
    public String help() {
        return "mfw you don't know what this command does. -_-";
    }

    @Override
    public void action(MessageReceivedEvent e) {
        ArrayList<File> mfw = new ArrayList<>();
        try {
            File mfwFolder = new File("src/mfw");
            if (mfwFolder.exists()) {
                try {
                    for (File pepe : mfwFolder.listFiles()) {
                        mfw.add(pepe);
                    }
                } catch (Exception ex) {
                    System.out.println("[ERROR] Pepes not found!");
                }
                Random rand = new Random();
                e.getChannel().sendFile(mfw.get(rand.nextInt(mfw.size())), null).queue();
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}