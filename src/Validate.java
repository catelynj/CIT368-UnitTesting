package src;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Validate {

  public static boolean zip(String input) {
    Pattern fiveDigits = Pattern.compile("^[0-9]{5}$");
    Matcher match = fiveDigits.matcher(input);
    return match.matches();
  }

  private static boolean minor(int age) {
    if (age > 17) {
      return false;
    }

    return true;
  }

  private static boolean email(String input) {
    if (input.contains("@") && input.contains("."))
      return true;

    return false;
  }

  public static boolean isLat(Double value) {
    return value >= -90 && value <= 90;
  }

  public static boolean isLng(Double value) {
    return value >= -180 && value <= 180;
  }

  public static boolean isDomain(String input) {
    // not perfect, but probably 95% accurate.
    Pattern p = Pattern.compile("^[a-zA-Z0-9-]{2,253}\\.[a-zA-Z]{1}[a-zA-Z0-9]{1,}$");
    Matcher m = p.matcher(input);

    return m.find();
  }

  public static boolean isInDomain(String domain, String url) {

    if (domain == null || url == null || domain.isEmpty() || url.isEmpty()) {
      return false;
    }

    String regex = "^(https?://)?([a-zA-Z0-9-]+\\.)*" + Pattern.quote(domain) + "(?::\\d+)?(/|$)";

    Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
    Matcher m = p.matcher(url);

    return m.find();

  }

  public static boolean isUrl(String input) {
    if (input == null || input.isEmpty()) {
      return false;
    }
    // not perfect, but probably 95% accurate.
    Pattern p = Pattern.compile("^http(s)?:\\/\\/(.*?)\\.[0-9a-z]{2,52}\\/.*$");
    Matcher m = p.matcher(input);

    return m.find();
  }

  // grade validation
  public static char grade(Double value) {

    if (value < 60 && value >= 0) {
      return 'F';
    } else if (value >= 60 && value < 70) {
      return 'D';
    } else if (value >= 70 && value < 80) {
      return 'C';
    } else if (value >= 80 && value < 90) {
      return 'B';
    } else if (value >= 90 && value <= 100) {
      return 'A';
    } else {
      System.err.println("Invalid Grade");
      return 'X';
    }
  }

  public static String sanitize(String sql) {
    if (sql == null) {
      return null;
    }

    sql.toUpperCase();

    // sql = sql.replaceAll("ADMIN", "");
    // sql = sql.replaceAll("OR", "");
    // sql = sql.replaceAll("COLLATE", "");
    // sql = sql.replaceAll("DROP", "");
    // sql = sql.replaceAll("AND", "");
    // sql = sql.replaceAll("UNION", "");
    // sql = sql.replaceAll("/*", "");
    // sql = sql.replaceAll("*/", "");
    // sql = sql.replaceAll("//", "");
    // sql = sql.replaceAll(";", "");
    // sql = sql.replaceAll("||", "");
    // sql = sql.replaceAll("&&", "");
    // sql = sql.replaceAll("--", "");
    // sql = sql.replaceAll("#", "");
    // sql = sql.replaceAll("=", "");
    // sql = sql.replaceAll("!=", "");
    // sql = sql.replaceAll("<>", "");

    // maybe try using the matcher .find() to see if any keywords or special
    // characters show up together and then sanitizing it from there ??????

    return sql.trim();
  }

  /**
   * TODO: Does this look correct? Can you improve it to pass more tests?
   */
  public static String stripNull(String filter) {
    filter = filter.toUpperCase().replace("NULL", "");

    return filter;
  }

  // IP address validation
  public static boolean ip(String input) {
    String regex = "^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$";

    Pattern p = Pattern.compile(regex);
    Matcher m = p.matcher(input);

    return m.matches();
  }

  // MAC address validation
  public static boolean mac(String input) {

    if (input == null || input.isEmpty()) {
      return false;
    }

    String regex = "^([0-9A-Fa-f]{2}[:-]?\\s*){5}([0-9A-Fa-f]{2})$";

    Pattern p = Pattern.compile(regex);
    Matcher m = p.matcher(input.toUpperCase());

    return m.matches();
  }

  // hash value validation
  public static boolean md5(String input) {
    if (input == null || input.isEmpty()) {
      return false;
    }

    String regex = "^[a-fA-F0-9]{32}$";
    Pattern p = Pattern.compile(regex);
    Matcher m = p.matcher(input);

    return m.matches();
  }
}
