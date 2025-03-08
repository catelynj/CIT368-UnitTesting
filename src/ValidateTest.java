package src;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class ValidateTest {
  @Test
  void testGrade() {
    // happy path
    assertTrue(Validate.grade(50.00) == 'F');
    assertTrue(Validate.grade(90.00) == 'A');
    assertFalse(Validate.grade(20.50) == 'B');

    // abuse cases
    assertFalse(Validate.grade(-800.00) == 'F');
    assertFalse(Validate.grade(9000.00) == 'A');

  }

  @Test
  void testIp() {

    // happy path
    assertTrue(Validate.ip("174.59.136.110"));
    assertTrue(Validate.ip("76.208.138.180"));

    // abuse cases
    assertFalse(Validate.ip(""));
    assertFalse(Validate.ip("abc.def.ghi.jkl"));
    assertFalse(Validate.ip("256.256.256.256"));
    assertFalse(Validate.ip("192.168.1"));
    assertFalse(Validate.ip("192.168.1.1.1"));
    assertFalse(Validate.ip("192.168.01.1"));
    assertFalse(Validate.ip("192.168.1.1abc"));
  }

  @Test
  void testIsDomain() {
    // happy path
    assertTrue(Validate.isDomain("google.com"));
    assertTrue(Validate.isDomain("c8win.xyz"));

    // abuse cases
    assertFalse(Validate.isDomain(""));
    assertFalse(Validate.isDomain("<img src=" + "https://placecats.com/400/400" + "/>"));
    assertFalse(Validate.isDomain("google.com/../../../../../../../../../../../"));
    assertFalse(Validate.isDomain("website......com"));
    assertFalse(Validate.isDomain("_.com"));
    assertFalse(Validate.isDomain(
        "nooffense-butifyourdomainnameislongenoughthatitthreatenstoreachthemaximumnumberofcharactersallowed-maybeyoushouldnotbeallowedtoownawebsite.likewhohastimefortypingallofthisoutbrother/icanteventhinkofenoughwordstoreachthemaximumnumber-thatshowyouknowitstoomany"));

  }

  @Test
  void testIsInDomain() {

    // happy path
    assertTrue(Validate.isInDomain("google.com", "https://google.com/images"));
    assertTrue(Validate.isInDomain("website.com", "https://subdomain.website.com"));
    assertTrue(Validate.isInDomain("website.com", "http://website.com:8080/path"));

    // abuse cases
    assertFalse(Validate.isInDomain("", ""));
    assertFalse(Validate.isInDomain("website.com", "abcd://notawebsite.com"));
    assertFalse(Validate.isInDomain("website.com", "http://website.org"));
    assertFalse(Validate.isInDomain("website.com", "https://website.com.website.org"));
  }

  @Test
  void testIsLat() {
    assertTrue(Validate.isLat(25.3));
    assertTrue(Validate.isLat(-43.8));
    assertTrue(Validate.isLat(0.0));

    assertFalse(Validate.isLat(-90.00000001));
    assertFalse(Validate.isLat(90.00000000001));
  }

  @Test
  void testIsLng() {
    assertTrue(Validate.isLng(-143.2));
    assertTrue(Validate.isLng(179.999999999));
    assertTrue(Validate.isLng(0.0));

    assertFalse(Validate.isLng(-180.00000001));
    assertFalse(Validate.isLng(180.00000000001));

  }

  @Test
  void testIsUrl() {

    assertTrue(Validate.isUrl("http://google.com/images"));
    assertTrue(Validate.isUrl("https://c8win.xyz/projects"));

    assertFalse(Validate.isUrl(""));
    assertFalse(Validate.isUrl("<img src=" + "https://placecats.com/400/400" + "/>"));
    assertFalse(Validate.isUrl("https://                   .com"));
    assertFalse(Validate.isUrl("_https://google.com"));
    assertFalse(Validate.isUrl("https://google.123"));
  }

  @Test
  void testMac() {
    assertTrue(Validate.mac("03-9F-05-F2-4E-A5"));
    assertTrue(Validate.mac("03:9F:05:F2:4E:A5"));
    assertTrue(Validate.mac("03:9a:05:f2:6e:b3"));

    assertFalse(Validate.mac(""));
    assertFalse(Validate.mac("ma:ca:dd:re:ss"));
  }

  @Test
  void testMd5() {
    assertTrue(Validate.md5("2617a541acbca3cddaeb41cbfb4a58df"));
    assertTrue(Validate.md5("dd2084b40a224997294bdeb527c426bd"));

    assertFalse(Validate.md5(null));
    assertFalse(Validate.md5(""));
    assertFalse(Validate.md5("totallysecrethashvalue1234!"));
    assertFalse(Validate.md5("abcdefghijklmnopqrstuvwxyz12343dd"));
    assertFalse(Validate.md5("d41d8cd98f00b204e9800998ecf8427ee"));
    assertFalse(Validate.md5("z41d8cd98f00b204e9800998ecf8427e"));
  }

  @Test
  void testSanitize() {

  }

  @Test
  void testStripNull() {

  }

  @Test
  void testZip() {
    assertTrue(Validate.zip("17028"));
    assertTrue(Validate.zip("00000"));

    assertFalse(Validate.zip("abcde"));
    assertFalse(Validate.zip("     12345"));
  }
}
