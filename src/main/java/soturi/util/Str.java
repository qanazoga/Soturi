package soturi.util;

public class Str {
	public static boolean containsAll(String str, String...args) {
		boolean containsAll = true;
		
		for (String s : args) {
			if (!str.contains(s))
				containsAll = false;
		}		
		return containsAll;
	}
}
